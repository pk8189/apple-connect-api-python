"""File Generated by Sideko (sideko.dev)"""

import io
import typing
import typing_extensions
from pydantic import (
    BaseModel as _PydanticBaseModel,
    Field as _PydanticField,
    ConfigDict as _PydanticConfigDict,
)

ModelFiles = typing.List[
    typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]
]


class GameCenterMatchmakingRuleSetAttributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    max_players: typing.Optional[int] = _PydanticField(alias="maxPlayers", default=None)
    min_players: typing.Optional[int] = _PydanticField(alias="minPlayers", default=None)
    reference_name: typing.Optional[str] = _PydanticField(
        alias="referenceName", default=None
    )
    rule_language_version: typing.Optional[int] = _PydanticField(
        alias="ruleLanguageVersion", default=None
    )


class ResourceLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class GameCenterMatchmakingRuleSetRelationshipsMatchmakingQueuesDataItem(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["gameCenterMatchmakingQueues"] = _PydanticField(
        alias="type"
    )


class GameCenterMatchmakingRuleSetRelationshipsMatchmakingQueuesLinks(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class PagingInformationPaging(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    limit: int = _PydanticField(alias="limit")
    total: typing.Optional[int] = _PydanticField(alias="total", default=None)


class GameCenterMatchmakingRuleSetRelationshipsRulesDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["gameCenterMatchmakingRules"] = _PydanticField(
        alias="type"
    )


class GameCenterMatchmakingRuleSetRelationshipsRulesLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class GameCenterMatchmakingRuleSetRelationshipsTeamsDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["gameCenterMatchmakingTeams"] = _PydanticField(
        alias="type"
    )


class GameCenterMatchmakingRuleSetRelationshipsTeamsLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class GameCenterMatchmakingTeamAttributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    max_players: typing.Optional[int] = _PydanticField(alias="maxPlayers", default=None)
    min_players: typing.Optional[int] = _PydanticField(alias="minPlayers", default=None)
    reference_name: typing.Optional[str] = _PydanticField(
        alias="referenceName", default=None
    )


class GameCenterMatchmakingRuleAttributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    description: typing.Optional[str] = _PydanticField(
        alias="description", default=None
    )
    expression: typing.Optional[str] = _PydanticField(alias="expression", default=None)
    reference_name: typing.Optional[str] = _PydanticField(
        alias="referenceName", default=None
    )
    type: typing.Optional[
        typing_extensions.Literal["COMPATIBLE", "DISTANCE", "MATCH", "TEAM"]
    ] = _PydanticField(alias="type", default=None)
    weight: typing.Optional[float] = _PydanticField(alias="weight", default=None)


class GameCenterMatchmakingQueueAttributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    classic_matchmaking_bundle_ids: typing.Optional[typing.List[str]] = _PydanticField(
        alias="classicMatchmakingBundleIds", default=None
    )
    reference_name: typing.Optional[str] = _PydanticField(
        alias="referenceName", default=None
    )


class GameCenterMatchmakingQueueRelationshipsExperimentRuleSetData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["gameCenterMatchmakingRuleSets"] = _PydanticField(
        alias="type"
    )


class GameCenterMatchmakingQueueRelationshipsExperimentRuleSetLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class GameCenterMatchmakingQueueRelationshipsRuleSetData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["gameCenterMatchmakingRuleSets"] = _PydanticField(
        alias="type"
    )


class GameCenterMatchmakingQueueRelationshipsRuleSetLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class PagedDocumentLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    first: typing.Optional[str] = _PydanticField(alias="first", default=None)
    next: typing.Optional[str] = _PydanticField(alias="next", default=None)
    self: str = _PydanticField(alias="self")


class DocumentLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    self: str = _PydanticField(alias="self")


class PagingInformation(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    paging: PagingInformationPaging = _PydanticField(alias="paging")


class GameCenterMatchmakingRuleSetRelationshipsRules(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        typing.List[GameCenterMatchmakingRuleSetRelationshipsRulesDataItem]
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[GameCenterMatchmakingRuleSetRelationshipsRulesLinks] = (
        _PydanticField(alias="links", default=None)
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class GameCenterMatchmakingRuleSetRelationshipsTeams(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        typing.List[GameCenterMatchmakingRuleSetRelationshipsTeamsDataItem]
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[GameCenterMatchmakingRuleSetRelationshipsTeamsLinks] = (
        _PydanticField(alias="links", default=None)
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class GameCenterMatchmakingTeam(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[GameCenterMatchmakingTeamAttributes] = _PydanticField(
        alias="attributes", default=None
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    type: typing_extensions.Literal["gameCenterMatchmakingTeams"] = _PydanticField(
        alias="type"
    )


class GameCenterMatchmakingRule(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[GameCenterMatchmakingRuleAttributes] = _PydanticField(
        alias="attributes", default=None
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    type: typing_extensions.Literal["gameCenterMatchmakingRules"] = _PydanticField(
        alias="type"
    )


class GameCenterMatchmakingQueueRelationshipsExperimentRuleSet(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        GameCenterMatchmakingQueueRelationshipsExperimentRuleSetData
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[
        GameCenterMatchmakingQueueRelationshipsExperimentRuleSetLinks
    ] = _PydanticField(alias="links", default=None)


class GameCenterMatchmakingQueueRelationshipsRuleSet(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[GameCenterMatchmakingQueueRelationshipsRuleSetData] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[GameCenterMatchmakingQueueRelationshipsRuleSetLinks] = (
        _PydanticField(alias="links", default=None)
    )


class GameCenterMatchmakingRuleSetRelationshipsMatchmakingQueues(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        typing.List[GameCenterMatchmakingRuleSetRelationshipsMatchmakingQueuesDataItem]
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[
        GameCenterMatchmakingRuleSetRelationshipsMatchmakingQueuesLinks
    ] = _PydanticField(alias="links", default=None)
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class GameCenterMatchmakingQueueRelationships(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    experiment_rule_set: typing.Optional[
        GameCenterMatchmakingQueueRelationshipsExperimentRuleSet
    ] = _PydanticField(alias="experimentRuleSet", default=None)
    rule_set: typing.Optional[GameCenterMatchmakingQueueRelationshipsRuleSet] = (
        _PydanticField(alias="ruleSet", default=None)
    )


class GameCenterMatchmakingRuleSetRelationships(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    matchmaking_queues: typing.Optional[
        GameCenterMatchmakingRuleSetRelationshipsMatchmakingQueues
    ] = _PydanticField(alias="matchmakingQueues", default=None)
    rules: typing.Optional[GameCenterMatchmakingRuleSetRelationshipsRules] = (
        _PydanticField(alias="rules", default=None)
    )
    teams: typing.Optional[GameCenterMatchmakingRuleSetRelationshipsTeams] = (
        _PydanticField(alias="teams", default=None)
    )


class GameCenterMatchmakingQueue(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[GameCenterMatchmakingQueueAttributes] = _PydanticField(
        alias="attributes", default=None
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    relationships: typing.Optional[GameCenterMatchmakingQueueRelationships] = (
        _PydanticField(alias="relationships", default=None)
    )
    type: typing_extensions.Literal["gameCenterMatchmakingQueues"] = _PydanticField(
        alias="type"
    )


class GameCenterMatchmakingRuleSet(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[GameCenterMatchmakingRuleSetAttributes] = (
        _PydanticField(alias="attributes", default=None)
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    relationships: typing.Optional[GameCenterMatchmakingRuleSetRelationships] = (
        _PydanticField(alias="relationships", default=None)
    )
    type: typing_extensions.Literal["gameCenterMatchmakingRuleSets"] = _PydanticField(
        alias="type"
    )


class GameCenterMatchmakingRuleSetResponse(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: GameCenterMatchmakingRuleSet = _PydanticField(alias="data")
    included: typing.Optional[
        typing.List[
            typing.Union[
                GameCenterMatchmakingTeam,
                GameCenterMatchmakingRule,
                GameCenterMatchmakingQueue,
            ]
        ]
    ] = _PydanticField(alias="included", default=None)
    links: DocumentLinks = _PydanticField(alias="links")


class GameCenterMatchmakingRuleSetsResponse(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.List[GameCenterMatchmakingRuleSet] = _PydanticField(alias="data")
    included: typing.Optional[
        typing.List[
            typing.Union[
                GameCenterMatchmakingTeam,
                GameCenterMatchmakingRule,
                GameCenterMatchmakingQueue,
            ]
        ]
    ] = _PydanticField(alias="included", default=None)
    links: PagedDocumentLinks = _PydanticField(alias="links")
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )
