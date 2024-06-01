from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in vppl_customization/__init__.py
from vppl_customization import __version__ as version

setup(
	name="vppl_customization",
	version=version,
	description="Get All your Doctype Customizations in this app only",
	author="Abhishek Chougule",
	author_email="chouguleabhis@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
