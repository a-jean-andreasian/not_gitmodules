import unittest
from unittest.mock import patch, mock_open
from not_gitmodules import initializer
from not_gitmodules.cli import cli


class TestInitializerFunction(unittest.TestCase):
    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="repos:\n  file_reader: https://github.com/Free-Apps-for-All/file_manager_git_module",
    )
    @patch("not_gitmodules.core.read_yaml")
    def test_initializer_with_valid_yaml(self, mock_read_yaml, mock_file):
        mock_read_yaml.return_value = {
            "repos": {
                "file_reader": "https://github.com/Free-Apps-for-All/file_manager_git_module"
            }
        }

        initializer("notgitmodules.yaml")

        mock_read_yaml.assert_called_once_with("notgitmodules.yaml")

    @patch("builtins.open", new_callable=mock_open, read_data="repos:\n  invalid_repo")
    def test_initializer_with_invalid_yaml(self, mock_file):
        with self.assertRaises(FileNotFoundError):
            initializer("notgitmodules.yaml")

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="repos:\n  file_reader: https://github.com/Free-Apps-for-All/file_manager_git_module",
    )
    @patch("not_gitmodules.core.read_yaml")
    def test_cli_with_default_input(self, mock_read_yaml, mock_file):
        with patch("builtins.input", return_value=""):
            cli()

        mock_read_yaml.assert_called_once_with("notgitmodules.yaml")


if __name__ == "__main__":
    unittest.main()
