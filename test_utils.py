import pytest

from utils import add_two_numbers


class TestAddTwoNumbers:
    def test_add_two_numbers_succes(self):
        number1 = 2
        number2 = 3
        expected_result = 5
        actual_result = add_two_numbers(number1, number2)
        assert actual_result == expected_result, f"fix{add_two_numbers()}"

    def test_add_two_numbers_error(self):
        number1 = "jdfjskdfkjs"
        number2 = "dfsjdfjsfjk"
        with pytest.raises(ValueError):
            add_two_numbers(number1, number2)

    @pytest.mark.parametrize(
        "number1, number2, expected_result", [(2, 3, 5), ("23", "23", 46)]
    )
    def test_success(self, number1, number2, expected_result):
        actual_result = add_two_numbers(number1, number2)
        assert actual_result == expected_result
