#!/usr/bin/env python
from setuptools import setup

setup(
    name="drf-mongo-filters",
    packages=["drf_mongo_filters",],
    version="1.1",
    install_requires=["Django == 1.8",
                      "mongoengine >= 0.10",
                      "djangorestframework >= 3.0",
                      "mock == 1.0.1",
                      "qualname == 0.1.0"],
    # metadata for upload to PyPI
    author="Maxim Vasiliev",
    author_email="qwiglydee@gmail.com",
    description="Filtering support for Django Rest Framework Mongoengine.",
    keywords=["mongoengine", "django rest framework", "filtering"],
    url="https://github.com/dschoeni/drf-mongo-filters",
    download_url="https://github.com/dschoeni/drf-mongo-filters/releases",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2.7 :: Only",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
