"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class GameCenterGroupGameCenterLeaderboardSetsLinkagesRequestDataItem(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[
        typing_extensions.Literal["gameCenterLeaderboardSets"]
    ]


class _SerializerGameCenterGroupGameCenterLeaderboardSetsLinkagesRequestDataItem(
    pydantic.BaseModel
):
    """
    Serializer for GameCenterGroupGameCenterLeaderboardSetsLinkagesRequestDataItem handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["gameCenterLeaderboardSets"] = pydantic.Field(
        alias="type"
    )


class GameCenterGroupGameCenterLeaderboardSetsLinkagesRequest(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.Required[
        typing.List[GameCenterGroupGameCenterLeaderboardSetsLinkagesRequestDataItem]
    ]


class _SerializerGameCenterGroupGameCenterLeaderboardSetsLinkagesRequest(
    pydantic.BaseModel
):
    """
    Serializer for GameCenterGroupGameCenterLeaderboardSetsLinkagesRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: typing.List[
        _SerializerGameCenterGroupGameCenterLeaderboardSetsLinkagesRequestDataItem
    ] = pydantic.Field(alias="data")
