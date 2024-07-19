"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class GameCenterAchievementReleaseCreateRequestDataRelationshipsGameCenterAchievementData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[
        typing_extensions.Literal["gameCenterAchievements"]
    ]


class _SerializerGameCenterAchievementReleaseCreateRequestDataRelationshipsGameCenterAchievementData(
    pydantic.BaseModel
):
    """
    Serializer for GameCenterAchievementReleaseCreateRequestDataRelationshipsGameCenterAchievementData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["gameCenterAchievements"] = pydantic.Field(
        alias="type"
    )


class GameCenterAchievementReleaseCreateRequestDataRelationshipsGameCenterDetailData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["gameCenterDetails"]]


class _SerializerGameCenterAchievementReleaseCreateRequestDataRelationshipsGameCenterDetailData(
    pydantic.BaseModel
):
    """
    Serializer for GameCenterAchievementReleaseCreateRequestDataRelationshipsGameCenterDetailData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["gameCenterDetails"] = pydantic.Field(alias="type")


class GameCenterAchievementReleaseCreateRequestDataRelationshipsGameCenterAchievement(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.Required[
        GameCenterAchievementReleaseCreateRequestDataRelationshipsGameCenterAchievementData
    ]


class _SerializerGameCenterAchievementReleaseCreateRequestDataRelationshipsGameCenterAchievement(
    pydantic.BaseModel
):
    """
    Serializer for GameCenterAchievementReleaseCreateRequestDataRelationshipsGameCenterAchievement handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerGameCenterAchievementReleaseCreateRequestDataRelationshipsGameCenterAchievementData = pydantic.Field(
        alias="data"
    )


class GameCenterAchievementReleaseCreateRequestDataRelationshipsGameCenterDetail(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.Required[
        GameCenterAchievementReleaseCreateRequestDataRelationshipsGameCenterDetailData
    ]


class _SerializerGameCenterAchievementReleaseCreateRequestDataRelationshipsGameCenterDetail(
    pydantic.BaseModel
):
    """
    Serializer for GameCenterAchievementReleaseCreateRequestDataRelationshipsGameCenterDetail handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerGameCenterAchievementReleaseCreateRequestDataRelationshipsGameCenterDetailData = pydantic.Field(
        alias="data"
    )


class GameCenterAchievementReleaseCreateRequestDataRelationships(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    game_center_achievement: typing_extensions.Required[
        GameCenterAchievementReleaseCreateRequestDataRelationshipsGameCenterAchievement
    ]
    game_center_detail: typing_extensions.Required[
        GameCenterAchievementReleaseCreateRequestDataRelationshipsGameCenterDetail
    ]


class _SerializerGameCenterAchievementReleaseCreateRequestDataRelationships(
    pydantic.BaseModel
):
    """
    Serializer for GameCenterAchievementReleaseCreateRequestDataRelationships handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    game_center_achievement: _SerializerGameCenterAchievementReleaseCreateRequestDataRelationshipsGameCenterAchievement = pydantic.Field(
        alias="gameCenterAchievement"
    )
    game_center_detail: _SerializerGameCenterAchievementReleaseCreateRequestDataRelationshipsGameCenterDetail = pydantic.Field(
        alias="gameCenterDetail"
    )


class GameCenterAchievementReleaseCreateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    relationships: typing_extensions.Required[
        GameCenterAchievementReleaseCreateRequestDataRelationships
    ]
    type: typing_extensions.Required[
        typing_extensions.Literal["gameCenterAchievementReleases"]
    ]


class _SerializerGameCenterAchievementReleaseCreateRequestData(pydantic.BaseModel):
    """
    Serializer for GameCenterAchievementReleaseCreateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    relationships: _SerializerGameCenterAchievementReleaseCreateRequestDataRelationships = pydantic.Field(
        alias="relationships"
    )
    type: typing_extensions.Literal["gameCenterAchievementReleases"] = pydantic.Field(
        alias="type"
    )


class GameCenterAchievementReleaseCreateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[GameCenterAchievementReleaseCreateRequestData]


class _SerializerGameCenterAchievementReleaseCreateRequest(pydantic.BaseModel):
    """
    Serializer for GameCenterAchievementReleaseCreateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerGameCenterAchievementReleaseCreateRequestData = pydantic.Field(
        alias="data"
    )