"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class GameCenterAchievementGroupAchievementLinkageRequestData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[
        typing_extensions.Literal["gameCenterAchievements"]
    ]


class _SerializerGameCenterAchievementGroupAchievementLinkageRequestData(
    pydantic.BaseModel
):
    """
    Serializer for GameCenterAchievementGroupAchievementLinkageRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["gameCenterAchievements"] = pydantic.Field(
        alias="type"
    )


class GameCenterAchievementGroupAchievementLinkageRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[
        GameCenterAchievementGroupAchievementLinkageRequestData
    ]


class _SerializerGameCenterAchievementGroupAchievementLinkageRequest(
    pydantic.BaseModel
):
    """
    Serializer for GameCenterAchievementGroupAchievementLinkageRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerGameCenterAchievementGroupAchievementLinkageRequestData = (
        pydantic.Field(alias="data")
    )
