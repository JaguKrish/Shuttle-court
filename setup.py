# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in shuttle_court/__init__.py
from shuttle_court import __version__ as version

setup(
	name="shuttle_court",
	version=version,
	description="my first custom app  sports",
	author="Jagadesh ",
	author_email="jaga639@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
