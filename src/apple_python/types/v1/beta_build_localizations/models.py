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


class BetaBuildLocalizationAttributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    locale_field: typing.Optional[str] = _PydanticField(alias="locale", default=None)
    whats_new: typing.Optional[str] = _PydanticField(alias="whatsNew", default=None)


class ResourceLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class BetaBuildLocalizationRelationshipsBuildData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["builds"] = _PydanticField(alias="type")


class BetaBuildLocalizationRelationshipsBuildLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class ImageAsset(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    height: typing.Optional[int] = _PydanticField(alias="height", default=None)
    template_url: typing.Optional[str] = _PydanticField(
        alias="templateUrl", default=None
    )
    width: typing.Optional[int] = _PydanticField(alias="width", default=None)


class BuildRelationshipsAppData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["apps"] = _PydanticField(alias="type")


class BuildRelationshipsAppLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class BuildRelationshipsAppEncryptionDeclarationData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["appEncryptionDeclarations"] = _PydanticField(
        alias="type"
    )


class BuildRelationshipsAppEncryptionDeclarationLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class BuildRelationshipsAppStoreVersionData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["appStoreVersions"] = _PydanticField(alias="type")


class BuildRelationshipsAppStoreVersionLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class BuildRelationshipsBetaAppReviewSubmissionData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["betaAppReviewSubmissions"] = _PydanticField(
        alias="type"
    )


class BuildRelationshipsBetaAppReviewSubmissionLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class BuildRelationshipsBetaBuildLocalizationsDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["betaBuildLocalizations"] = _PydanticField(
        alias="type"
    )


class BuildRelationshipsBetaBuildLocalizationsLinks(_PydanticBaseModel):
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


class BuildRelationshipsBetaGroupsDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["betaGroups"] = _PydanticField(alias="type")


class BuildRelationshipsBetaGroupsLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class BuildRelationshipsBuildBetaDetailData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["buildBetaDetails"] = _PydanticField(alias="type")


class BuildRelationshipsBuildBetaDetailLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class BuildRelationshipsBuildBundlesDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["buildBundles"] = _PydanticField(alias="type")


class BuildRelationshipsBuildBundlesLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class BuildRelationshipsIconsDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["buildIcons"] = _PydanticField(alias="type")


class BuildRelationshipsIconsLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class BuildRelationshipsIndividualTestersDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["betaTesters"] = _PydanticField(alias="type")


class BuildRelationshipsIndividualTestersLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class BuildRelationshipsPreReleaseVersionData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["preReleaseVersions"] = _PydanticField(alias="type")


class BuildRelationshipsPreReleaseVersionLinks(_PydanticBaseModel):
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


class BetaBuildLocalizationRelationshipsBuild(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[BetaBuildLocalizationRelationshipsBuildData] = _PydanticField(
        alias="data", default=None
    )
    links: typing.Optional[BetaBuildLocalizationRelationshipsBuildLinks] = (
        _PydanticField(alias="links", default=None)
    )


class BuildAttributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    build_audience_type: typing.Optional[
        typing_extensions.Literal["INTERNAL_ONLY", "APP_STORE_ELIGIBLE"]
    ] = _PydanticField(alias="buildAudienceType", default=None)
    computed_min_mac_os_version: typing.Optional[str] = _PydanticField(
        alias="computedMinMacOsVersion", default=None
    )
    expiration_date: typing.Optional[str] = _PydanticField(
        alias="expirationDate", default=None
    )
    expired: typing.Optional[bool] = _PydanticField(alias="expired", default=None)
    icon_asset_token: typing.Optional[ImageAsset] = _PydanticField(
        alias="iconAssetToken", default=None
    )
    ls_minimum_system_version: typing.Optional[str] = _PydanticField(
        alias="lsMinimumSystemVersion", default=None
    )
    min_os_version: typing.Optional[str] = _PydanticField(
        alias="minOsVersion", default=None
    )
    processing_state: typing.Optional[
        typing_extensions.Literal["PROCESSING", "FAILED", "INVALID", "VALID"]
    ] = _PydanticField(alias="processingState", default=None)
    uploaded_date: typing.Optional[str] = _PydanticField(
        alias="uploadedDate", default=None
    )
    uses_non_exempt_encryption: typing.Optional[bool] = _PydanticField(
        alias="usesNonExemptEncryption", default=None
    )
    version: typing.Optional[str] = _PydanticField(alias="version", default=None)


class BuildRelationshipsApp(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[BuildRelationshipsAppData] = _PydanticField(
        alias="data", default=None
    )
    links: typing.Optional[BuildRelationshipsAppLinks] = _PydanticField(
        alias="links", default=None
    )


class BuildRelationshipsAppEncryptionDeclaration(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[BuildRelationshipsAppEncryptionDeclarationData] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[BuildRelationshipsAppEncryptionDeclarationLinks] = (
        _PydanticField(alias="links", default=None)
    )


class BuildRelationshipsAppStoreVersion(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[BuildRelationshipsAppStoreVersionData] = _PydanticField(
        alias="data", default=None
    )
    links: typing.Optional[BuildRelationshipsAppStoreVersionLinks] = _PydanticField(
        alias="links", default=None
    )


class BuildRelationshipsBetaAppReviewSubmission(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[BuildRelationshipsBetaAppReviewSubmissionData] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[BuildRelationshipsBetaAppReviewSubmissionLinks] = (
        _PydanticField(alias="links", default=None)
    )


class PagingInformation(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    paging: PagingInformationPaging = _PydanticField(alias="paging")


class BuildRelationshipsBetaGroups(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.List[BuildRelationshipsBetaGroupsDataItem]] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[BuildRelationshipsBetaGroupsLinks] = _PydanticField(
        alias="links", default=None
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class BuildRelationshipsBuildBetaDetail(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[BuildRelationshipsBuildBetaDetailData] = _PydanticField(
        alias="data", default=None
    )
    links: typing.Optional[BuildRelationshipsBuildBetaDetailLinks] = _PydanticField(
        alias="links", default=None
    )


class BuildRelationshipsBuildBundles(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.List[BuildRelationshipsBuildBundlesDataItem]] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[BuildRelationshipsBuildBundlesLinks] = _PydanticField(
        alias="links", default=None
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class BuildRelationshipsIcons(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.List[BuildRelationshipsIconsDataItem]] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[BuildRelationshipsIconsLinks] = _PydanticField(
        alias="links", default=None
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class BuildRelationshipsIndividualTesters(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.List[BuildRelationshipsIndividualTestersDataItem]] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[BuildRelationshipsIndividualTestersLinks] = _PydanticField(
        alias="links", default=None
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class BuildRelationshipsPreReleaseVersion(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[BuildRelationshipsPreReleaseVersionData] = _PydanticField(
        alias="data", default=None
    )
    links: typing.Optional[BuildRelationshipsPreReleaseVersionLinks] = _PydanticField(
        alias="links", default=None
    )


class BetaBuildLocalizationRelationships(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    build: typing.Optional[BetaBuildLocalizationRelationshipsBuild] = _PydanticField(
        alias="build", default=None
    )


class BuildRelationshipsBetaBuildLocalizations(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        typing.List[BuildRelationshipsBetaBuildLocalizationsDataItem]
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[BuildRelationshipsBetaBuildLocalizationsLinks] = (
        _PydanticField(alias="links", default=None)
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class BetaBuildLocalization(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[BetaBuildLocalizationAttributes] = _PydanticField(
        alias="attributes", default=None
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    relationships: typing.Optional[BetaBuildLocalizationRelationships] = _PydanticField(
        alias="relationships", default=None
    )
    type: typing_extensions.Literal["betaBuildLocalizations"] = _PydanticField(
        alias="type"
    )


class BuildRelationships(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    app: typing.Optional[BuildRelationshipsApp] = _PydanticField(
        alias="app", default=None
    )
    app_encryption_declaration: typing.Optional[
        BuildRelationshipsAppEncryptionDeclaration
    ] = _PydanticField(alias="appEncryptionDeclaration", default=None)
    app_store_version: typing.Optional[BuildRelationshipsAppStoreVersion] = (
        _PydanticField(alias="appStoreVersion", default=None)
    )
    beta_app_review_submission: typing.Optional[
        BuildRelationshipsBetaAppReviewSubmission
    ] = _PydanticField(alias="betaAppReviewSubmission", default=None)
    beta_build_localizations: typing.Optional[
        BuildRelationshipsBetaBuildLocalizations
    ] = _PydanticField(alias="betaBuildLocalizations", default=None)
    beta_groups: typing.Optional[BuildRelationshipsBetaGroups] = _PydanticField(
        alias="betaGroups", default=None
    )
    build_beta_detail: typing.Optional[BuildRelationshipsBuildBetaDetail] = (
        _PydanticField(alias="buildBetaDetail", default=None)
    )
    build_bundles: typing.Optional[BuildRelationshipsBuildBundles] = _PydanticField(
        alias="buildBundles", default=None
    )
    icons: typing.Optional[BuildRelationshipsIcons] = _PydanticField(
        alias="icons", default=None
    )
    individual_testers: typing.Optional[BuildRelationshipsIndividualTesters] = (
        _PydanticField(alias="individualTesters", default=None)
    )
    pre_release_version: typing.Optional[BuildRelationshipsPreReleaseVersion] = (
        _PydanticField(alias="preReleaseVersion", default=None)
    )


class Build(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[BuildAttributes] = _PydanticField(
        alias="attributes", default=None
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    relationships: typing.Optional[BuildRelationships] = _PydanticField(
        alias="relationships", default=None
    )
    type: typing_extensions.Literal["builds"] = _PydanticField(alias="type")


class BetaBuildLocalizationResponse(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: BetaBuildLocalization = _PydanticField(alias="data")
    included: typing.Optional[typing.List[Build]] = _PydanticField(
        alias="included", default=None
    )
    links: DocumentLinks = _PydanticField(alias="links")


class BetaBuildLocalizationsResponse(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.List[BetaBuildLocalization] = _PydanticField(alias="data")
    included: typing.Optional[typing.List[Build]] = _PydanticField(
        alias="included", default=None
    )
    links: PagedDocumentLinks = _PydanticField(alias="links")
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )
