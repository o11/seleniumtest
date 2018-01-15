import unittest
from selenium_github import Github


class TestGithub(unittest.TestCase):
    def setUp(self):
        self.github = Github(username='o11', password='')
        self.github.login()

    def test_get_repositories(self):
        self.assertEqual(len(self.github.get_stars()), 386)
        self.assertEqual(len(self.github.get_repositories()), 46)

    def tearDown(self):
        self.github.__del__()
