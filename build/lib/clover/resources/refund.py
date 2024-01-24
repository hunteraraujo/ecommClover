#!/usr/bin/env python3
"""Refund"""

from clover.abstract import (
    CreatableResource,
    RetrievableResource,
    ListableResource
)


class Refund(CreatableResource, RetrievableResource, ListableResource):
    
    path = 'refunds'
