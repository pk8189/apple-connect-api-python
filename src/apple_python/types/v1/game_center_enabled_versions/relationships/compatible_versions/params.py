"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class GameCenterEnabledVersionCompatibleVersionsLinkagesRequestDataItem(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[
        typing_extensions.Literal["gameCenterEnabledVersions"]
    ]


class _SerializerGameCenterEnabledVersionCompatibleVersionsLinkagesRequestDataItem(
    pydantic.BaseModel
):
    """
    Serializer for GameCenterEnabledVersionCompatibleVersionsLinkagesRequestDataItem handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["gameCenterEnabledVersions"] = pydantic.Field(
        alias="type"
    )


class GameCenterEnabledVersionCompatibleVersionsLinkagesRequest(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.Required[
        typing.List[GameCenterEnabledVersionCompatibleVersionsLinkagesRequestDataItem]
    ]


class _SerializerGameCenterEnabledVersionCompatibleVersionsLinkagesRequest(
    pydantic.BaseModel
):
    """
    Serializer for GameCenterEnabledVersionCompatibleVersionsLinkagesRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: typing.List[
        _SerializerGameCenterEnabledVersionCompatibleVersionsLinkagesRequestDataItem
    ] = pydantic.Field(alias="data")
