#!/usr/bin/env python3
"""
Clover ECOMM Python SDK Package
"""
import setuptools

setuptools.setup(
    name='ecommClover',
    version='1.0.0',
    description="Python SDK for Clover's E-Commerce APIs.",
    url='https://github.com/clover/ecomm-SDK-python',
    author='Clover',
    author_email='support@clover.com, deepali.mittal@clover.com',
    license='MIT',
    keywords="clover api payments",
    packages=setuptools.find_packages(),
    install_requires=[
    'requests',
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    zip_safe=False,
    python_requires=">=3.0",  # Corrected line
    project_urls={
        "Bug Tracker": "https://github.com/clover/ecomm-SDK-python/issues",
        "Documentation": "https://docs.clover.com",
        "Source Code": "https://github.com/clover/ecomm-SDK-python",
    }
)
