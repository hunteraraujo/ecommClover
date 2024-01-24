#!/usr/bin/env python3
"""Utility functions.

Random functions that are used commonly.
"""
import json
import clover

def json_ps(dict_obj):
    """
    Converts a dictionary object to a pretty JSON string.
    """
    pretty_dict = json.dumps(dict_obj, indent=4, sort_keys=True)
    return pretty_dict

def json_pp(dict_obj):
    """Pretty prints dictionary object.

    Args:
        dict_obj (dict): Any dictionary object.
    """
    print(json_ps(dict_obj))

def remove_all_none_values(dictionary):
    """Removes all None value keys."""
    filtered = {
        key: val for key, val in dictionary.items() if val is not None
    }
    dictionary.clear()
    dictionary.update(filtered)

def set_api_endpoint(url):
    """Sets the package wide base url."""
    clover.base_url = url

def set_tokenization_api_endpoint(url):
    """Sets the package wide tokenization base url."""
    clover.tokenization_base_url = url

def set_public_access_key_endpoint(url):
    """Sets the package wide public access key base url."""
    clover.base_url = url

def set_credentials_from_public_access_key():
    """Sets package wide api key, merchant UUID, and developer app UUID."""
    
    credentials = clover.PublicAccessKey.retrieve()

    clover.api_key = credentials['apiAccessKey']
    clover.merchant_uuid = ['merchantUuid']
    clover.developer_app_uuid = ['developerAppUuid']
