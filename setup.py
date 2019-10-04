from setuptools import setup, find_packages

setup(
    name='hello_cpp',
    version='1.0.0',
    packages=find_packages(),
    package_data={
        '':['*.dylib']
    },
    include_package_data=True,
    install_requires=[],
)

