"""
Author: Louis Goodnews
Date: 2025-08-03
"""

from setuptools import setup, find_packages

setup(
    name="dispatcher",
    version="0.1.0",
    author="Louis Goodnews",
    description="A modular event dispatching system with builder and notification pattern.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/louisgoodnews/dispatcher",
    packages=find_packages(),
    py_modules=["dispatcher"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
