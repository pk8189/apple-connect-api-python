from typing import Any, Union, Dict, Type, TypeVar, List
from pydantic import BaseModel

EncodableT = TypeVar(
    "EncodableT",
    bound=Union[
        object,
        str,
        int,
        float,
        None,
        BaseModel,
        List[Any],
        Dict[str, Any],
    ],
)


def from_encodable(*, data: Any, load_with: Type[EncodableT]) -> Any:
    class Caster(BaseModel):
        data: load_with  # type: ignore

    return Caster(data=data).data
