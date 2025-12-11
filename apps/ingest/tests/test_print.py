import sys


def test_print() -> None:
    """
        Test printing from app
    :return:
    """

    assert print("print test with [print]") is None
    assert sys.stdout.write("print test with [sys.stdout.write]") is not None
