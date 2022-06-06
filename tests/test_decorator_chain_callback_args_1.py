import unittest
from unittest import TestCase

from la_catch import Catch


class TestDecorator(TestCase):
    """Test if is possible to chain Catchs"""

    def setUp(self) -> None:
        self._type_error = TypeError()
        self._file_not_found = FileNotFoundError()

    def test_decorator(self):
        m = "Unknown fail"

        def on_file_error(message, exception):
            assert message == m
            assert exception == self._file_not_found

        def on_type_error(message, exception):
            assert message == m
            assert exception == self._type_error

        @Catch(FileNotFoundError, callback=on_file_error)
        @Catch(TypeError, callback=on_type_error)
        def func(message=m):
            raise self._type_error

        func()
        func()

    def test_decorator_2(self):
        m = "Unknown fail"

        def on_file_error(message, exception):
            assert message == m
            assert exception == self._file_not_found

        def on_type_error(message, exception):
            assert message == m
            assert exception == self._type_error

        @Catch(FileNotFoundError, callback=on_file_error)
        @Catch(TypeError, callback=on_type_error)
        def func(message=m):
            raise self._file_not_found

        func()
        func()


if __name__ == "__main__":
    unittest.main()
