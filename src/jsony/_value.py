from typing import TypeAlias, TypeVar

JsonStr: TypeAlias = str
JsonValue: TypeAlias = (
    str | int | float | bool | None | dict[str, "JsonValue"] | list["JsonValue"]
)
GenericJsonValue = TypeVar("GenericJsonValue", bound=JsonValue)
