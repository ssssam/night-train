# Copyright 2017 Codethink Ltd.
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

'''Test cases for Night Train task descriptions.'''

import nighttrain


def test_simple():
    '''Basic test of task list parser.'''

    tasklist = nighttrain.tasks.TaskList('''
    tasks:
    - name: print-hello
      commands: echo "hello"
    ''')

    assert tasklist.names() == ['print-hello']


def test_no_tasks_header():
    '''The task list is allowed to just be a list.'''

    tasklist = nighttrain.tasks.TaskList('''
    - name: print-hello
      commands: echo "hello"
    ''')

    assert tasklist.names() == ['print-hello']
