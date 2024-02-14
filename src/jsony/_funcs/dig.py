from typing import Literal, cast

from jsony._value import GenericJsonValue, JsonValue
from jsony.exceptions import JsonNullValueError, JsonValueTypeError
from typing_extensions import overload


def dig(data: JsonValue, *keys: str | int) -> JsonValue:
    try:
        for key in keys:
            if isinstance(data, dict) and isinstance(key, str):
                data = data[key]

            elif isinstance(data, list) and isinstance(key, int):
                data = data[key]

            else:
                return None

        return data

    except (KeyError, IndexError) as _:
        return None


@overload
def dig_as(
    value_type: type[GenericJsonValue],
    self: JsonValue,
    *keys: str | int,
    allow_null: Literal[False] = False,
) -> GenericJsonValue:
    ...


@overload
def dig_as(
    value_type: type[GenericJsonValue],
    self: JsonValue,
    *keys: str | int,
    allow_null: Literal[True],
) -> GenericJsonValue | None:
    ...


def dig_as(
    value_type: type[GenericJsonValue],
    self: JsonValue,
    *keys: str | int,
    allow_null=False,
) -> GenericJsonValue | None:
    data = dig(self, *keys)

    if data is None:
        if allow_null:
            return None

        else:
            raise JsonNullValueError(data, keys)

    while hasattr(value_type, "__origin__"):
        value_type = cast(
            type[GenericJsonValue],
            value_type.__origin__,  # type: ignore
        )

    if not isinstance(data, value_type):
        raise JsonValueTypeError(value_type, data, keys)

    return data
