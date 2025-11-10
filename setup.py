#!/usr/bin/env python3
"""
Privvy Language Setup
Install with: pip install -e .
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
long_description = (Path(__file__).parent / "README.md").read_text()

setup(
    name="privvy-lang",
    version="1.0.0",
    description="The Easiest Backend Programming Language with Built-in ORM",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Privvy Team",
    author_email="hello@privvy.dev",
    url="https://github.com/yourname/privvy",
    license="MIT",
    
    # Package data
    py_modules=[
        "privvy",
        "lexer",
        "parser",
        "interpreter",
        "ast_nodes",
        "token_types",
    ],
    
    # Include CLI script
    scripts=["privvy-cli.py", "privvy-db.py"],
    
    # Entry points for command-line tools
    entry_points={
        "console_scripts": [
            "privvy=privvy-cli:main",
            "privvy-db=privvy-db:main",
        ],
    },
    
    # Dependencies
    install_requires=[
        "psycopg2-binary>=2.9.0",  # PostgreSQL support
    ],
    
    # Metadata
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Interpreters",
        "Topic :: Database",
        "Topic :: Internet :: WWW/HTTP",
    ],
    
    keywords="programming-language backend orm database postgresql sqlite beginner-friendly",
    
    python_requires=">=3.7",
    
    # Project URLs
    project_urls={
        "Documentation": "https://github.com/yourname/privvy/blob/main/README.md",
        "Source": "https://github.com/yourname/privvy",
        "Bug Reports": "https://github.com/yourname/privvy/issues",
    },
)

