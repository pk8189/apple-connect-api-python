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


class SubscriptionGroupLocalizationAttributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    custom_app_name: typing.Optional[str] = _PydanticField(
        alias="customAppName", default=None
    )
    locale_field: typing.Optional[str] = _PydanticField(alias="locale", default=None)
    name: typing.Optional[str] = _PydanticField(alias="name", default=None)
    state: typing.Optional[
        typing_extensions.Literal[
            "PREPARE_FOR_SUBMISSION", "WAITING_FOR_REVIEW", "APPROVED", "REJECTED"
        ]
    ] = _PydanticField(alias="state", default=None)


class ResourceLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class SubscriptionGroupLocalizationRelationshipsSubscriptionGroupData(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["subscriptionGroups"] = _PydanticField(alias="type")


class SubscriptionGroupLocalizationRelationshipsSubscriptionGroupLinks(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class SubscriptionGroupAttributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    reference_name: typing.Optional[str] = _PydanticField(
        alias="referenceName", default=None
    )


class SubscriptionGroupRelationshipsSubscriptionGroupLocalizationsDataItem(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["subscriptionGroupLocalizations"] = _PydanticField(
        alias="type"
    )


class SubscriptionGroupRelationshipsSubscriptionGroupLocalizationsLinks(
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


class SubscriptionGroupRelationshipsSubscriptionsDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["subscriptions"] = _PydanticField(alias="type")


class SubscriptionGroupRelationshipsSubscriptionsLinks(_PydanticBaseModel):
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


class SubscriptionGroupLocalizationRelationshipsSubscriptionGroup(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        SubscriptionGroupLocalizationRelationshipsSubscriptionGroupData
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[
        SubscriptionGroupLocalizationRelationshipsSubscriptionGroupLinks
    ] = _PydanticField(alias="links", default=None)


class PagingInformation(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    paging: PagingInformationPaging = _PydanticField(alias="paging")


class SubscriptionGroupRelationshipsSubscriptions(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        typing.List[SubscriptionGroupRelationshipsSubscriptionsDataItem]
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[SubscriptionGroupRelationshipsSubscriptionsLinks] = (
        _PydanticField(alias="links", default=None)
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class SubscriptionGroupLocalizationRelationships(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    subscription_group: typing.Optional[
        SubscriptionGroupLocalizationRelationshipsSubscriptionGroup
    ] = _PydanticField(alias="subscriptionGroup", default=None)


class SubscriptionGroupRelationshipsSubscriptionGroupLocalizations(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        typing.List[
            SubscriptionGroupRelationshipsSubscriptionGroupLocalizationsDataItem
        ]
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[
        SubscriptionGroupRelationshipsSubscriptionGroupLocalizationsLinks
    ] = _PydanticField(alias="links", default=None)
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class SubscriptionGroupLocalization(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[SubscriptionGroupLocalizationAttributes] = (
        _PydanticField(alias="attributes", default=None)
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    relationships: typing.Optional[SubscriptionGroupLocalizationRelationships] = (
        _PydanticField(alias="relationships", default=None)
    )
    type: typing_extensions.Literal["subscriptionGroupLocalizations"] = _PydanticField(
        alias="type"
    )


class SubscriptionGroupRelationships(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    subscription_group_localizations: typing.Optional[
        SubscriptionGroupRelationshipsSubscriptionGroupLocalizations
    ] = _PydanticField(alias="subscriptionGroupLocalizations", default=None)
    subscriptions: typing.Optional[SubscriptionGroupRelationshipsSubscriptions] = (
        _PydanticField(alias="subscriptions", default=None)
    )


class SubscriptionGroup(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[SubscriptionGroupAttributes] = _PydanticField(
        alias="attributes", default=None
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    relationships: typing.Optional[SubscriptionGroupRelationships] = _PydanticField(
        alias="relationships", default=None
    )
    type: typing_extensions.Literal["subscriptionGroups"] = _PydanticField(alias="type")


class SubscriptionGroupLocalizationResponse(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: SubscriptionGroupLocalization = _PydanticField(alias="data")
    included: typing.Optional[typing.List[SubscriptionGroup]] = _PydanticField(
        alias="included", default=None
    )
    links: DocumentLinks = _PydanticField(alias="links")