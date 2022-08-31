#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
	name="Gb Subdomain Scanner",
	description="Gb Subdomain scanner is a python tool designed to quickly enumerate subdomains on a target domain through dictionary attack.",
	url="https://github.com/GbolahanAnon/Gb-subdomain-scanner.git",
	author="GbolahanAnon",
	license="MIT",
	packages=["gbscanner"],
	package_data={
		"gbscanner": [
			"wordlist.txt",
			"config.json",
			], 
	},
	include_package_data=True,
	install_requires = [
			"requests",
			"beautifulsoup4",
			"colorama",
			],
	python_requires=">=3.6",
	entry_points={
		'console_scripts': [
			'gbscanner=gbscanner.gbscanner:main',
		],
	}
)
