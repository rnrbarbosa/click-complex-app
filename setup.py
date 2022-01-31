from setuptools import setup
from setuptools import find_namespace_packages

setup(
    name="click-example-complex",
    version="1.0",
    packages= find_namespace_packages(include=['*']),
    include_package_data=True,
    #install_requires=["click"],
    entry_points="""
        [console_scripts]
        complex=complex.cli:cli
    """,
)