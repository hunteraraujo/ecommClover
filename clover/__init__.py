# Needed for authentication and authorization.
access_token = None
api_key = None


merchant_uuid = None
developer_app_uuid = None
mid = None

# Endpoints
# base_url = 'https://scl.clover.com'
# tokenization_base_url = 'https://token.clover.com'

# To test api in Sandbox environment, below should be updated to point to Sandbox
#Sandbox endpoints
base_url = 'https://scl-sandbox.dev.clover.com'
tokenization_base_url = 'https://token-sandbox.dev.clover.com'

# Imports
from .http_client import HTTPClient
from .base_requestor import BaseRequestor
from .resources.token import Token
from .resources.charge import Charge
from .resources.customer import Customer
from .resources.refund import Refund
from .resources.order import Order
from .resources.public_access_key_management_service import PublicAccessKey
from .utils import (
    set_api_endpoint,
    set_tokenization_api_endpoint,
    set_public_access_key_endpoint
)
