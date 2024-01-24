#!/usr/bin/env python3
"""Customer Tests"""

import clover
from clover import Customer, Token
from clover.test import MockedTestCase
from clover.test.constants import CARD
from clover.test.mock_responses import (
    CREATE_TOKEN,
    CREATE_CUSTOMER,
    MODIFY_CUSTOMER,
    DELETE_SOURCE_CUSTOMER
)

class TestCharge(MockedTestCase):
    
    def test_create_customer(self):
        """Tests creating a customer."""

        self.set_mock_json(CREATE_TOKEN)

        token = token = Token.create(
            card=CARD
        )

        self.set_mock_json(CREATE_CUSTOMER)

        response = Customer.create(
            email="test@clover.com",
            source=token['id']
        )

        # Check that it is a customer.
        self.assertKeyValueEqual(response, 'object', 'customer')

    def test_modify_customer(self):
        """Tests modifying a customer."""

        self.set_mock_json(CREATE_TOKEN)

        token = token = Token.create(
            card=CARD
        )

        self.set_mock_json(CREATE_CUSTOMER)

        response = Customer.create(
            email="test@clover.com",
            source=token['id']
        )

        self.set_mock_json(MODIFY_CUSTOMER)

        response = Customer.modify(
            sid=response['id'],
            email="test@clover.com",
            source=token['id'],
            first_name="clover",
            last_name="test"
        )

        # Check that it is a customer.
        self.assertKeyValueEqual(response, 'object', 'customer')

        # Check that first name is updated.
        self.assertKeyValueEqual(response, 'firstName', 'clover')

        # Check that last name is updated.
        self.assertKeyValueEqual(response, 'lastName', 'test')

    def test_delete_source_customer(self):
        """Tests deleting a payment method of a customer."""

        self.set_mock_json(CREATE_TOKEN)

        token = token = Token.create(
            card=CARD
        )


        self.set_mock_json(CREATE_CUSTOMER)

        create_response = Customer.create(
            email="test@clover.com",
            source=token['id']
        )

        # Assumes only one source.
        source_id = create_response['sources']['data']['elements'][0]

        self.set_mock_json(DELETE_SOURCE_CUSTOMER)

        delete_response = Customer.delete_source(
            customer_id=create_response['id'],
            source_id=source_id
        )

        # Check that it is a deletecard.
        self.assertKeyValueEqual(delete_response, 'object', 'deletedcard')

        # Check that id matches.
        self.assertKeyValueEqual(delete_response, 'id', source_id)

        # Check that it is deleted.
        self.assertKeyValueEqual(delete_response, 'deleted', True)
