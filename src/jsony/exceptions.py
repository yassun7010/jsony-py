from typing import Sequence

from jsony._value import GenericJsonValue, JsonValue


class JsonyError(Exception):
    pass


class JsonNullValueError(JsonyError, ValueError):
    def __init__(self, data: JsonValue, keys: Sequence[str | int]) -> None:
        self.data = data
        self.keys = keys

    def __str__(self) -> str:
        return f"Expected not None, got {self.data} in {self.keys}"


class JsonValueTypeError(JsonyError, TypeError):
    def __init__(
        self,
        value_type: type[GenericJsonValue],
        data: JsonValue,
        keys: Sequence[str | int],
    ) -> None:
        self.value_type = value_type
        self.data = data
        self.keys = keys

    def __str__(self) -> str:
        return f"Expected {self.value_type}, got {type(self.data)} in {self.keys}"
