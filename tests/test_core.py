"""Tests for core module."""

from agent2.core import greet


def test_greet_default():
    assert greet() == "Hello, world! Ready to refactor."


def test_greet_custom():
    assert greet("Claude") == "Hello, Claude! Ready to refactor."
