"""
Integration tests for pyyamlconfig
"""
import unittest
# pylint: disable=import-error
from pyyamlconfig import (
    load_config,
    PyYAMLConfigError,
)


class TestLoadConfig(unittest.TestCase):
    """
    Tests for pyyamlconfig.load_config
    """
    def test_loads_config(self):
        """
        Tests that config can be loaded
        """
        config = load_config('config.yaml')
        self.assertEqual(
            config,
            {'mykey': 'myvalue'},
        )

    def test_raises_file_not_found(self):
        """
        Test that it raises if file is not found
        """
        with self.assertRaises(PyYAMLConfigError) as err:
            load_config('myconfig.yaml')

        self.assertEqual(
            str(err.exception),
            'Could not open config file: myconfig.yaml',
        )

    def test_raises_parse_error(self):
        """
        Test that it raises if file can't be parsed
        """
        with self.assertRaises(PyYAMLConfigError) as err:
            load_config('faulty_config.yaml')

        self.assertEqual(
            str(err.exception),
            'Could not parse config file: faulty_config.yaml',
        )
