import jsony.literal
from jsony.literal import *  # noqa: F403, F401


def test_values() -> None:
    assert jsony.literal.null is None
    assert jsony.literal.true is True
    assert jsony.literal.false is False


def test_specified_load():
    from jsony.literal import false, null, true

    assert null is None  # noqa: F405
    assert true is True  # noqa: F405
    assert false is False  # noqa: F405


def test_auto_load():
    assert null is None  # noqa: F405
    assert true is True  # noqa: F405
    assert false is False  # noqa: F405


def test_json_literal():
    from jsony.literal import false, null, true

    assert {
        "string": "string",
        "float": 1.0,
        "int": 1,
        "null": null,
        "true": true,
        "false": false,
    }
