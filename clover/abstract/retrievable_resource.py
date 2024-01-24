#!/usr/bin/env python3
"""Retrievable Resource"""

from clover import BaseRequestor


class RetrievableResource(BaseRequestor):

    @classmethod
    def retrieve(cls, id):
        """Makes create request for an object."""

        return cls.request(
            method='get',
            path=[id]
        )

