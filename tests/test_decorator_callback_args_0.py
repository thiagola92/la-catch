import unittest
from typing import Type
from unittest import TestCase

from la_catch import Catch


class TestContextManagerCallbackArgs(TestCase):
    """Test if the arguments and exception are being pass to callback"""

    def setUp(self) -> None:
        self._exception = Exception("Exception")

    def test_context_manager(self):
        def test(a, b, e):
            assert a == 1
            assert b == 2
            assert e == self._exception

        @Catch(Exception, test, 1, 2)
        def func():
            raise self._exception

        func()
        func()

    def test_context_manager_2(self):
        def test(a, b, exception):
            assert a == 1
            assert b == 2
            assert exception == self._exception

        @Catch(Exception, test, 1, b=2)
        def func():
            raise self._exception

        func()
        func()

    def test_context_manager_3(self):
        def test(a, b, exception):
            assert a == 1
            assert b == 2
            assert exception == self._exception

        @Catch(Exception, test, a=1, b=2)
        def func():
            raise self._exception

        func()
        func()


if __name__ == "__main__":
    unittest.main()
