"""
Integration tests for pyyamlconfig
"""
import os
import unittest
# pylint: disable=import-error
from pyyamlconfig import (
    load_config,
    write_config,
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
        config = load_config('tests/config.yaml')
        self.assertEqual(
            config,
            {'mykey': 'myvalue'},
        )

    def test_raises_file_not_found(self):
        """
        Test that it raises if file is not found
        """
        with self.assertRaises(PyYAMLConfigError) as err:
            load_config('tests/myconfig.yaml')

        self.assertEqual(
            str(err.exception),
            'Could not open config file: tests/myconfig.yaml',
        )

    def test_raises_parse_error(self):
        """
        Test that it raises if file can't be parsed
        """
        with self.assertRaises(PyYAMLConfigError) as err:
            load_config('tests/faulty_config.yaml')

        self.assertEqual(
            str(err.exception),
            'Could not parse config file: tests/faulty_config.yaml',
        )


class TestWriteConfig(unittest.TestCase):
    """
    Tests for pyyamlconfig.load_config
    """
    def test_writes_config(self):
        """
        Test that config can be written
        """
        try:
            os.remove('tests/written_config.yaml')
        except FileNotFoundError:
            pass

        write_config(
            'tests/written_config.yaml',
            {'mywrittenkey': 'mywrittenvalue'}
        )

        with open('tests/written_config.yaml') as file:
            self.assertEqual(
                file.read(),
                'mywrittenkey: mywrittenvalue\n',
            )
