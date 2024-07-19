"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class BetaGroupBetaTestersLinkagesRequestDataItem(typing_extensions.TypedDict):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["betaTesters"]]


class _SerializerBetaGroupBetaTestersLinkagesRequestDataItem(pydantic.BaseModel):
    """
    Serializer for BetaGroupBetaTestersLinkagesRequestDataItem handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["betaTesters"] = pydantic.Field(alias="type")


class BetaGroupBetaTestersLinkagesRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[
        typing.List[BetaGroupBetaTestersLinkagesRequestDataItem]
    ]


class _SerializerBetaGroupBetaTestersLinkagesRequest(pydantic.BaseModel):
    """
    Serializer for BetaGroupBetaTestersLinkagesRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: typing.List[_SerializerBetaGroupBetaTestersLinkagesRequestDataItem] = (
        pydantic.Field(alias="data")
    )