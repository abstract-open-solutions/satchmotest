from setuptools import setup, find_packages
import os


version = '0.1'


setup(
    name='satchmotest',
    version=version,
    description="Satchmo test package",
    long_description=open("README.rst").read() + "\n" +
                     open(os.path.join("docs", "HISTORY.rst")).read(),
    # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Programming Language :: Python",
    ],
    keywords='',
    author='Simone Deponti',
    author_email='simone.deponti@abstract.it',
    url='http://abstract-open-solutions.github.com/satchmotest/',
    license='BSD',
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Django',
        'Satchmo'
    ]
)
