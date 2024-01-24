#!/usr/bin/env python3
""" HTTP Client

HTTP Client to make requests to Clover endpoints.
"""

import requests
import clover


class HTTPClient:

    @staticmethod
    def request(method, url, headers={}, params={}, **kwargs):
        """HTTP request."""

        # Headers.
        headers['Content-Type'] = 'application/json'
        headers['Authorization'] = 'Bearer {access_token}'.format(
            access_token=clover.access_token
        )

        # Query parameters.
        params['merchantUuid'] = clover.merchant_uuid
        params['mid'] = clover.mid


        return requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            **kwargs)

    @staticmethod
    def post(url, json, headers={}, params={}):
        """POST request."""
        
        return HTTPClient.request(
            method='POST',
            url=url,
            json=json,
            headers=headers,
            params=params)

    @staticmethod
    def get(url, headers={}, params={}):
        """GET request."""
        
        return HTTPClient.request(
            method='GET',
            url=url,
            headers=headers,
            params=params)

    @staticmethod
    def put(url, json, headers={}, params={}):
        """PUT request."""

        return HTTPClient.request(
            method='PUT',
            url=url,
            headers=headers,
            params=params,
            json=json)

    @staticmethod
    def delete(url, json, headers={}, params={}):
        """DELETE request."""

        return HTTPClient.request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
            json=json)
