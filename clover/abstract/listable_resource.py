#!/usr/bin/env python3
"""Listable Resource"""

from clover import BaseRequestor


class ListableResource(BaseRequestor):

    @classmethod
    def list(cls, **params):
        """Retrieves a list of objects."""

        return cls.request(
            method='get',
            params=params
        )
