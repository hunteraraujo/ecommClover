RETRIEVE_PUBLIC_ACCESS_KEY = {
    "apiAccessKey": "309f30e7fbacd10d6af9f7a38fce5b16",
    "merchantUuid": "CVSWF4EE5DP81",
    "developerAppUuid": "1HXD300CFCJ8C",
    "active": True,
    "createdTime": 1565729754000,
    "modifiedTime": 1565729754000
}

CREATE_TOKEN = {
    "id": "clv_1TSTS89P1vANcEi3DXaQEck7",
    "object": "token",
    "card": {
        "exp_month": "12",
        "exp_year": "2030",
        "last4": "1111",
        "brand": "VISA"
    }
}

RETRIEVE_TOKEN = {
    "card": {
        "brand": "VISA",
        "created_time": 2019,
        "encrypted_pan": "NJUWmTC+uBz4KDPMwHDw0NFvDrv8bj8EZ7Jl3u6KAW0=",
        "exp_month": "12",
        "exp_year": "2030",
        "first6": "411111",
        "id": "E46M2RK9B00JJ",
        "last4": "1111",
        "modified_time": 2019
    },
    "cloverToken": {
        "createdTime": 2019,
        "developerUuid": "mockdeveloper",
        "lastAccessedTime": 0,
        "merchantUuid": "mockmerchant",
        "tokenValue": "clv_1TSTS89P1vANcEi3DXaQEck7"
    },
    "tokenMeta": {
        "createdTime": 2019,
        "modifiedTime": 2019,
        "paymentInstrument": "CARD",
        "tokenProvider": "MOCK",
        "tokenStatus": "NEW"
    }
}

AFTER_MODIFY_RETRIEVE_TOKEN = {
    "card": {
        "brand": "VISA",
        "created_time": 2019,
        "encrypted_pan": "NJUWmTC+uBz4KDPMwHDw0NFvDrv8bj8EZ7Jl3u6KAW0=",
        "exp_month": "12",
        "exp_year": "2030",
        "first6": "411111",
        "id": "E46M2RK9B00JJ",
        "last4": "1111",
        "modified_time": 2019
    },
    "cloverToken": {
        "createdTime": 2019,
        "developerUuid": "mockdeveloper",
        "lastAccessedTime": 2019,
        "merchantUuid": "mockmerchant",
        "tokenValue": "clv_1TSTS89P1vANcEi3DXaQEck7"
    },
    "tokenMeta": {
        "createdTime": 2019,
        "modifiedTime": 2019,
        "paymentInstrument": "CARD",
        "tokenProvider": "MOCK",
        "tokenStatus": "NEW",
        "tokenType": "RECURRING"
    }
}

CREATE_CHARGE = {
    "amount": 999,
    "capture": False,
    "created": 1563825782866,
    "currency": "usd",
    "description": "Example charge",
    "id": "KW5VKX3GG90CP",
    "outcome": {
        "network_status": "approved_by_network",
        "type": "authorized"
    },
    "paid": True,
    "refunded": False,
    "source": {
        "cvc_check": "unavailable",
        "object": "clv_1TSTSutExahSCcYgnh9z7Yct"
    },
    "status": "succeeded"
}

RETRIEVE_CHARGE = {
    "amount": 999,
    "created": 1563830252722,
    "description": "Example charge",
    "id": "KW5VKX3GG90CP",
    "order": "ZCXV7QA1SSZZM",
    "outcome": {
        "network_status": "approved_by_network",
        "risk_level": "normal",
        "risk_score": 10,
        "type": "authorized"
    },
    "paid": True,
    "refunded": False,
    "source": {},
    "status": "succeeded"
}

LIST_CHARGE = {
    "data": {
        "elements": [
            {
                "amount": 999,
                "created": 1563830334562,
                "description": "Example charge",
                "id": "1RZE6CCMHSENA",
                "order": "3XVF6TWSH1XAJ",
                "outcome": {
                    "network_status": "approved_by_network",
                    "risk_level": "normal",
                    "risk_score": 10,
                    "type": "authorized"
                },
                "paid": True,
                "refunded": False,
                "source": {},
                "status": "succeeded"
            },
            {
                "amount": 999,
                "created": 1563830334581,
                "description": "Example charge",
                "id": "SGZ5C90AD8B7M",
                "order": "P91V2TDV06FJY",
                "outcome": {
                    "network_status": "approved_by_network",
                    "risk_level": "normal",
                    "risk_score": 10,
                    "type": "authorized"
                },
                "paid": True,
                "refunded": False,
                "source": {},
                "status": "succeeded"
            },
            {
                "amount": 999,
                "created": 1563830334620,
                "description": "Example charge",
                "id": "VMD7MFZ5PZYE0",
                "order": "NMW0YMGFQ3CNT",
                "outcome": {
                    "network_status": "approved_by_network",
                    "risk_level": "normal",
                    "risk_score": 10,
                    "type": "authorized"
                },
                "paid": True,
                "refunded": False,
                "source": {},
                "status": "succeeded"
            }
        ]
    },
    "has_more": True,
    "object": "list",
    "url": "/v1/charges"
}

CREATE_CUSTOMER = {
    "id": "XR01MDZ9ZB9QG",
    "object": "customer",
    "created": 1564410985777,
    "currency": "usd",
    "email": "test@clover.com",
    "sources": {
        "object": "list",
        "data": {
            "elements": [
                "MB33YF9F4RGS2"
            ]
        },
        "has_more": False
    },
    "shipping": {
        "name": "null null"
    }
}

MODIFY_CUSTOMER = {
    "id": "XR01MDZ9ZB9QG",
    "object": "customer",
    "created": 1564411087340,
    "currency": "usd",
    "email": "test@clover.com",
    "firstName": "clover",
    "lastName": "test",
    "sources": {
        "object": "list",
        "data": {
            "elements": [
                "MB33YF9F4RGS2"
            ]
        },
        "has_more": False
    }
}

DELETE_SOURCE_CUSTOMER = {
    "deleted": True,
    "id": "MB33YF9F4RGS2",
    "object": "deletedcard"
}

CREATE_REFUND = {
    "amount": 999,
    "capture": False,
    "created": 1563825782866,
    "currency": "usd",
    "description": "Example charge",
    "id": "KW5VKX3GG90CP",
    "outcome": {
        "network_status": "approved_by_network",
        "type": "authorized"
    },
    "paid": True,
    "refunded": False,
    "source": {
        "cvc_check": "unavailable",
        "object": "clv_1TSTSutExahSCcYgnh9z7Yct"
    },
    "status": "succeeded"
}

RETRIEVE_REFUND = {
    "amount": 999,
    "created": 1563830252722,
    "description": "Example charge",
    "id": "KW5VKX3GG90CP",
    "order": "ZCXV7QA1SSZZM",
    "outcome": {
        "network_status": "approved_by_network",
        "risk_level": "normal",
        "risk_score": 10,
        "type": "authorized"
    },
    "paid": True,
    "refunded": False,
    "source": {},
    "status": "succeeded"
}

LIST_REFUND = {
    "data": {
        "elements": [
            {
                "amount": 999,
                "created": 1563830334562,
                "description": "Example charge",
                "id": "1RZE6CCMHSENA",
                "order": "3XVF6TWSH1XAJ",
                "outcome": {
                    "network_status": "approved_by_network",
                    "risk_level": "normal",
                    "risk_score": 10,
                    "type": "authorized"
                },
                "paid": True,
                "refunded": False,
                "source": {},
                "status": "succeeded"
            },
            {
                "amount": 999,
                "created": 1563830334581,
                "description": "Example charge",
                "id": "SGZ5C90AD8B7M",
                "order": "P91V2TDV06FJY",
                "outcome": {
                    "network_status": "approved_by_network",
                    "risk_level": "normal",
                    "risk_score": 10,
                    "type": "authorized"
                },
                "paid": True,
                "refunded": False,
                "source": {},
                "status": "succeeded"
            },
            {
                "amount": 999,
                "created": 1563830334620,
                "description": "Example charge",
                "id": "VMD7MFZ5PZYE0",
                "order": "NMW0YMGFQ3CNT",
                "outcome": {
                    "network_status": "approved_by_network",
                    "risk_level": "normal",
                    "risk_score": 10,
                    "type": "authorized"
                },
                "paid": True,
                "refunded": False,
                "source": {},
                "status": "succeeded"
            }
        ]
    },
    "has_more": True,
    "object": "list",
    "url": "/v1/charges"
}

CREATE_ORDER = {
    "id": "4CEQ3THZJPXJA",
    "amount": 0,
    "amount_returned": 0,
    "currency": "usd",
    "created": 1565030627000,
    "items": {
        "elements": [
            {
                "parent": "string",
                "quantity": 1,
                "amount": 100,
                "currency": "string",
                "description": "string"
            }
        ]
    },
    "status": "created"
}

RETRIEVE_ORDER = {
    "id": "4CEQ3THZJPXJA",
    "amount": 0,
    "currency": "USD"
}

LIST_ORDER = {
    "object": "list",
    "url": "/v1/orders",
    "has_more": True,
    "data": {
        "elements": [
            {
                "id": "4CEQ3THZJPXJA",
                "amount": 0,
                "currency": "USD"
            },
            {
                "id": "F1ZZP6VK7NPSA",
                "currency": "USD",
                "charge": "2XAP0F7K5EVJT"
            },
            {
                "id": "59EQ70BSV53D0",
                "currency": "USD",
                "charge": "6E327M9S7JSFE"
            }
        ]
    }
}

MODIFY_ORDER = {}

PAY_ORDER = {}

CAPTURE_ORDER = {}

RETURN_ORDER = {}
