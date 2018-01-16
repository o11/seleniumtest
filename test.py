import unittest
from selenium_github import Github


class TestGithub(unittest.TestCase):
    def setUp(self):
        self.github = Github(username='o11', password='')

    def test_login(self):
        self.github.login()

    def test_get_repositories(self):
        self.assertEqual(len(self.github.get_repositories()), 47)

    def test_get_stars(self):
        self.assertEqual(len(self.github.get_stars()), 387)

    def test_set_username(self):
        self.github.username = 'torvalds'
        self.assertEqual(self.github.username, 'torvalds')
        self.assertEqual(len(self.github.get_stars()), 2)
        self.assertEqual(len(self.github.get_repositories()), 5)


if __name__ == '__main__':
    unittest.main()
