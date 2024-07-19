"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class GameCenterMatchmakingTeamUpdateRequestDataAttributes(typing_extensions.TypedDict):
    """
    No description specified
    """

    max_players: typing_extensions.NotRequired[int]
    min_players: typing_extensions.NotRequired[int]


class _SerializerGameCenterMatchmakingTeamUpdateRequestDataAttributes(
    pydantic.BaseModel
):
    """
    Serializer for GameCenterMatchmakingTeamUpdateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    max_players: typing.Optional[int] = pydantic.Field(alias="maxPlayers", default=None)
    min_players: typing.Optional[int] = pydantic.Field(alias="minPlayers", default=None)


class GameCenterMatchmakingTeamCreateRequestDataAttributes(typing_extensions.TypedDict):
    """
    No description specified
    """

    max_players: typing_extensions.Required[int]
    min_players: typing_extensions.Required[int]
    reference_name: typing_extensions.Required[str]


class _SerializerGameCenterMatchmakingTeamCreateRequestDataAttributes(
    pydantic.BaseModel
):
    """
    Serializer for GameCenterMatchmakingTeamCreateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    max_players: int = pydantic.Field(alias="maxPlayers")
    min_players: int = pydantic.Field(alias="minPlayers")
    reference_name: str = pydantic.Field(alias="referenceName")


class GameCenterMatchmakingTeamCreateRequestDataRelationshipsRuleSetData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[
        typing_extensions.Literal["gameCenterMatchmakingRuleSets"]
    ]


class _SerializerGameCenterMatchmakingTeamCreateRequestDataRelationshipsRuleSetData(
    pydantic.BaseModel
):
    """
    Serializer for GameCenterMatchmakingTeamCreateRequestDataRelationshipsRuleSetData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["gameCenterMatchmakingRuleSets"] = pydantic.Field(
        alias="type"
    )


class GameCenterMatchmakingTeamUpdateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.NotRequired[
        GameCenterMatchmakingTeamUpdateRequestDataAttributes
    ]
    id: typing_extensions.Required[str]
    type: typing_extensions.Required[
        typing_extensions.Literal["gameCenterMatchmakingTeams"]
    ]


class _SerializerGameCenterMatchmakingTeamUpdateRequestData(pydantic.BaseModel):
    """
    Serializer for GameCenterMatchmakingTeamUpdateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: typing.Optional[
        _SerializerGameCenterMatchmakingTeamUpdateRequestDataAttributes
    ] = pydantic.Field(alias="attributes", default=None)
    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["gameCenterMatchmakingTeams"] = pydantic.Field(
        alias="type"
    )


class GameCenterMatchmakingTeamCreateRequestDataRelationshipsRuleSet(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.Required[
        GameCenterMatchmakingTeamCreateRequestDataRelationshipsRuleSetData
    ]


class _SerializerGameCenterMatchmakingTeamCreateRequestDataRelationshipsRuleSet(
    pydantic.BaseModel
):
    """
    Serializer for GameCenterMatchmakingTeamCreateRequestDataRelationshipsRuleSet handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerGameCenterMatchmakingTeamCreateRequestDataRelationshipsRuleSetData = pydantic.Field(
        alias="data"
    )


class GameCenterMatchmakingTeamUpdateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[GameCenterMatchmakingTeamUpdateRequestData]


class _SerializerGameCenterMatchmakingTeamUpdateRequest(pydantic.BaseModel):
    """
    Serializer for GameCenterMatchmakingTeamUpdateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerGameCenterMatchmakingTeamUpdateRequestData = pydantic.Field(
        alias="data"
    )


class GameCenterMatchmakingTeamCreateRequestDataRelationships(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    rule_set: typing_extensions.Required[
        GameCenterMatchmakingTeamCreateRequestDataRelationshipsRuleSet
    ]


class _SerializerGameCenterMatchmakingTeamCreateRequestDataRelationships(
    pydantic.BaseModel
):
    """
    Serializer for GameCenterMatchmakingTeamCreateRequestDataRelationships handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    rule_set: _SerializerGameCenterMatchmakingTeamCreateRequestDataRelationshipsRuleSet = pydantic.Field(
        alias="ruleSet"
    )


class GameCenterMatchmakingTeamCreateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.Required[
        GameCenterMatchmakingTeamCreateRequestDataAttributes
    ]
    relationships: typing_extensions.Required[
        GameCenterMatchmakingTeamCreateRequestDataRelationships
    ]
    type: typing_extensions.Required[
        typing_extensions.Literal["gameCenterMatchmakingTeams"]
    ]


class _SerializerGameCenterMatchmakingTeamCreateRequestData(pydantic.BaseModel):
    """
    Serializer for GameCenterMatchmakingTeamCreateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: _SerializerGameCenterMatchmakingTeamCreateRequestDataAttributes = (
        pydantic.Field(alias="attributes")
    )
    relationships: _SerializerGameCenterMatchmakingTeamCreateRequestDataRelationships = pydantic.Field(
        alias="relationships"
    )
    type: typing_extensions.Literal["gameCenterMatchmakingTeams"] = pydantic.Field(
        alias="type"
    )


class GameCenterMatchmakingTeamCreateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[GameCenterMatchmakingTeamCreateRequestData]


class _SerializerGameCenterMatchmakingTeamCreateRequest(pydantic.BaseModel):
    """
    Serializer for GameCenterMatchmakingTeamCreateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerGameCenterMatchmakingTeamCreateRequestData = pydantic.Field(
        alias="data"
    )
