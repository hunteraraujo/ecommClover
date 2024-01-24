#!/usr/bin/env python3
"""Order Tests"""

from clover import Order
from clover.test import MockedTestCase
from clover.utils import json_ps
from clover.test.mock_responses import (
    CREATE_ORDER,
    RETRIEVE_ORDER,
    LIST_ORDER,
    MODIFY_ORDER,
    CREATE_TOKEN,
    PAY_ORDER,
    CAPTURE_ORDER,
    RETURN_ORDER
)


class TestOrder(MockedTestCase):
    
    def test_create_order(self):
        """Tests creating a order."""

        self.set_mock_json(CREATE_ORDER)
 
        order = Order.create(
            currency="usd",
            items=[
                {
                    "amount": 100,
                    "currency": "string",
                    "description": "string",
                    "parent": "string",
                    "quantity": 1,
                    "type": "discount"
                }
            ]
        )

        self.assertKeyValueEqual(order, 'status', 'created')

    def test_retrieve_order(self):
        """Tests to retrieving a order."""
        self.set_mock_json(RETRIEVE_ORDER)

        order = CREATE_ORDER

        r_order = Order.retrieve(
            id=order['id']
        )

        # Check that it isn't an error code.
        self.assertNotInDict('error', r_order, r_order)

        # Check that it is the same order object.
        self.assertEqual(r_order['id'], order['id'], json_ps(r_order))

    def test_list_order(self):
        """Tests listing orders."""
        self.set_mock_json(LIST_ORDER)

        num_orders = 3

        orders = Order.list(limit=num_orders)

        # Check that it isn't an error code.
        self.assertNotInDict('error', orders, orders)

        # Check that it is a list object.
        self.assertKeyValueEqual(orders, 'object', 'list')

        # Check that the correct amount was listed.
        self.assertEqual(
            len(orders['data']['elements']),
            num_orders,
            json_ps(orders)
        )

    def est_pay_order(self):
        """Tests paying an order."""

        self.set_mock_json(PAY_ORDER)

        order = CREATE_ORDER
        token = CREATE_TOKEN

        r_order = Order.pay(
            sid=order['id'],
            source=token['id']
        )

        # Check that it isn't an error code.
        self.assertNotInDict('error', r_order, r_order)

    def est_capture_order(self):
        """Tests capturing an order."""

        self.set_mock_json(CAPTURE_ORDER)

        order = CREATE_ORDER

        r_order = Order.capture(
            sid=order['id']
        )

        # Check that it isn't an error code.
        self.assertNotInDict('error', r_order, r_order)

    def est_return_order(self):
        """Tests returning an order."""

        self.set_mock_json(RETURN_ORDER)

        order = CREATE_ORDER

        r_order = Order.return_order(
            sid=order['id']
        )

        # Check that it isn't an error code.
        self.assertNotInDict('error', r_order, r_order)
