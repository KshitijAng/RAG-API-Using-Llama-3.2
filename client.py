
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import requests
import sys

if len(sys.argv) < 3 or sys.argv[1] != "--query":
    print("Usage: python client.py --query \"Your question here\"")
    sys.exit(1)

# Get the query from the command-line arguments
query = sys.argv[2]

response = requests.post("http://127.0.0.1:8080/predict", json={"input": query})
# print(f"Status: {response.status_code}\nResponse:\n {response.text}")
print(response.text)
