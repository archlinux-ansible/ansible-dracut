from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = """
  filter: find_unmanaged_resources
  author: Alex Wicks <alex@awicks.io>
  short_description: Return currently active display manager
  description:
    - This filter will construct a command using find from coreutils, to remove non-ansible managed resources.
    - The input list will be ignored.
"""
from ansible import errors

class FilterModule(object):
    def filters(self):
        return {
            "find_unmanaged_resources": self.find_unmanaged_resources,
        }

    def add_suffix_and_prefix(self, _index: str):
        return "-not -name '{}'".format(_index)

    def find_unmanaged_resources(self, directory, ignored):
        if not isinstance(ignored, list):
            raise errors.AnsibleFilterError("Expected list")
        return "find {} -type f {} -delete -print".format(
            directory,
            " ".join(list(map(
                self.add_suffix_and_prefix,
                ignored,
            ))),
        )
