#!/usr/bin/env python3
"""Charge"""

from clover.abstract import (
    CreatableResource,
    RetrievableResource,
    ListableResource,
    add_resource_method
)

@add_resource_method(name='capture', http_verb='post')
class Charge(CreatableResource, RetrievableResource, ListableResource):
    
    path = 'charges'
