from typing import Any

import hamcrest as hc


class AssertThat:
    def __init__(self, actual: Any) -> None:
        self._actual = actual

    def is_true(self, message: str = "Expected value is 'False'") -> None:
        """Checks boolean value is True"""
        if not isinstance(self._actual, bool):
            raise TypeError("Unexpected parameter type. Boolean type is expected")
        hc.assert_that(self._actual, message)

    def is_false(self, message: str = "Expected value is 'True'") -> None:
        """Checks boolean value is False"""
        if not isinstance(self._actual, bool):
            raise TypeError("Unexpected parameter type. Boolean type is expected")
        hc.assert_that(self._actual, hc.is_(False), message)

    def is_none(self, message: str = "Expected value is 'None'") -> None:
        hc.assert_that(self._actual, hc.is_(None), message)

    def is_not_none(self, message: str = "Expected value is not 'None'") -> None:
        hc.assert_that(self._actual, hc.is_not(None), message)

    def equal_to(self, expected: Any, message: str = "Objects are not equal") -> None:
        """Checks objects are equal"""
        if isinstance(self._actual, bool):
            hc.assert_that(self._actual, hc.is_(expected), message)
        else:
            hc.assert_that(self._actual, hc.equal_to(expected), message)

    def not_equal_to(self, expected: Any, message: str = "Objects are equal") -> None:
        """Checks objects are not equal"""
        if isinstance(self._actual, bool):
            hc.assert_that(self._actual, hc.is_not(expected), message)
        else:
            hc.assert_that(self._actual, hc.not_(hc.equal_to(expected)), message)

    def is_in(self, item: Any, message: str = "The object is not present in given sequence") -> None:
        """Checks if evaluated object is present in a given sequence"""
        hc.assert_that(self._actual, hc.is_in(item), message)

    def not_is_in(self, item: Any, message: str = "The object is present in given sequence") -> None:
        """Checks if evaluated object is not present in a given sequence"""
        hc.assert_that(self._actual, hc.not_(hc.is_in(item)), message)
