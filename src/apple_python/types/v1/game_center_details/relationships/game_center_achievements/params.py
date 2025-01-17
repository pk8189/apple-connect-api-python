"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class GameCenterDetailGameCenterAchievementsLinkagesRequestDataItem(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[
        typing_extensions.Literal["gameCenterAchievements"]
    ]


class _SerializerGameCenterDetailGameCenterAchievementsLinkagesRequestDataItem(
    pydantic.BaseModel
):
    """
    Serializer for GameCenterDetailGameCenterAchievementsLinkagesRequestDataItem handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["gameCenterAchievements"] = pydantic.Field(
        alias="type"
    )


class GameCenterDetailGameCenterAchievementsLinkagesRequest(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.Required[
        typing.List[GameCenterDetailGameCenterAchievementsLinkagesRequestDataItem]
    ]


class _SerializerGameCenterDetailGameCenterAchievementsLinkagesRequest(
    pydantic.BaseModel
):
    """
    Serializer for GameCenterDetailGameCenterAchievementsLinkagesRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: typing.List[
        _SerializerGameCenterDetailGameCenterAchievementsLinkagesRequestDataItem
    ] = pydantic.Field(alias="data")
