#!/usr/bin/env python3
"""Createable Resource"""

from clover import BaseRequestor


class CreatableResource(BaseRequestor):

    @classmethod
    def create(cls, **params):
        """Creates an object."""

        return cls.request(
            method='post',
            json=params
        )
