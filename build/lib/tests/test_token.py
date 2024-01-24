#!/usr/bin/env python3
"""Token Tests"""

from clover import Token
from clover.test import MockedTestCase
from clover.test.constants import CARD
from clover.test.mock_responses import (
    CREATE_TOKEN,
    RETRIEVE_TOKEN,
    AFTER_MODIFY_RETRIEVE_TOKEN
)


class TestToken(MockedTestCase):
    
    def test_create_token(self):
        """Trys to create a token using card details."""

        self.set_mock_json(CREATE_TOKEN)

        token = Token.create(
            card=CARD
        )

        self.assertKeyValueEqual(token, 'object', 'token')

    def test_retrieve_token(self):
        """Tests token retrieval using a token ID."""
        token = CREATE_TOKEN

        token_id = token['id']

        self.set_mock_json(RETRIEVE_TOKEN)
        response = Token.retrieve(token_id)

        # Check there's a token object.
        r_token = self.assertGetValue('cloverToken', response)

        # Make sure that it is the same token.
        self.assertKeyValueEqual(r_token, 'tokenValue', token_id)

    def test_modify_token(self):
        """Tests modifying a token to become recurring."""
        token = CREATE_TOKEN

        token_id = token['id']
        new_type = "RECURRING"

        response = Token.modify(
            sid=token['id'],
            type=new_type
        )

        self.set_mock_json(AFTER_MODIFY_RETRIEVE_TOKEN)
        response = Token.retrieve(token_id)

        # Make sure that it is the same token.
        r_token = self.assertGetValue('cloverToken', response)
        self.assertKeyValueEqual(r_token, 'tokenValue', token_id)

        # Make sure that the token type is updated.
        meta = self.assertGetValue('tokenMeta', response)
        self.assertKeyValueEqual(meta, 'tokenType', new_type)
