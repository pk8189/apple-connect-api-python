"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class GameCenterAchievementUpdateRequestDataAttributes(typing_extensions.TypedDict):
    """
    No description specified
    """

    archived: typing_extensions.NotRequired[bool]
    points: typing_extensions.NotRequired[int]
    reference_name: typing_extensions.NotRequired[str]
    repeatable: typing_extensions.NotRequired[bool]
    show_before_earned: typing_extensions.NotRequired[bool]


class _SerializerGameCenterAchievementUpdateRequestDataAttributes(pydantic.BaseModel):
    """
    Serializer for GameCenterAchievementUpdateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    archived: typing.Optional[bool] = pydantic.Field(alias="archived", default=None)
    points: typing.Optional[int] = pydantic.Field(alias="points", default=None)
    reference_name: typing.Optional[str] = pydantic.Field(
        alias="referenceName", default=None
    )
    repeatable: typing.Optional[bool] = pydantic.Field(alias="repeatable", default=None)
    show_before_earned: typing.Optional[bool] = pydantic.Field(
        alias="showBeforeEarned", default=None
    )


class GameCenterAchievementCreateRequestDataAttributes(typing_extensions.TypedDict):
    """
    No description specified
    """

    points: typing_extensions.Required[int]
    reference_name: typing_extensions.Required[str]
    repeatable: typing_extensions.Required[bool]
    show_before_earned: typing_extensions.Required[bool]
    vendor_identifier: typing_extensions.Required[str]


class _SerializerGameCenterAchievementCreateRequestDataAttributes(pydantic.BaseModel):
    """
    Serializer for GameCenterAchievementCreateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    points: int = pydantic.Field(alias="points")
    reference_name: str = pydantic.Field(alias="referenceName")
    repeatable: bool = pydantic.Field(alias="repeatable")
    show_before_earned: bool = pydantic.Field(alias="showBeforeEarned")
    vendor_identifier: str = pydantic.Field(alias="vendorIdentifier")


class GameCenterAchievementCreateRequestDataRelationshipsGameCenterDetailData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["gameCenterDetails"]]


class _SerializerGameCenterAchievementCreateRequestDataRelationshipsGameCenterDetailData(
    pydantic.BaseModel
):
    """
    Serializer for GameCenterAchievementCreateRequestDataRelationshipsGameCenterDetailData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["gameCenterDetails"] = pydantic.Field(alias="type")


class GameCenterAchievementCreateRequestDataRelationshipsGameCenterGroupData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["gameCenterGroups"]]


class _SerializerGameCenterAchievementCreateRequestDataRelationshipsGameCenterGroupData(
    pydantic.BaseModel
):
    """
    Serializer for GameCenterAchievementCreateRequestDataRelationshipsGameCenterGroupData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["gameCenterGroups"] = pydantic.Field(alias="type")


class GameCenterAchievementUpdateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.NotRequired[
        GameCenterAchievementUpdateRequestDataAttributes
    ]
    id: typing_extensions.Required[str]
    type: typing_extensions.Required[
        typing_extensions.Literal["gameCenterAchievements"]
    ]


class _SerializerGameCenterAchievementUpdateRequestData(pydantic.BaseModel):
    """
    Serializer for GameCenterAchievementUpdateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: typing.Optional[
        _SerializerGameCenterAchievementUpdateRequestDataAttributes
    ] = pydantic.Field(alias="attributes", default=None)
    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["gameCenterAchievements"] = pydantic.Field(
        alias="type"
    )


class GameCenterAchievementCreateRequestDataRelationshipsGameCenterDetail(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.NotRequired[
        GameCenterAchievementCreateRequestDataRelationshipsGameCenterDetailData
    ]


class _SerializerGameCenterAchievementCreateRequestDataRelationshipsGameCenterDetail(
    pydantic.BaseModel
):
    """
    Serializer for GameCenterAchievementCreateRequestDataRelationshipsGameCenterDetail handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: typing.Optional[
        _SerializerGameCenterAchievementCreateRequestDataRelationshipsGameCenterDetailData
    ] = pydantic.Field(alias="data", default=None)


class GameCenterAchievementCreateRequestDataRelationshipsGameCenterGroup(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.NotRequired[
        GameCenterAchievementCreateRequestDataRelationshipsGameCenterGroupData
    ]


class _SerializerGameCenterAchievementCreateRequestDataRelationshipsGameCenterGroup(
    pydantic.BaseModel
):
    """
    Serializer for GameCenterAchievementCreateRequestDataRelationshipsGameCenterGroup handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: typing.Optional[
        _SerializerGameCenterAchievementCreateRequestDataRelationshipsGameCenterGroupData
    ] = pydantic.Field(alias="data", default=None)


class GameCenterAchievementUpdateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[GameCenterAchievementUpdateRequestData]


class _SerializerGameCenterAchievementUpdateRequest(pydantic.BaseModel):
    """
    Serializer for GameCenterAchievementUpdateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerGameCenterAchievementUpdateRequestData = pydantic.Field(
        alias="data"
    )


class GameCenterAchievementCreateRequestDataRelationships(typing_extensions.TypedDict):
    """
    No description specified
    """

    game_center_detail: typing_extensions.NotRequired[
        GameCenterAchievementCreateRequestDataRelationshipsGameCenterDetail
    ]
    game_center_group: typing_extensions.NotRequired[
        GameCenterAchievementCreateRequestDataRelationshipsGameCenterGroup
    ]


class _SerializerGameCenterAchievementCreateRequestDataRelationships(
    pydantic.BaseModel
):
    """
    Serializer for GameCenterAchievementCreateRequestDataRelationships handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    game_center_detail: typing.Optional[
        _SerializerGameCenterAchievementCreateRequestDataRelationshipsGameCenterDetail
    ] = pydantic.Field(alias="gameCenterDetail", default=None)
    game_center_group: typing.Optional[
        _SerializerGameCenterAchievementCreateRequestDataRelationshipsGameCenterGroup
    ] = pydantic.Field(alias="gameCenterGroup", default=None)


class GameCenterAchievementCreateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.Required[
        GameCenterAchievementCreateRequestDataAttributes
    ]
    relationships: typing_extensions.NotRequired[
        GameCenterAchievementCreateRequestDataRelationships
    ]
    type: typing_extensions.Required[
        typing_extensions.Literal["gameCenterAchievements"]
    ]


class _SerializerGameCenterAchievementCreateRequestData(pydantic.BaseModel):
    """
    Serializer for GameCenterAchievementCreateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: _SerializerGameCenterAchievementCreateRequestDataAttributes = (
        pydantic.Field(alias="attributes")
    )
    relationships: typing.Optional[
        _SerializerGameCenterAchievementCreateRequestDataRelationships
    ] = pydantic.Field(alias="relationships", default=None)
    type: typing_extensions.Literal["gameCenterAchievements"] = pydantic.Field(
        alias="type"
    )


class GameCenterAchievementCreateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[GameCenterAchievementCreateRequestData]


class _SerializerGameCenterAchievementCreateRequest(pydantic.BaseModel):
    """
    Serializer for GameCenterAchievementCreateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerGameCenterAchievementCreateRequestData = pydantic.Field(
        alias="data"
    )
