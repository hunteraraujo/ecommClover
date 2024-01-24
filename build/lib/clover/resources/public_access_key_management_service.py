#!/usr/bin/env python3
"""Public Access Key Management Service (PAKMS)"""

import clover
from clover import BaseRequestor


class PublicAccessKey(BaseRequestor):

    path = 'pakms/apikey'

    @classmethod
    def get_class_url(cls):
        """Overrides because PAKMS uses a different server.

        Note:
            Removed version in path.
        """

        url = '{base_url}/{path}'.format(
            base_url=clover.base_url,
            path=cls.path
        )

        return url

    @classmethod
    def retrieve(cls):
        """Retrieves PAKMS credentials."""

        return cls.request(
            method='get'
        )
