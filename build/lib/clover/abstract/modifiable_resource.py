#!/usr/bin/env python3
"""Modifiable Resource"""

from clover import BaseRequestor


class ModifiableResource(BaseRequestor):

    @classmethod
    def modify(cls, sid, **params):
        """Modifies an object."""

        return cls.request(
            method='put',
            path=[sid],
            json=params
        )
