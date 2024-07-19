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


class SubscriptionGroupAttributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    reference_name: typing.Optional[str] = _PydanticField(
        alias="referenceName", default=None
    )


class ResourceLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


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


class SubscriptionAttributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    family_sharable: typing.Optional[bool] = _PydanticField(
        alias="familySharable", default=None
    )
    group_level: typing.Optional[int] = _PydanticField(alias="groupLevel", default=None)
    name: typing.Optional[str] = _PydanticField(alias="name", default=None)
    product_id: typing.Optional[str] = _PydanticField(alias="productId", default=None)
    review_note: typing.Optional[str] = _PydanticField(alias="reviewNote", default=None)
    state: typing.Optional[
        typing_extensions.Literal[
            "MISSING_METADATA",
            "READY_TO_SUBMIT",
            "WAITING_FOR_REVIEW",
            "IN_REVIEW",
            "DEVELOPER_ACTION_NEEDED",
            "PENDING_BINARY_APPROVAL",
            "APPROVED",
            "DEVELOPER_REMOVED_FROM_SALE",
            "REMOVED_FROM_SALE",
            "REJECTED",
        ]
    ] = _PydanticField(alias="state", default=None)
    subscription_period: typing.Optional[
        typing_extensions.Literal[
            "ONE_WEEK",
            "ONE_MONTH",
            "TWO_MONTHS",
            "THREE_MONTHS",
            "SIX_MONTHS",
            "ONE_YEAR",
        ]
    ] = _PydanticField(alias="subscriptionPeriod", default=None)


class SubscriptionRelationshipsAppStoreReviewScreenshotData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["subscriptionAppStoreReviewScreenshots"] = (
        _PydanticField(alias="type")
    )


class SubscriptionRelationshipsAppStoreReviewScreenshotLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class SubscriptionRelationshipsGroupData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["subscriptionGroups"] = _PydanticField(alias="type")


class SubscriptionRelationshipsGroupLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class SubscriptionRelationshipsIntroductoryOffersDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["subscriptionIntroductoryOffers"] = _PydanticField(
        alias="type"
    )


class SubscriptionRelationshipsIntroductoryOffersLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class SubscriptionRelationshipsOfferCodesDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["subscriptionOfferCodes"] = _PydanticField(
        alias="type"
    )


class SubscriptionRelationshipsOfferCodesLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class SubscriptionRelationshipsPricesDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["subscriptionPrices"] = _PydanticField(alias="type")


class SubscriptionRelationshipsPricesLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class SubscriptionRelationshipsPromotedPurchaseData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["promotedPurchases"] = _PydanticField(alias="type")


class SubscriptionRelationshipsPromotedPurchaseLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class SubscriptionRelationshipsPromotionalOffersDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["subscriptionPromotionalOffers"] = _PydanticField(
        alias="type"
    )


class SubscriptionRelationshipsPromotionalOffersLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class SubscriptionRelationshipsSubscriptionAvailabilityData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["subscriptionAvailabilities"] = _PydanticField(
        alias="type"
    )


class SubscriptionRelationshipsSubscriptionAvailabilityLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class SubscriptionRelationshipsSubscriptionLocalizationsDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["subscriptionLocalizations"] = _PydanticField(
        alias="type"
    )


class SubscriptionRelationshipsSubscriptionLocalizationsLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


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


class PagedDocumentLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    first: typing.Optional[str] = _PydanticField(alias="first", default=None)
    next: typing.Optional[str] = _PydanticField(alias="next", default=None)
    self: str = _PydanticField(alias="self")


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


class SubscriptionRelationshipsAppStoreReviewScreenshot(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[SubscriptionRelationshipsAppStoreReviewScreenshotData] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[SubscriptionRelationshipsAppStoreReviewScreenshotLinks] = (
        _PydanticField(alias="links", default=None)
    )


class SubscriptionRelationshipsGroup(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[SubscriptionRelationshipsGroupData] = _PydanticField(
        alias="data", default=None
    )
    links: typing.Optional[SubscriptionRelationshipsGroupLinks] = _PydanticField(
        alias="links", default=None
    )


class SubscriptionRelationshipsIntroductoryOffers(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        typing.List[SubscriptionRelationshipsIntroductoryOffersDataItem]
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[SubscriptionRelationshipsIntroductoryOffersLinks] = (
        _PydanticField(alias="links", default=None)
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class SubscriptionRelationshipsOfferCodes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.List[SubscriptionRelationshipsOfferCodesDataItem]] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[SubscriptionRelationshipsOfferCodesLinks] = _PydanticField(
        alias="links", default=None
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class SubscriptionRelationshipsPrices(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.List[SubscriptionRelationshipsPricesDataItem]] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[SubscriptionRelationshipsPricesLinks] = _PydanticField(
        alias="links", default=None
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class SubscriptionRelationshipsPromotedPurchase(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[SubscriptionRelationshipsPromotedPurchaseData] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[SubscriptionRelationshipsPromotedPurchaseLinks] = (
        _PydanticField(alias="links", default=None)
    )


class SubscriptionRelationshipsPromotionalOffers(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        typing.List[SubscriptionRelationshipsPromotionalOffersDataItem]
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[SubscriptionRelationshipsPromotionalOffersLinks] = (
        _PydanticField(alias="links", default=None)
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class SubscriptionRelationshipsSubscriptionAvailability(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[SubscriptionRelationshipsSubscriptionAvailabilityData] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[SubscriptionRelationshipsSubscriptionAvailabilityLinks] = (
        _PydanticField(alias="links", default=None)
    )


class SubscriptionRelationshipsSubscriptionLocalizations(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        typing.List[SubscriptionRelationshipsSubscriptionLocalizationsDataItem]
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[SubscriptionRelationshipsSubscriptionLocalizationsLinks] = (
        _PydanticField(alias="links", default=None)
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


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


class SubscriptionRelationships(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    app_store_review_screenshot: typing.Optional[
        SubscriptionRelationshipsAppStoreReviewScreenshot
    ] = _PydanticField(alias="appStoreReviewScreenshot", default=None)
    group: typing.Optional[SubscriptionRelationshipsGroup] = _PydanticField(
        alias="group", default=None
    )
    introductory_offers: typing.Optional[
        SubscriptionRelationshipsIntroductoryOffers
    ] = _PydanticField(alias="introductoryOffers", default=None)
    offer_codes: typing.Optional[SubscriptionRelationshipsOfferCodes] = _PydanticField(
        alias="offerCodes", default=None
    )
    prices: typing.Optional[SubscriptionRelationshipsPrices] = _PydanticField(
        alias="prices", default=None
    )
    promoted_purchase: typing.Optional[SubscriptionRelationshipsPromotedPurchase] = (
        _PydanticField(alias="promotedPurchase", default=None)
    )
    promotional_offers: typing.Optional[SubscriptionRelationshipsPromotionalOffers] = (
        _PydanticField(alias="promotionalOffers", default=None)
    )
    subscription_availability: typing.Optional[
        SubscriptionRelationshipsSubscriptionAvailability
    ] = _PydanticField(alias="subscriptionAvailability", default=None)
    subscription_localizations: typing.Optional[
        SubscriptionRelationshipsSubscriptionLocalizations
    ] = _PydanticField(alias="subscriptionLocalizations", default=None)


class SubscriptionGroupLocalizationRelationships(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    subscription_group: typing.Optional[
        SubscriptionGroupLocalizationRelationshipsSubscriptionGroup
    ] = _PydanticField(alias="subscriptionGroup", default=None)


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


class Subscription(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[SubscriptionAttributes] = _PydanticField(
        alias="attributes", default=None
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    relationships: typing.Optional[SubscriptionRelationships] = _PydanticField(
        alias="relationships", default=None
    )
    type: typing_extensions.Literal["subscriptions"] = _PydanticField(alias="type")


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


class SubscriptionGroupsResponse(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.List[SubscriptionGroup] = _PydanticField(alias="data")
    included: typing.Optional[
        typing.List[typing.Union[Subscription, SubscriptionGroupLocalization]]
    ] = _PydanticField(alias="included", default=None)
    links: PagedDocumentLinks = _PydanticField(alias="links")
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )
