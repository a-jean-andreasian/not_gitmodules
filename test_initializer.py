import unittest
from unittest.mock import patch, mock_open, call
import subprocess
from not_gitmodules import initializer
from not_gitmodules.cli import cli

module_for_test = "https://github.com/not-gitmodules/notgitmodules-file-manager-py"


class TestInitializerFunction(unittest.TestCase):
    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data=f"file_manager: {module_for_test}",
    )
    @patch("not_gitmodules.core.read_yaml")
    def test_initializer_with_valid_yaml(self, mock_read_yaml, mock_file):
        mock_read_yaml.return_value = {
            "file_manager": f"{module_for_test}",
        }

        initializer("notgitmodules.yaml")
        mock_read_yaml.assert_called_once_with("notgitmodules.yaml")

    @patch("builtins.open", new_callable=mock_open, read_data="file_manager: invalid_repo")
    @patch("not_gitmodules.core.read_yaml")
    @patch("builtins.print")
    @patch("subprocess.run")
    def test_initializer_with_invalid_yaml(self, mock_subprocess, mock_print, mock_read_yaml, mock_file):
        mock_read_yaml.return_value = {"file_manager": "invalid_repo"}

        mock_subprocess.side_effect = subprocess.CalledProcessError(
            returncode=1, cmd="git clone", stderr="error"
        )

        initializer("notgitmodules.yaml")

        expected_calls = [
            call("Directory 'my_gitmodules/file_manager' already exists. Skipping..."),
            call("Failed to clone invalid_repo: error"),
        ]

        self.assertTrue(any(call in mock_print.mock_calls for call in expected_calls))

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data=f"file_manager: {module_for_test}",
    )
    @patch("not_gitmodules.core.read_yaml")
    def test_cli_with_default_input(self, mock_read_yaml, mock_file):
        with patch("builtins.input", return_value=""):
            cli()

        mock_read_yaml.assert_called_once_with("notgitmodules.yaml")


if __name__ == "__main__":
    unittest.main()
