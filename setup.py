from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in erpdemo/__init__.py
from erpdemo import __version__ as version

setup(
	name="erpdemo",
	version=version,
	description="“Integrate for a better tomorrow- SAS ERP”",
	author="SAS Technologies Co. W.L.L",
	author_email="erp@sastechnologies.co",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
