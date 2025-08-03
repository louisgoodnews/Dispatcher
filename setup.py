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
    url="https://github.com/louisgoodnews/dispatcher",  # Optional: falls du ein Repo hast
    packages=find_packages(),  # Oder ['.'] wenn du keinen Ordner hast
    py_modules=["dispatcher"],  # Da dein Modul aktuell in einer einzelnen Datei liegt
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Optional: Wenn du eine Lizenz hast
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
