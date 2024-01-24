#!/usr/bin/env python3
"""API Test Case

Test case for an API resource.
"""
from unittest import TestCase
import clover
from clover.test.constants import (
    SANDBOX_ACCESS_TOKEN,
    SANDBOX_API_KEY,
    SANDBOX_MERCHANTUUID,
    SANDBOX_MID
)
from clover.utils import json_ps

class ApiTestCase(TestCase):
    
    @classmethod
    def setup_class(cls):
        """Starts mocks for HTTP requests."""

        # Sets the package wide access token.
        # Required when requesting the actual server.
        clover.access_token = SANDBOX_ACCESS_TOKEN

        clover.api_key = SANDBOX_API_KEY

        # Merchant information.
        clover.merchant_uuid = SANDBOX_MERCHANTUUID
        clover.mid = SANDBOX_MID

    def assertInDict(self, first, second, msg=None):
        """Checks that first is in second.
        
        Pretty prints dictionary.
        """
        self.assertIn(first, second, json_ps(msg))

    def assertNotInDict(self, first, second, msg=None):
        """Checks that first is not in second.
        
        Pretty prints dictionary.
        """
        self.assertNotIn(first, second, json_ps(msg))

    def assertKeyValueEqual(self, first, key, second):
        """Checks that key is in first and that the value is equal to second.
        
        Pretty prints dictionary.
        """
        self.assertInDict(key, first, msg=first)
        self.assertEqual(first[key], second, msg=json_ps(first))

    def assertGetValue(self, key, second):
        self.assertInDict(key, second, second)
        return second[key]

    def set_mock_json(self, data):
        """Dummy method for mocking subclass."""
        pass
