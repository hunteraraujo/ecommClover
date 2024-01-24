#!/usr/bin/env python3
"""Mocked Test Case

Test case that will start mocking HTTP request methods.
"""
from os import environ
from clover.test import ApiTestCase, mock_request


DISABLE_MOCKING = False
if ('DISABLE_CLOVER_MOCKING' in environ and
    environ['DISABLE_CLOVER_MOCKING'] == 'true'):
    DISABLE_MOCKING = True

class MockedTestCase(ApiTestCase):
    
    @classmethod
    def setup_class(cls):
        """Starts mocks for HTTP requests."""

        if not DISABLE_MOCKING:
            # Create the patch object.
            cls.mock_request_patcher = mock_request('request')
            
            # Start the patch.
            cls.mock_request = cls.mock_request_patcher.start()

        super(MockedTestCase, cls).setup_class()

    @classmethod
    def teardown_class(cls):
        """Stops mocks for HTTP requests."""
        if not DISABLE_MOCKING:
            cls.mock_request_patcher.stop()

    def set_mock_json(self, data):
        """Sets the mock request json."""
        if not DISABLE_MOCKING:
            self.mock_request.return_value.json.return_value = data
