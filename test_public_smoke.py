"""Integrity tests for the public-repo diagnostic evidence (offline, stdlib)."""
import json
import os
import unittest

ROOT = os.path.dirname(os.path.abspath(__file__))


class PublicSmokeTests(unittest.TestCase):
    def test_public_run_succeeded(self):
        data = json.load(open(os.path.join(ROOT, "run-34869320641-jobs.json"), encoding="utf-8"))
        self.assertEqual(data["status"], "completed")
        self.assertEqual(data["conclusion"], "success")

    def test_public_job_executed_all_steps(self):
        data = json.load(open(os.path.join(ROOT, "run-34869320641-jobs.json"), encoding="utf-8"))
        j = data["jobs"][0]
        self.assertEqual(j["conclusion"], "success")
        self.assertEqual(len(j["steps"]), 5)
        names = [s["name"] for s in j["steps"]]
        self.assertIn("Upload smoke receipt", names)

    def test_deletion_attempt_recorded(self):
        data = json.load(open(os.path.join(ROOT, "deletion-confirmation.json"), encoding="utf-8"))
        self.assertIn("delete_repo", data["result"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
