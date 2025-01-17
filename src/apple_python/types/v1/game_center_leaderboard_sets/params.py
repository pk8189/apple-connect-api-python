"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class GameCenterLeaderboardSetUpdateRequestDataAttributes(typing_extensions.TypedDict):
    """
    No description specified
    """

    reference_name: typing_extensions.NotRequired[str]


class _SerializerGameCenterLeaderboardSetUpdateRequestDataAttributes(
    pydantic.BaseModel
):
    """
    Serializer for GameCenterLeaderboardSetUpdateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    reference_name: typing.Optional[str] = pydantic.Field(
        alias="referenceName", default=None
    )


class GameCenterLeaderboardSetCreateRequestDataAttributes(typing_extensions.TypedDict):
    """
    No description specified
    """

    reference_name: typing_extensions.Required[str]
    vendor_identifier: typing_extensions.Required[str]


class _SerializerGameCenterLeaderboardSetCreateRequestDataAttributes(
    pydantic.BaseModel
):
    """
    Serializer for GameCenterLeaderboardSetCreateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    reference_name: str = pydantic.Field(alias="referenceName")
    vendor_identifier: str = pydantic.Field(alias="vendorIdentifier")


class GameCenterLeaderboardSetCreateRequestDataRelationshipsGameCenterDetailData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["gameCenterDetails"]]


class _SerializerGameCenterLeaderboardSetCreateRequestDataRelationshipsGameCenterDetailData(
    pydantic.BaseModel
):
    """
    Serializer for GameCenterLeaderboardSetCreateRequestDataRelationshipsGameCenterDetailData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["gameCenterDetails"] = pydantic.Field(alias="type")


class GameCenterLeaderboardSetCreateRequestDataRelationshipsGameCenterGroupData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["gameCenterGroups"]]


class _SerializerGameCenterLeaderboardSetCreateRequestDataRelationshipsGameCenterGroupData(
    pydantic.BaseModel
):
    """
    Serializer for GameCenterLeaderboardSetCreateRequestDataRelationshipsGameCenterGroupData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["gameCenterGroups"] = pydantic.Field(alias="type")


class GameCenterLeaderboardSetCreateRequestDataRelationshipsGameCenterLeaderboardsDataItem(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[
        typing_extensions.Literal["gameCenterLeaderboards"]
    ]


class _SerializerGameCenterLeaderboardSetCreateRequestDataRelationshipsGameCenterLeaderboardsDataItem(
    pydantic.BaseModel
):
    """
    Serializer for GameCenterLeaderboardSetCreateRequestDataRelationshipsGameCenterLeaderboardsDataItem handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["gameCenterLeaderboards"] = pydantic.Field(
        alias="type"
    )


class GameCenterLeaderboardSetUpdateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.NotRequired[
        GameCenterLeaderboardSetUpdateRequestDataAttributes
    ]
    id: typing_extensions.Required[str]
    type: typing_extensions.Required[
        typing_extensions.Literal["gameCenterLeaderboardSets"]
    ]


class _SerializerGameCenterLeaderboardSetUpdateRequestData(pydantic.BaseModel):
    """
    Serializer for GameCenterLeaderboardSetUpdateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: typing.Optional[
        _SerializerGameCenterLeaderboardSetUpdateRequestDataAttributes
    ] = pydantic.Field(alias="attributes", default=None)
    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["gameCenterLeaderboardSets"] = pydantic.Field(
        alias="type"
    )


class GameCenterLeaderboardSetCreateRequestDataRelationshipsGameCenterDetail(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.NotRequired[
        GameCenterLeaderboardSetCreateRequestDataRelationshipsGameCenterDetailData
    ]


class _SerializerGameCenterLeaderboardSetCreateRequestDataRelationshipsGameCenterDetail(
    pydantic.BaseModel
):
    """
    Serializer for GameCenterLeaderboardSetCreateRequestDataRelationshipsGameCenterDetail handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: typing.Optional[
        _SerializerGameCenterLeaderboardSetCreateRequestDataRelationshipsGameCenterDetailData
    ] = pydantic.Field(alias="data", default=None)


class GameCenterLeaderboardSetCreateRequestDataRelationshipsGameCenterGroup(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.NotRequired[
        GameCenterLeaderboardSetCreateRequestDataRelationshipsGameCenterGroupData
    ]


class _SerializerGameCenterLeaderboardSetCreateRequestDataRelationshipsGameCenterGroup(
    pydantic.BaseModel
):
    """
    Serializer for GameCenterLeaderboardSetCreateRequestDataRelationshipsGameCenterGroup handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: typing.Optional[
        _SerializerGameCenterLeaderboardSetCreateRequestDataRelationshipsGameCenterGroupData
    ] = pydantic.Field(alias="data", default=None)


class GameCenterLeaderboardSetCreateRequestDataRelationshipsGameCenterLeaderboards(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.NotRequired[
        typing.List[
            GameCenterLeaderboardSetCreateRequestDataRelationshipsGameCenterLeaderboardsDataItem
        ]
    ]


class _SerializerGameCenterLeaderboardSetCreateRequestDataRelationshipsGameCenterLeaderboards(
    pydantic.BaseModel
):
    """
    Serializer for GameCenterLeaderboardSetCreateRequestDataRelationshipsGameCenterLeaderboards handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: typing.Optional[
        typing.List[
            _SerializerGameCenterLeaderboardSetCreateRequestDataRelationshipsGameCenterLeaderboardsDataItem
        ]
    ] = pydantic.Field(alias="data", default=None)


class GameCenterLeaderboardSetUpdateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[GameCenterLeaderboardSetUpdateRequestData]


class _SerializerGameCenterLeaderboardSetUpdateRequest(pydantic.BaseModel):
    """
    Serializer for GameCenterLeaderboardSetUpdateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerGameCenterLeaderboardSetUpdateRequestData = pydantic.Field(
        alias="data"
    )


class GameCenterLeaderboardSetCreateRequestDataRelationships(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    game_center_detail: typing_extensions.NotRequired[
        GameCenterLeaderboardSetCreateRequestDataRelationshipsGameCenterDetail
    ]
    game_center_group: typing_extensions.NotRequired[
        GameCenterLeaderboardSetCreateRequestDataRelationshipsGameCenterGroup
    ]
    game_center_leaderboards: typing_extensions.NotRequired[
        GameCenterLeaderboardSetCreateRequestDataRelationshipsGameCenterLeaderboards
    ]


class _SerializerGameCenterLeaderboardSetCreateRequestDataRelationships(
    pydantic.BaseModel
):
    """
    Serializer for GameCenterLeaderboardSetCreateRequestDataRelationships handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    game_center_detail: typing.Optional[
        _SerializerGameCenterLeaderboardSetCreateRequestDataRelationshipsGameCenterDetail
    ] = pydantic.Field(alias="gameCenterDetail", default=None)
    game_center_group: typing.Optional[
        _SerializerGameCenterLeaderboardSetCreateRequestDataRelationshipsGameCenterGroup
    ] = pydantic.Field(alias="gameCenterGroup", default=None)
    game_center_leaderboards: typing.Optional[
        _SerializerGameCenterLeaderboardSetCreateRequestDataRelationshipsGameCenterLeaderboards
    ] = pydantic.Field(alias="gameCenterLeaderboards", default=None)


class GameCenterLeaderboardSetCreateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.Required[
        GameCenterLeaderboardSetCreateRequestDataAttributes
    ]
    relationships: typing_extensions.NotRequired[
        GameCenterLeaderboardSetCreateRequestDataRelationships
    ]
    type: typing_extensions.Required[
        typing_extensions.Literal["gameCenterLeaderboardSets"]
    ]


class _SerializerGameCenterLeaderboardSetCreateRequestData(pydantic.BaseModel):
    """
    Serializer for GameCenterLeaderboardSetCreateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: _SerializerGameCenterLeaderboardSetCreateRequestDataAttributes = (
        pydantic.Field(alias="attributes")
    )
    relationships: typing.Optional[
        _SerializerGameCenterLeaderboardSetCreateRequestDataRelationships
    ] = pydantic.Field(alias="relationships", default=None)
    type: typing_extensions.Literal["gameCenterLeaderboardSets"] = pydantic.Field(
        alias="type"
    )


class GameCenterLeaderboardSetCreateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[GameCenterLeaderboardSetCreateRequestData]


class _SerializerGameCenterLeaderboardSetCreateRequest(pydantic.BaseModel):
    """
    Serializer for GameCenterLeaderboardSetCreateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerGameCenterLeaderboardSetCreateRequestData = pydantic.Field(
        alias="data"
    )
