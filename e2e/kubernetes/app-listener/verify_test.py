# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Ensure listener E2E cannot skip missing or unexpected app Services."""

import unittest

from verify import check_app_service_count


class AppServiceCountTest(unittest.TestCase):
    def test_missing_dedicated_service_fails(self):
        with self.assertRaisesRegex(AssertionError, "expected 1"):
            check_app_service_count([], "dedicated")

    def test_duplicate_dedicated_services_fail(self):
        with self.assertRaisesRegex(AssertionError, "found 2"):
            check_app_service_count([{}, {}], "dedicated")

    def test_shared_topology_rejects_app_services(self):
        with self.assertRaisesRegex(AssertionError, "expected 0"):
            check_app_service_count([{}], "shared")

    def test_expected_topologies_pass(self):
        check_app_service_count([{}], "dedicated")
        check_app_service_count([], "shared")


if __name__ == "__main__":
    unittest.main()
