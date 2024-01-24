#!/usr/bin/env python3
"""Customer"""

from clover.abstract import (
    CreatableResource,
    ModifiableResource
)


class Customer(CreatableResource, ModifiableResource):

    path = 'customers'

    @classmethod
    def delete_source(cls, customer_id, source_id):
        """Deletes a payment method from a customer."""

        return cls.request(
            method='delete',
            path=[customer_id, 'sources', source_id]
        )
