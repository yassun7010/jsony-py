import pytest
from jsony import (
    JsonNullValueError,
    JsonValue,
    JsonValueTypeError,
    dig,
    dig_as,
)


class TestDig:
    def test_dig(self):
        assert dig({"a": 1}, "a") == 1
        assert dig(["a", "b"], 1) == "b"
        assert dig({"a": {"b": 2}}, "a", "b") == 2
        assert dig(["a", ["b", 2]], 1, 1) == 2

    def test_dig_failed(self):
        assert dig({"a": 1}, "b") is None
        assert dig("a", "b") is None
        assert dig(["a", "b"], 2) is None
        assert dig({"a": {"b": 2}}, "a", "c") is None
        assert dig(["a", ["b", 2]], 1, 2) is None


class TestDigAs:
    def test_dag_as(self):
        assert dig_as(str, {"a": "b"}, "a") == "b"
        assert dig_as(str, ["a", "b"], 1) == "b"
        assert dig_as(int, {"a": {"b": 2}}, "a", "b") == 2
        assert dig_as(int, ["a", ["b", 2]], 1, 1) == 2
        assert dig_as(bool, {"a": True}, "a") is True
        assert dig_as(dict[str, JsonValue], {"a": {"b": 2}}, "a") == {"b": 2}
        assert dig_as(list[JsonValue], ["a", ["b", 2]], 1) == ["b", 2]

    def test_dag_as_with_allow_null_options(self):
        _: str = dig_as(str, {"a": "b"}, "a")
        _: str | None = dig_as(str, {"a": "b"}, "a", allow_null=True)

    def test_dag_as_null_error(self):
        assert dig_as(str, {"a": "b"}, "c", allow_null=True) is None

        with pytest.raises(JsonNullValueError):
            _: str = dig_as(str, {"a": "b"}, "c")

    def test_dag_as_value_type_error(self):
        with pytest.raises(JsonValueTypeError):
            dig_as(int, {"a": "b"}, "a")

    def test_dig_update(self):
        origin: JsonValue = {"a": {"b": 2}}

        dig_as(dict[str, JsonValue], origin, "a").update(b=5)

        assert origin == {"a": {"b": 5}}
