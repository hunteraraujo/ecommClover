#!/usr/bin/env python3
"""Token"""

import clover
from clover.abstract import (
    CreatableResource,
    RetrievableResource,
    ModifiableResource
)


class Token(CreatableResource, RetrievableResource, ModifiableResource):

    path = 'tokens'

    @classmethod
    def get_class_url(cls, version=1):
        """Overrides because Tokenization uses a different server."""

        url = '{base_url}/v{version}/{path}'.format(
            base_url=clover.tokenization_base_url,
            version=version,
            path=cls.path
        )

        return url

    @classmethod
    def request(cls, method, path=None, **kwargs):
        """Overrides because we need the api key."""

        # Add the api key into the headers just for Token.
        if 'params' in kwargs:
            headers = kwargs['headers']
        else:
            headers = {}

        headers['APIKEY'] = clover.api_key

        kwargs['headers'] = headers
        
        return super(Token, cls).request(
            method=method,
            path=path,
            **kwargs
        )
