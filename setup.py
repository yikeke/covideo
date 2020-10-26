#!/usr/bin/env python
# coding: utf-8

import setuptools

setuptools.setup(
    name='covideo',
    version='0.0.4',
    author='yikeke',
    author_email='yikeke@pingcap.com',
    url='https://github.com/yikeke/covideo',
    description='Easily clip and merge MP4 videos',
    long_description="Easily clip and merge MP4 videos",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    keywords='video-clipping',
    install_requires=[],
    # folder/file names can not contain "-"
    entry_points={
        'console_scripts': [
            'covideo=covideo:exe_main'
        ],
    }
)