# setup.py

from setuptools import setup, find_packages

setup(
    name='the-forest-palette',
    version='0.1.0',
    author="Beth O'Dwyer",
    author_email='odwyerbeth621@gmail.com',
    description='A package for custom matplotlib color palettes',
    packages=find_packages(),
    install_requires=[
        'matplotlib>=3.0.0'
    ],
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
