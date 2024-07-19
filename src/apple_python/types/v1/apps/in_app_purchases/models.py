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


class InAppPurchaseAttributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    in_app_purchase_type: typing.Optional[
        typing_extensions.Literal[
            "AUTOMATICALLY_RENEWABLE_SUBSCRIPTION",
            "NON_CONSUMABLE",
            "CONSUMABLE",
            "NON_RENEWING_SUBSCRIPTION",
            "FREE_SUBSCRIPTION",
        ]
    ] = _PydanticField(alias="inAppPurchaseType", default=None)
    product_id: typing.Optional[str] = _PydanticField(alias="productId", default=None)
    reference_name: typing.Optional[str] = _PydanticField(
        alias="referenceName", default=None
    )
    state: typing.Optional[
        typing_extensions.Literal[
            "CREATED",
            "DEVELOPER_SIGNED_OFF",
            "DEVELOPER_ACTION_NEEDED",
            "DELETION_IN_PROGRESS",
            "APPROVED",
            "DELETED",
            "REMOVED_FROM_SALE",
            "DEVELOPER_REMOVED_FROM_SALE",
            "WAITING_FOR_UPLOAD",
            "PROCESSING_CONTENT",
            "REPLACED",
            "REJECTED",
            "WAITING_FOR_SCREENSHOT",
            "PREPARE_FOR_SUBMISSION",
            "MISSING_METADATA",
            "READY_TO_SUBMIT",
            "WAITING_FOR_REVIEW",
            "IN_REVIEW",
            "PENDING_DEVELOPER_RELEASE",
        ]
    ] = _PydanticField(alias="state", default=None)


class ResourceLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class InAppPurchaseRelationshipsAppsDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["apps"] = _PydanticField(alias="type")


class InAppPurchaseRelationshipsAppsLinks(_PydanticBaseModel):
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


class AppAttributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    bundle_id: typing.Optional[str] = _PydanticField(alias="bundleId", default=None)
    content_rights_declaration: typing.Optional[
        typing_extensions.Literal[
            "DOES_NOT_USE_THIRD_PARTY_CONTENT", "USES_THIRD_PARTY_CONTENT"
        ]
    ] = _PydanticField(alias="contentRightsDeclaration", default=None)
    is_or_ever_was_made_for_kids: typing.Optional[bool] = _PydanticField(
        alias="isOrEverWasMadeForKids", default=None
    )
    name: typing.Optional[str] = _PydanticField(alias="name", default=None)
    primary_locale: typing.Optional[str] = _PydanticField(
        alias="primaryLocale", default=None
    )
    sku: typing.Optional[str] = _PydanticField(alias="sku", default=None)
    subscription_status_url: typing.Optional[str] = _PydanticField(
        alias="subscriptionStatusUrl", default=None
    )
    subscription_status_url_for_sandbox: typing.Optional[str] = _PydanticField(
        alias="subscriptionStatusUrlForSandbox", default=None
    )
    subscription_status_url_version: typing.Optional[
        typing_extensions.Literal["V1", "V2", "v1", "v2"]
    ] = _PydanticField(alias="subscriptionStatusUrlVersion", default=None)
    subscription_status_url_version_for_sandbox: typing.Optional[
        typing_extensions.Literal["V1", "V2", "v1", "v2"]
    ] = _PydanticField(alias="subscriptionStatusUrlVersionForSandbox", default=None)


class AppRelationshipsAppClipsDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["appClips"] = _PydanticField(alias="type")


class AppRelationshipsAppClipsLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppRelationshipsAppCustomProductPagesDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["appCustomProductPages"] = _PydanticField(
        alias="type"
    )


class AppRelationshipsAppCustomProductPagesLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppRelationshipsAppEncryptionDeclarationsDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["appEncryptionDeclarations"] = _PydanticField(
        alias="type"
    )


class AppRelationshipsAppEncryptionDeclarationsLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppRelationshipsAppEventsDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["appEvents"] = _PydanticField(alias="type")


class AppRelationshipsAppEventsLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppRelationshipsAppInfosDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["appInfos"] = _PydanticField(alias="type")


class AppRelationshipsAppInfosLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppRelationshipsAppStoreVersionExperimentsV2DataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["appStoreVersionExperiments"] = _PydanticField(
        alias="type"
    )


class AppRelationshipsAppStoreVersionExperimentsV2Links(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppRelationshipsAppStoreVersionsDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["appStoreVersions"] = _PydanticField(alias="type")


class AppRelationshipsAppStoreVersionsLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppRelationshipsBetaAppLocalizationsDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["betaAppLocalizations"] = _PydanticField(
        alias="type"
    )


class AppRelationshipsBetaAppLocalizationsLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppRelationshipsBetaAppReviewDetailData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["betaAppReviewDetails"] = _PydanticField(
        alias="type"
    )


class AppRelationshipsBetaAppReviewDetailLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppRelationshipsBetaGroupsDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["betaGroups"] = _PydanticField(alias="type")


class AppRelationshipsBetaGroupsLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppRelationshipsBetaLicenseAgreementData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["betaLicenseAgreements"] = _PydanticField(
        alias="type"
    )


class AppRelationshipsBetaLicenseAgreementLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppRelationshipsBuildsDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["builds"] = _PydanticField(alias="type")


class AppRelationshipsBuildsLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppRelationshipsCiProductData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["ciProducts"] = _PydanticField(alias="type")


class AppRelationshipsCiProductLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppRelationshipsEndUserLicenseAgreementData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["endUserLicenseAgreements"] = _PydanticField(
        alias="type"
    )


class AppRelationshipsEndUserLicenseAgreementLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppRelationshipsGameCenterDetailData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["gameCenterDetails"] = _PydanticField(alias="type")


class AppRelationshipsGameCenterDetailLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppRelationshipsGameCenterEnabledVersionsDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["gameCenterEnabledVersions"] = _PydanticField(
        alias="type"
    )


class AppRelationshipsGameCenterEnabledVersionsLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppRelationshipsInAppPurchasesDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["inAppPurchases"] = _PydanticField(alias="type")


class AppRelationshipsInAppPurchasesLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppRelationshipsInAppPurchasesV2DataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["inAppPurchases"] = _PydanticField(alias="type")


class AppRelationshipsInAppPurchasesV2Links(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppRelationshipsPreOrderData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["appPreOrders"] = _PydanticField(alias="type")


class AppRelationshipsPreOrderLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppRelationshipsPreReleaseVersionsDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["preReleaseVersions"] = _PydanticField(alias="type")


class AppRelationshipsPreReleaseVersionsLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppRelationshipsPromotedPurchasesDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["promotedPurchases"] = _PydanticField(alias="type")


class AppRelationshipsPromotedPurchasesLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppRelationshipsReviewSubmissionsDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["reviewSubmissions"] = _PydanticField(alias="type")


class AppRelationshipsReviewSubmissionsLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppRelationshipsSubscriptionGracePeriodData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["subscriptionGracePeriods"] = _PydanticField(
        alias="type"
    )


class AppRelationshipsSubscriptionGracePeriodLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppRelationshipsSubscriptionGroupsDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["subscriptionGroups"] = _PydanticField(alias="type")


class AppRelationshipsSubscriptionGroupsLinks(_PydanticBaseModel):
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


class AppRelationshipsAppClips(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.List[AppRelationshipsAppClipsDataItem]] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[AppRelationshipsAppClipsLinks] = _PydanticField(
        alias="links", default=None
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class AppRelationshipsAppCustomProductPages(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        typing.List[AppRelationshipsAppCustomProductPagesDataItem]
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[AppRelationshipsAppCustomProductPagesLinks] = _PydanticField(
        alias="links", default=None
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class AppRelationshipsAppEncryptionDeclarations(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        typing.List[AppRelationshipsAppEncryptionDeclarationsDataItem]
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[AppRelationshipsAppEncryptionDeclarationsLinks] = (
        _PydanticField(alias="links", default=None)
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class AppRelationshipsAppEvents(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.List[AppRelationshipsAppEventsDataItem]] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[AppRelationshipsAppEventsLinks] = _PydanticField(
        alias="links", default=None
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class AppRelationshipsAppInfos(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.List[AppRelationshipsAppInfosDataItem]] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[AppRelationshipsAppInfosLinks] = _PydanticField(
        alias="links", default=None
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class AppRelationshipsAppStoreVersionExperimentsV2(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        typing.List[AppRelationshipsAppStoreVersionExperimentsV2DataItem]
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[AppRelationshipsAppStoreVersionExperimentsV2Links] = (
        _PydanticField(alias="links", default=None)
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class AppRelationshipsAppStoreVersions(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.List[AppRelationshipsAppStoreVersionsDataItem]] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[AppRelationshipsAppStoreVersionsLinks] = _PydanticField(
        alias="links", default=None
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class AppRelationshipsBetaAppLocalizations(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.List[AppRelationshipsBetaAppLocalizationsDataItem]] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[AppRelationshipsBetaAppLocalizationsLinks] = _PydanticField(
        alias="links", default=None
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class AppRelationshipsBetaAppReviewDetail(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[AppRelationshipsBetaAppReviewDetailData] = _PydanticField(
        alias="data", default=None
    )
    links: typing.Optional[AppRelationshipsBetaAppReviewDetailLinks] = _PydanticField(
        alias="links", default=None
    )


class AppRelationshipsBetaGroups(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.List[AppRelationshipsBetaGroupsDataItem]] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[AppRelationshipsBetaGroupsLinks] = _PydanticField(
        alias="links", default=None
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class AppRelationshipsBetaLicenseAgreement(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[AppRelationshipsBetaLicenseAgreementData] = _PydanticField(
        alias="data", default=None
    )
    links: typing.Optional[AppRelationshipsBetaLicenseAgreementLinks] = _PydanticField(
        alias="links", default=None
    )


class AppRelationshipsBuilds(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.List[AppRelationshipsBuildsDataItem]] = _PydanticField(
        alias="data", default=None
    )
    links: typing.Optional[AppRelationshipsBuildsLinks] = _PydanticField(
        alias="links", default=None
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class AppRelationshipsCiProduct(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[AppRelationshipsCiProductData] = _PydanticField(
        alias="data", default=None
    )
    links: typing.Optional[AppRelationshipsCiProductLinks] = _PydanticField(
        alias="links", default=None
    )


class AppRelationshipsEndUserLicenseAgreement(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[AppRelationshipsEndUserLicenseAgreementData] = _PydanticField(
        alias="data", default=None
    )
    links: typing.Optional[AppRelationshipsEndUserLicenseAgreementLinks] = (
        _PydanticField(alias="links", default=None)
    )


class AppRelationshipsGameCenterDetail(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[AppRelationshipsGameCenterDetailData] = _PydanticField(
        alias="data", default=None
    )
    links: typing.Optional[AppRelationshipsGameCenterDetailLinks] = _PydanticField(
        alias="links", default=None
    )


class AppRelationshipsGameCenterEnabledVersions(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        typing.List[AppRelationshipsGameCenterEnabledVersionsDataItem]
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[AppRelationshipsGameCenterEnabledVersionsLinks] = (
        _PydanticField(alias="links", default=None)
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class AppRelationshipsInAppPurchases(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.List[AppRelationshipsInAppPurchasesDataItem]] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[AppRelationshipsInAppPurchasesLinks] = _PydanticField(
        alias="links", default=None
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class AppRelationshipsInAppPurchasesV2(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.List[AppRelationshipsInAppPurchasesV2DataItem]] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[AppRelationshipsInAppPurchasesV2Links] = _PydanticField(
        alias="links", default=None
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class AppRelationshipsPreOrder(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[AppRelationshipsPreOrderData] = _PydanticField(
        alias="data", default=None
    )
    links: typing.Optional[AppRelationshipsPreOrderLinks] = _PydanticField(
        alias="links", default=None
    )


class AppRelationshipsPreReleaseVersions(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.List[AppRelationshipsPreReleaseVersionsDataItem]] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[AppRelationshipsPreReleaseVersionsLinks] = _PydanticField(
        alias="links", default=None
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class AppRelationshipsPromotedPurchases(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.List[AppRelationshipsPromotedPurchasesDataItem]] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[AppRelationshipsPromotedPurchasesLinks] = _PydanticField(
        alias="links", default=None
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class AppRelationshipsReviewSubmissions(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.List[AppRelationshipsReviewSubmissionsDataItem]] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[AppRelationshipsReviewSubmissionsLinks] = _PydanticField(
        alias="links", default=None
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class AppRelationshipsSubscriptionGracePeriod(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[AppRelationshipsSubscriptionGracePeriodData] = _PydanticField(
        alias="data", default=None
    )
    links: typing.Optional[AppRelationshipsSubscriptionGracePeriodLinks] = (
        _PydanticField(alias="links", default=None)
    )


class AppRelationshipsSubscriptionGroups(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.List[AppRelationshipsSubscriptionGroupsDataItem]] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[AppRelationshipsSubscriptionGroupsLinks] = _PydanticField(
        alias="links", default=None
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class InAppPurchaseRelationshipsApps(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.List[InAppPurchaseRelationshipsAppsDataItem]] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[InAppPurchaseRelationshipsAppsLinks] = _PydanticField(
        alias="links", default=None
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class AppRelationships(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    app_clips: typing.Optional[AppRelationshipsAppClips] = _PydanticField(
        alias="appClips", default=None
    )
    app_custom_product_pages: typing.Optional[AppRelationshipsAppCustomProductPages] = (
        _PydanticField(alias="appCustomProductPages", default=None)
    )
    app_encryption_declarations: typing.Optional[
        AppRelationshipsAppEncryptionDeclarations
    ] = _PydanticField(alias="appEncryptionDeclarations", default=None)
    app_events: typing.Optional[AppRelationshipsAppEvents] = _PydanticField(
        alias="appEvents", default=None
    )
    app_infos: typing.Optional[AppRelationshipsAppInfos] = _PydanticField(
        alias="appInfos", default=None
    )
    app_store_version_experiments_v2: typing.Optional[
        AppRelationshipsAppStoreVersionExperimentsV2
    ] = _PydanticField(alias="appStoreVersionExperimentsV2", default=None)
    app_store_versions: typing.Optional[AppRelationshipsAppStoreVersions] = (
        _PydanticField(alias="appStoreVersions", default=None)
    )
    beta_app_localizations: typing.Optional[AppRelationshipsBetaAppLocalizations] = (
        _PydanticField(alias="betaAppLocalizations", default=None)
    )
    beta_app_review_detail: typing.Optional[AppRelationshipsBetaAppReviewDetail] = (
        _PydanticField(alias="betaAppReviewDetail", default=None)
    )
    beta_groups: typing.Optional[AppRelationshipsBetaGroups] = _PydanticField(
        alias="betaGroups", default=None
    )
    beta_license_agreement: typing.Optional[AppRelationshipsBetaLicenseAgreement] = (
        _PydanticField(alias="betaLicenseAgreement", default=None)
    )
    builds: typing.Optional[AppRelationshipsBuilds] = _PydanticField(
        alias="builds", default=None
    )
    ci_product: typing.Optional[AppRelationshipsCiProduct] = _PydanticField(
        alias="ciProduct", default=None
    )
    end_user_license_agreement: typing.Optional[
        AppRelationshipsEndUserLicenseAgreement
    ] = _PydanticField(alias="endUserLicenseAgreement", default=None)
    game_center_detail: typing.Optional[AppRelationshipsGameCenterDetail] = (
        _PydanticField(alias="gameCenterDetail", default=None)
    )
    game_center_enabled_versions: typing.Optional[
        AppRelationshipsGameCenterEnabledVersions
    ] = _PydanticField(alias="gameCenterEnabledVersions", default=None)
    in_app_purchases: typing.Optional[AppRelationshipsInAppPurchases] = _PydanticField(
        alias="inAppPurchases", default=None
    )
    in_app_purchases_v2: typing.Optional[AppRelationshipsInAppPurchasesV2] = (
        _PydanticField(alias="inAppPurchasesV2", default=None)
    )
    pre_order: typing.Optional[AppRelationshipsPreOrder] = _PydanticField(
        alias="preOrder", default=None
    )
    pre_release_versions: typing.Optional[AppRelationshipsPreReleaseVersions] = (
        _PydanticField(alias="preReleaseVersions", default=None)
    )
    promoted_purchases: typing.Optional[AppRelationshipsPromotedPurchases] = (
        _PydanticField(alias="promotedPurchases", default=None)
    )
    review_submissions: typing.Optional[AppRelationshipsReviewSubmissions] = (
        _PydanticField(alias="reviewSubmissions", default=None)
    )
    subscription_grace_period: typing.Optional[
        AppRelationshipsSubscriptionGracePeriod
    ] = _PydanticField(alias="subscriptionGracePeriod", default=None)
    subscription_groups: typing.Optional[AppRelationshipsSubscriptionGroups] = (
        _PydanticField(alias="subscriptionGroups", default=None)
    )


class InAppPurchaseRelationships(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    apps: typing.Optional[InAppPurchaseRelationshipsApps] = _PydanticField(
        alias="apps", default=None
    )


class App(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[AppAttributes] = _PydanticField(
        alias="attributes", default=None
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    relationships: typing.Optional[AppRelationships] = _PydanticField(
        alias="relationships", default=None
    )
    type: typing_extensions.Literal["apps"] = _PydanticField(alias="type")


class InAppPurchase(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[InAppPurchaseAttributes] = _PydanticField(
        alias="attributes", default=None
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    relationships: typing.Optional[InAppPurchaseRelationships] = _PydanticField(
        alias="relationships", default=None
    )
    type: typing_extensions.Literal["inAppPurchases"] = _PydanticField(alias="type")


class InAppPurchasesResponse(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.List[InAppPurchase] = _PydanticField(alias="data")
    included: typing.Optional[typing.List[App]] = _PydanticField(
        alias="included", default=None
    )
    links: PagedDocumentLinks = _PydanticField(alias="links")
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )
