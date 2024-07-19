"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class BetaTesterAppsLinkagesRequestDataItem(typing_extensions.TypedDict):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["apps"]]


class _SerializerBetaTesterAppsLinkagesRequestDataItem(pydantic.BaseModel):
    """
    Serializer for BetaTesterAppsLinkagesRequestDataItem handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["apps"] = pydantic.Field(alias="type")


class BetaTesterAppsLinkagesRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[typing.List[BetaTesterAppsLinkagesRequestDataItem]]


class _SerializerBetaTesterAppsLinkagesRequest(pydantic.BaseModel):
    """
    Serializer for BetaTesterAppsLinkagesRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: typing.List[_SerializerBetaTesterAppsLinkagesRequestDataItem] = (
        pydantic.Field(alias="data")
    )