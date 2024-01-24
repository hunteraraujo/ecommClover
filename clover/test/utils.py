#!/usr/bin/env python3
"""Test Utility functions.

Random functions that are used commonly.
"""
from time import sleep
try:
    # Python 3: Mock is built in.
    from unittest.mock import patch
except ImportError:
    # Python 2.7: Mock must be installed via pip.
    from mock import patch
from clover.test.constants import DEFAULT_REQUEST_DELAY_SECS, REQUESTS_PATH

def request_delay(seconds=DEFAULT_REQUEST_DELAY_SECS):
    """Sleep for a set period of time before the next request."""
    sleep(seconds)

def mock_request(method):
    """Mocks the requests method."""

    # Form the path to the method within in the module.
    method_path = '{base_path}.{method}'.format(
                        base_path=REQUESTS_PATH,
                        method=method
    )

    # Get the patch object.
    mock = patch(method_path)

    return mock
