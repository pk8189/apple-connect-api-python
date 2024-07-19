"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class AppBetaTestersLinkagesRequestDataItem(typing_extensions.TypedDict):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["betaTesters"]]


class _SerializerAppBetaTestersLinkagesRequestDataItem(pydantic.BaseModel):
    """
    Serializer for AppBetaTestersLinkagesRequestDataItem handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["betaTesters"] = pydantic.Field(alias="type")


class AppBetaTestersLinkagesRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[typing.List[AppBetaTestersLinkagesRequestDataItem]]


class _SerializerAppBetaTestersLinkagesRequest(pydantic.BaseModel):
    """
    Serializer for AppBetaTestersLinkagesRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: typing.List[_SerializerAppBetaTestersLinkagesRequestDataItem] = (
        pydantic.Field(alias="data")
    )
