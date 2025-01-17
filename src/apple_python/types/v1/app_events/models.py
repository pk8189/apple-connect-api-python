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


class AppEventAttributesArchivedTerritorySchedulesItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    event_end: typing.Optional[str] = _PydanticField(alias="eventEnd", default=None)
    event_start: typing.Optional[str] = _PydanticField(alias="eventStart", default=None)
    publish_start: typing.Optional[str] = _PydanticField(
        alias="publishStart", default=None
    )
    territories: typing.Optional[typing.List[str]] = _PydanticField(
        alias="territories", default=None
    )


class AppEventAttributesTerritorySchedulesItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    event_end: typing.Optional[str] = _PydanticField(alias="eventEnd", default=None)
    event_start: typing.Optional[str] = _PydanticField(alias="eventStart", default=None)
    publish_start: typing.Optional[str] = _PydanticField(
        alias="publishStart", default=None
    )
    territories: typing.Optional[typing.List[str]] = _PydanticField(
        alias="territories", default=None
    )


class ResourceLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppEventRelationshipsLocalizationsDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["appEventLocalizations"] = _PydanticField(
        alias="type"
    )


class AppEventRelationshipsLocalizationsLinks(_PydanticBaseModel):
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


class AppEventLocalizationAttributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    locale_field: typing.Optional[str] = _PydanticField(alias="locale", default=None)
    long_description: typing.Optional[str] = _PydanticField(
        alias="longDescription", default=None
    )
    name: typing.Optional[str] = _PydanticField(alias="name", default=None)
    short_description: typing.Optional[str] = _PydanticField(
        alias="shortDescription", default=None
    )


class AppEventLocalizationRelationshipsAppEventData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["appEvents"] = _PydanticField(alias="type")


class AppEventLocalizationRelationshipsAppEventLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppEventLocalizationRelationshipsAppEventScreenshotsDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["appEventScreenshots"] = _PydanticField(
        alias="type"
    )


class AppEventLocalizationRelationshipsAppEventScreenshotsLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppEventLocalizationRelationshipsAppEventVideoClipsDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["appEventVideoClips"] = _PydanticField(alias="type")


class AppEventLocalizationRelationshipsAppEventVideoClipsLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class DocumentLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    self: str = _PydanticField(alias="self")


class AppEventAttributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    archived_territory_schedules: typing.Optional[
        typing.List[AppEventAttributesArchivedTerritorySchedulesItem]
    ] = _PydanticField(alias="archivedTerritorySchedules", default=None)
    badge: typing.Optional[
        typing_extensions.Literal[
            "LIVE_EVENT",
            "PREMIERE",
            "CHALLENGE",
            "COMPETITION",
            "NEW_SEASON",
            "MAJOR_UPDATE",
            "SPECIAL_EVENT",
        ]
    ] = _PydanticField(alias="badge", default=None)
    deep_link: typing.Optional[str] = _PydanticField(alias="deepLink", default=None)
    event_state: typing.Optional[
        typing_extensions.Literal[
            "DRAFT",
            "READY_FOR_REVIEW",
            "WAITING_FOR_REVIEW",
            "IN_REVIEW",
            "REJECTED",
            "ACCEPTED",
            "APPROVED",
            "PUBLISHED",
            "PAST",
            "ARCHIVED",
        ]
    ] = _PydanticField(alias="eventState", default=None)
    primary_locale: typing.Optional[str] = _PydanticField(
        alias="primaryLocale", default=None
    )
    priority: typing.Optional[typing_extensions.Literal["HIGH", "NORMAL"]] = (
        _PydanticField(alias="priority", default=None)
    )
    purchase_requirement: typing.Optional[
        typing_extensions.Literal[
            "NO_COST_ASSOCIATED",
            "IN_APP_PURCHASE",
            "SUBSCRIPTION",
            "IN_APP_PURCHASE_AND_SUBSCRIPTION",
            "IN_APP_PURCHASE_OR_SUBSCRIPTION",
        ]
    ] = _PydanticField(alias="purchaseRequirement", default=None)
    purpose: typing.Optional[
        typing_extensions.Literal[
            "APPROPRIATE_FOR_ALL_USERS",
            "ATTRACT_NEW_USERS",
            "KEEP_ACTIVE_USERS_INFORMED",
            "BRING_BACK_LAPSED_USERS",
        ]
    ] = _PydanticField(alias="purpose", default=None)
    reference_name: typing.Optional[str] = _PydanticField(
        alias="referenceName", default=None
    )
    territory_schedules: typing.Optional[
        typing.List[AppEventAttributesTerritorySchedulesItem]
    ] = _PydanticField(alias="territorySchedules", default=None)


class PagingInformation(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    paging: PagingInformationPaging = _PydanticField(alias="paging")


class AppEventLocalizationRelationshipsAppEvent(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[AppEventLocalizationRelationshipsAppEventData] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[AppEventLocalizationRelationshipsAppEventLinks] = (
        _PydanticField(alias="links", default=None)
    )


class AppEventLocalizationRelationshipsAppEventScreenshots(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        typing.List[AppEventLocalizationRelationshipsAppEventScreenshotsDataItem]
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[
        AppEventLocalizationRelationshipsAppEventScreenshotsLinks
    ] = _PydanticField(alias="links", default=None)
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class AppEventLocalizationRelationshipsAppEventVideoClips(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        typing.List[AppEventLocalizationRelationshipsAppEventVideoClipsDataItem]
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[AppEventLocalizationRelationshipsAppEventVideoClipsLinks] = (
        _PydanticField(alias="links", default=None)
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class AppEventRelationshipsLocalizations(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.List[AppEventRelationshipsLocalizationsDataItem]] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[AppEventRelationshipsLocalizationsLinks] = _PydanticField(
        alias="links", default=None
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class AppEventLocalizationRelationships(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    app_event: typing.Optional[AppEventLocalizationRelationshipsAppEvent] = (
        _PydanticField(alias="appEvent", default=None)
    )
    app_event_screenshots: typing.Optional[
        AppEventLocalizationRelationshipsAppEventScreenshots
    ] = _PydanticField(alias="appEventScreenshots", default=None)
    app_event_video_clips: typing.Optional[
        AppEventLocalizationRelationshipsAppEventVideoClips
    ] = _PydanticField(alias="appEventVideoClips", default=None)


class AppEventRelationships(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    localizations: typing.Optional[AppEventRelationshipsLocalizations] = _PydanticField(
        alias="localizations", default=None
    )


class AppEventLocalization(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[AppEventLocalizationAttributes] = _PydanticField(
        alias="attributes", default=None
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    relationships: typing.Optional[AppEventLocalizationRelationships] = _PydanticField(
        alias="relationships", default=None
    )
    type: typing_extensions.Literal["appEventLocalizations"] = _PydanticField(
        alias="type"
    )


class AppEvent(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[AppEventAttributes] = _PydanticField(
        alias="attributes", default=None
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    relationships: typing.Optional[AppEventRelationships] = _PydanticField(
        alias="relationships", default=None
    )
    type: typing_extensions.Literal["appEvents"] = _PydanticField(alias="type")


class AppEventResponse(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: AppEvent = _PydanticField(alias="data")
    included: typing.Optional[typing.List[AppEventLocalization]] = _PydanticField(
        alias="included", default=None
    )
    links: DocumentLinks = _PydanticField(alias="links")
