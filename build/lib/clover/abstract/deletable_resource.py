#!/usr/bin/env python3
"""Deletable Resource"""

from clover import BaseRequestor


class DeletableResource(BaseRequestor):

    @classmethod
    def delete(cls, sid):
        """Modifies an object."""

        return cls.request(
            method='delete',
            path=[sid]
        )
