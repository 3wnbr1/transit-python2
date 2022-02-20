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

import json
import time
from io import StringIO

from transit.reader import JsonUnmarshaler


def run_tests(data):
    datas = StringIO(str(data))
    t = time.time()
    JsonUnmarshaler().load(datas)
    et = time.time()
    datas = StringIO(str(data))
    tt = time.time()
    json.load(datas)
    ett = time.time()
    read_delta = (et - t) * 1000.0
    print(f"Done: {read_delta}  --  raw JSON in: {(ett - tt) * 1000.0}")
    return read_delta


seattle_dir = "transit-format/examples/0.8/"
means = {}
for jsonfile in [seattle_dir + "example.json", seattle_dir + "example.verbose.json"]:
    data = ""
    with open(jsonfile, "r") as fd:
        data = fd.read()

    print(f"{'-' * 50} Running {jsonfile} {'-' * 50}")

    runs = 200
    deltas = [run_tests(data) for x in range(runs)]
    means[jsonfile] = sum(deltas) / runs

for jsonfile, mean in means.items():
    print(f"Mean for {jsonfile}: {mean}")
