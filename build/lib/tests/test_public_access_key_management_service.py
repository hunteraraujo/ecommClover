#!/usr/bin/env python3
"""Public Access Key Management Service Tests"""

from clover import PublicAccessKey
from clover.test import MockedTestCase
from clover.test.mock_responses import (
    RETRIEVE_PUBLIC_ACCESS_KEY
)


class TestPublicAccessKey(MockedTestCase):

    def test_retrieve_public_access_key(self):
        """Tests public access key retrieval."""

        self.set_mock_json(RETRIEVE_PUBLIC_ACCESS_KEY)

        response = PublicAccessKey.retrieve()

        # Check that it has all the required credentials.
        self.assertInDict('apiAccessKey', response)
        self.assertInDict('merchantUuid', response)
        self.assertInDict('developerAppUuid', response)
