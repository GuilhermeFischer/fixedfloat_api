from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.2'
DESCRIPTION = 'FixedFloat API'
LONG_DESCRIPTION = 'The FixedFloat API allows you to automate the receipt of \
    information about the exchange rates of currencies, created orders, \
    presented on the FixedFloat service, create orders and manage them using it'

# Setting up
setup(
    name="fixedfloat_api",
    version=VERSION,
    author="Guilherme A. Fischer",
    author_email="<gfx.fischer@gmail.com>",
    url="https://github.com/GuilhermeFischer/fixedfloat_api",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['api', 'crypto', 'exchange', 'fixedfloat', 'bitcoin', 'ethereum'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License"
    ]
)