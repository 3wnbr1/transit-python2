#!/usr/bin/env python

## Copyright 2014 Cognitect. All Rights Reserved.
##
## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
##
##      http://www.apache.org/licenses/LICENSE-2.0
##
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS-IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.


from pathlib import Path
from setuptools import setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="transit-python2",
    version="0.8.321",
    description="Transit marshalling for Python",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Cognitect, 3wnbr1",
    url="https://github.com/3wnbr1/transit-python2",
    packages=["transit"],
    install_requires=["python-dateutil", "msgpack-python"],
)
