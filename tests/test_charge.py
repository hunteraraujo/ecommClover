#!/usr/bin/env python3
"""Charge Tests"""

from clover import Charge, Token
from clover.test import MockedTestCase
from clover.test.constants import CARD
from clover.utils import json_ps
from clover.test.mock_responses import (
    CREATE_TOKEN,
    CREATE_CHARGE,
    RETRIEVE_CHARGE,
    LIST_CHARGE
)


class TestCharge(MockedTestCase):
    
    def test_create_charge(self):
        """Trys to create a charge."""

        self.set_mock_json(CREATE_TOKEN)

        token = token = Token.create(
            card=CARD
        )

        self.set_mock_json(CREATE_CHARGE)

        charge = Charge.create(
            amount='999',
            currency='usd',
            description='Example charge',
            source=token['id'],
        )

        self.assertKeyValueEqual(charge, 'status', 'succeeded')

    def test_retrieve_charge(self):
        """Trys to retrieve a charge."""

        self.set_mock_json(CREATE_TOKEN)

        token = token = Token.create(
            card=CARD
        )

        self.set_mock_json(CREATE_CHARGE)

        charge = Charge.create(
            amount='999',
            currency='usd',
            description='Example charge',
            source=token['id'],
        )

        self.set_mock_json(RETRIEVE_CHARGE)

        r_charge = Charge.retrieve(
            id=charge['id']
        )

        # Check that it isn't an error code.
        self.assertNotInDict('error', r_charge, r_charge)

        # Check that it is the same charge object.
        self.assertEqual(r_charge['id'], charge['id'], json_ps(r_charge))

    def test_list_charge(self):
        """Tests listing charges."""

        self.set_mock_json(CREATE_TOKEN)

        token = token = Token.create(
            card=CARD
        )

        num_charges = 3

        # Make 3 charges so that they can be listed.
        for _ in range(num_charges):
            Charge.create(
                amount='999',
                currency='usd',
                description='Example charge',
                source=token['id'],
            )

        self.set_mock_json(LIST_CHARGE)

        charges = Charge.list(limit=num_charges)

        # Check that it isn't an error code.
        self.assertNotInDict('error', charges, charges)

        # Check that it is a list object.
        self.assertKeyValueEqual(charges, 'object', 'list')

        # Check that the correct amount was listed.
        self.assertEqual(
            len(charges['data']['elements']),
            num_charges,
            json_ps(charges)
        )
