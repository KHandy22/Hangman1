import pytest
import random
from io import StringIO
from unittest import mock

def test_task1_correct_guess(monkeypatch):
    # Mock random.choice to always pick "camel"
    monkeypatch.setattr(random, "choice", lambda x: "camel")
    with mock.patch("builtins.input", return_value="c"):
        with mock.patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            import task1  # Import the task1 starter code
            output = mock_stdout.getvalue().strip().split("\n")
            assert output[0] == "camel"  # Check chosen word
            assert output[1] == "c"      # Check lowercase conversion
            assert output[2] == "right"  # Check correct guess

def test_task1_incorrect_guess(monkeypatch):
    # Mock random.choice to always pick "camel"
    monkeypatch.setattr(random, "choice", lambda x: "camel")
    with mock.patch("builtins.input", return_value="x"):
        with mock.patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            import task1  # Import the task1 starter code
            output = mock_stdout.getvalue().strip().split("\n")
            assert output[0] == "camel"  # Check chosen word
            assert output[1] == "x"      # Check lowercase conversion
            assert output[2] == "wrong"  # Check incorrect guess
