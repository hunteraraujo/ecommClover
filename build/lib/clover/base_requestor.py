#!/usr/bin/env python3
""" Base Requestor

Base class that wraps an endpoint.
"""

import clover
from clover import HTTPClient


class BaseRequestor(object):

    path = None

    @classmethod
    def request(cls, method, path=None, **kwargs):
        """Requests with path parameters."""

        # Append path parameters to url.
        if path is not None:
            url = cls.build_url_with_path_parameters(path)
        else:
            url = cls.get_class_url()

        response = HTTPClient.request(
            method=method,
            url=url, 
            **kwargs)
        
        return response.json()

    @classmethod
    def build_url_with_path_parameters(cls, path):
        """Builds a url with path parameters."""
        path_str = '/'.join(path)
        url_with_path = '/'.join([cls.get_class_url(), path_str])
        return url_with_path

    @classmethod
    def get_class_url(cls, version=1):
        """Builds the endpoint url."""

        url = '{base_url}/v{version}/{path}'.format(
            base_url=clover.base_url,
            version=version,
            path=cls.path
        )

        return url
