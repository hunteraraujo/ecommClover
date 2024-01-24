#!/usr/bin/env python3
"""Order"""

from clover.abstract import (
    CreatableResource,
    RetrievableResource,
    ListableResource,
    ModifiableResource,
    add_resource_method
)

@add_resource_method(name='pay', http_verb='post')
@add_resource_method(name='return_order', http_verb='post', http_path='returns')
class Order(CreatableResource, RetrievableResource, ListableResource, ModifiableResource):
    
    path = 'orders'
