from setuptools import setup, find_packages
from pathlib import Path

VERSION = "0.1.0"
DESCRIPTION = "Helper tool for building Visibility Allocation Systems"


# read the contents of README file
this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory / "README.md").read_text()

setup(
    name="vas",
    version=VERSION,
    author="Kshitijaa Jaglan",
    author_email="kjaglan@ifi.uzh.ch",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/deutranium/vas",
    packages=find_packages(),
    install_requires=[],
    keywords=["vas", "visibility allocation systems"],
    classifiers=[],
    license="Apache License 2.0",
)
