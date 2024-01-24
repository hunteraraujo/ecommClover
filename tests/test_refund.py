#!/usr/bin/env python3
"""Refund Tests"""

from clover import Refund
from clover.test import MockedTestCase
from clover.utils import json_ps
from clover.test.mock_responses import (
    CREATE_CHARGE,
    CREATE_REFUND,
    RETRIEVE_REFUND,
    LIST_REFUND
)


class TestRefund(MockedTestCase):
    
    def test_create_refund(self):
        """Tests creating a refund."""

        charge = CREATE_CHARGE

        self.set_mock_json(CREATE_REFUND)
            
        refund = Refund.create(
            charge=charge['id']
        )

        self.assertKeyValueEqual(refund, 'status', 'succeeded')

    def test_retrieve_refund(self):
        """Tests to retrieving a refund."""
        self.set_mock_json(RETRIEVE_REFUND)

        refund = CREATE_REFUND

        r_refund = Refund.retrieve(
            id=refund['id']
        )

        # Check that it isn't an error code.
        self.assertNotInDict('error', r_refund, r_refund)

        # Check that it is the same refund object.
        self.assertEqual(r_refund['id'], refund['id'], json_ps(r_refund))

    def test_list_refund(self):
        """Tests listing refunds."""
        self.set_mock_json(LIST_REFUND)

        num_refunds = 3

        refunds = Refund.list(limit=num_refunds)

        # Check that it isn't an error code.
        self.assertNotInDict('error', refunds, refunds)

        # Check that it is a list object.
        self.assertKeyValueEqual(refunds, 'object', 'list')

        # Check that the correct amount was listed.
        self.assertEqual(
            len(refunds['data']['elements']),
            num_refunds,
            json_ps(refunds)
        )
