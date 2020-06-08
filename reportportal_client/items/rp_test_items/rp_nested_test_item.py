"""
This module contains functional for Nested RP test items management.
Copyright (c) 2018 http://reportportal.io .
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from reportportal_client.items.rp_test_items.rp_child_test_item import RPChildTestItem


class NestedItem(RPChildTestItem):

    """This model stores attributes for RP nested test items."""

    def __init__(self, rp_url, session, api_version, project_name, parent_item, item_name, item_type, launch_uuid,
                 description=None, attributes=None, uuid=None, code_ref=None, parameters=None, unique_id=None,
                 retry=False):
        """
        Initialize instance attributes.

        :param rp_url:          report portal url
        :param session:         Session object
        :param api_version:     RP API version
        :param project_name:    RP project name
        :param item_name:       RP item name
        :param item_type:       Type of the test item. Allowable values: "suite",
                                "story", "test", "scenario", "step",
                                "before_class", "before_groups", "before_method",
                                "before_suite", "before_test", "after_class",
                                "after_groups", "after_method", "after_suite",
                                "after_test"
        :param launch_uuid:     Parent launch UUID
        :param description:     Test item description
        :param attributes:      Test item attributes
        :param uuid:            Test item UUID (auto generated)
        :param code_ref:        Physical location of the test item
        :param parameters:      Set of parameters (for parametrized test items)
        :param unique_id:       Test item ID (auto generated)
        :param retry:           Used to report retry of the test. Allowable values:
                                "True" or "False"
        """
        super(NestedItem, self).__init__(rp_url, session, api_version, project_name, parent_item, item_name, item_type,
                                         launch_uuid, description, attributes, uuid, code_ref, parameters, unique_id,
                                         retry)
        self.has_stats = False
