"""
setup.py
"""

from setuptools import setup

with open("README.md", "r") as md:
  long_description = md.read()


setup(
  name="pynab-client-pc",
  packages=["pynabapipc", "pynabapipc.model"],
  version="0.2",
  license="GNU GPLv3",
  url="https://github.com/irunasroot/pynab-client-pc",
  download_url="https://github.com/irunasroot/pynab-client/archive/v0.2.tar.gz",
  keywords=["ynab", "pynab", "budgeting", "budgets", "youneedabudget"],
  install_requires=[
          "requests"
  ],
  classifiers=[
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Build Tools",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Programming Language :: Python :: 3.6",
  ]
)
