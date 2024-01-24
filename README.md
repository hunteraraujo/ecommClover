# Clover E-Commerce Python SDK

The Clover E-Commerce Python SDK provides convenient access to the E-Commerce API from applications written in server-side Python.

## Prerequisites

Before you can use the SDK, you need the following:

* A Clover [sandbox developer account](https://sandbox.dev.clover.com/developers)
* A sandbox application which requests the needed [E-Commerce app permissions](https://docs.clover.com/clover-platform/docs/e-commerce-app-permissions)
* A sandbox [test merchant](https://docs.clover.com/clover-platform/docs/working-with-test-merchants) which has your test app installed
* A Python virtual environment

## Installing the SDK

To install the SDK on your machine, complete the following steps.

1. Clone the repository by running the following command.

```bash
git clone git@github.com:clover/ecomm-SDK-python.git
```
2. Navigate to the current folder.
```bash
cd ecomm-SDK-python
```

3. Install the package locally (this uses the `setup.py` in the package directory).

```bash
pip3 install .
```

**Note**

If you're developing on this package, you'll want to symlink the installation so changes show up right away.

```bash
pip3 install -e .
```

4. To test that your installation works, change to your home directory and start the Python3 interpreter.

```bash
cd ~
python3
```

With the Python Interpeter running, type `import clover` and press **Enter**.

```python
Python 3.7.2 (default, Jan 14 2019, 17:53:34)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import clover
>>>
```

If it was installed correctly, nothing will happen.

If the installation failed, you will see a `ModuleNotFoundError`:

```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'clover'
```

## Running Tests

To run all the unit tests, run the following command in the `clover` package directory (`~/src/ecomm-SDK-python/clover`).

```bash
python3 setup.py test
```

If you run these tests frequently, you can create an alias for the command in your `.bashrc` or `.bash_profile`.

```bash
alias py3test='python3 setup.py test'
```

# Usage

The library needs to be configured with your public key retrieved from the PAKMS service (`clover.api_key`).
You also need to set your test merchant's OAuth/API token (`clover.access_token`).

Add the following identifiers and update them with the values for your app.

```python
clover.access_token = "Bkk321..."
clover.api_key = "fhjk1..."
```

# Examples

The following examples show basic usage of the SDK. For complete information about the E-Commerce API and its purpose, see the [Clover Developer Docs](https://docs.clover.com).

## Tokens

### Tokenizing a Card

```python
import clover

token = clover.Token.create(
    card={
        'number': '4111111111111111',
        'brand': 'VISA',
        'exp_month': '12',
        'exp_year': '2030',
        'cvv': '123',
    }
)
```

The returned token object will look similar to the following:

```python
>>> token
{
    'card' : {
        'exp_year' : '2030',
        'exp_month' : '12',
        'last4' : '1111',
        'brand' : 'VISA'
    },
    'object' : 'token',
    'id' : 'clv_1TSTSaGjnPmHdfHjBCMr7VtB'
}
```

## Charges

### Making a Charge

```python
import clover
clover.access_token = 'DF762CF60AFDA86C14A1A20BDAEA3F43'

charge = clover.Charge.create(
    amount='999',
    currency='usd',
    description='Example charge',
    source='clv_1TSTSaGjnPmHdfHjBCMr7VtB',
)
```

The returned charge object will look similar to the following:

```python
>>> charge
{
    'amount': 999,
    'capture': false,
    'created': 1563308683701,
    'currency': 'usd',
    'description': 'Example charge',
    'id': '5X28Y5HMHYKAC',
    'outcome': {
        'network_status': 'approved_by_network',
        'type': 'authorized'
    },
    'paid': true,
    'refunded': false,
    'source': {
        'cvc_check': 'unavailable',
        'object': 'clv_1TSTSaGjnPmHdfHjBCMr7VtB'
    },
    'status': 'succeeded'
}
```

## Uninstalling the SDK

If you want to uninstall the package, run the following command:

```bash
pip3 uninstall clover
```

When you are asked to confirm, type `y` and press **Enter**.

```bash
Uninstalling clover-0.1:
  Would remove:
    /usr/local/lib/python3.7/site-packages/clover-0.1.dist-info/*
    /usr/local/lib/python3.7/site-packages/clover/*
Proceed (y/n)? y
```
