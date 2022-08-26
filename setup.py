import os.path
from setuptools import setup

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

# This call to setup() does all the work
setup(
    name="tocgen",
    version="1.0.0",
    description="Dynamically creates table of content for freeCodeCamp articles in markdown format",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/fhsinchy/tocgen",
    author="Article Table of Content Generator",
    author_email="shovik.is.here@gmail.com",
    license="GPL-3.0",
    classifiers=[
        "License :: OSI Approved :: GPL-3.0 License",
        "Programming Language :: Python :: 3",
    ],
    py_modules=["tocgen"],
    entry_points={"console_scripts": ["tocgen=tocgen:main"]},
)