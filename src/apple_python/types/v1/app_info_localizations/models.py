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


class AppInfoLocalizationAttributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    locale_field: typing.Optional[str] = _PydanticField(alias="locale", default=None)
    name: typing.Optional[str] = _PydanticField(alias="name", default=None)
    privacy_choices_url: typing.Optional[str] = _PydanticField(
        alias="privacyChoicesUrl", default=None
    )
    privacy_policy_text: typing.Optional[str] = _PydanticField(
        alias="privacyPolicyText", default=None
    )
    privacy_policy_url: typing.Optional[str] = _PydanticField(
        alias="privacyPolicyUrl", default=None
    )
    subtitle: typing.Optional[str] = _PydanticField(alias="subtitle", default=None)


class ResourceLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppInfoLocalizationRelationshipsAppInfoData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["appInfos"] = _PydanticField(alias="type")


class AppInfoLocalizationRelationshipsAppInfoLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppInfoAttributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    app_store_age_rating: typing.Optional[
        typing_extensions.Literal[
            "FOUR_PLUS", "NINE_PLUS", "TWELVE_PLUS", "SEVENTEEN_PLUS", "UNRATED"
        ]
    ] = _PydanticField(alias="appStoreAgeRating", default=None)
    app_store_state: typing.Optional[
        typing_extensions.Literal[
            "ACCEPTED",
            "DEVELOPER_REMOVED_FROM_SALE",
            "DEVELOPER_REJECTED",
            "IN_REVIEW",
            "INVALID_BINARY",
            "METADATA_REJECTED",
            "PENDING_APPLE_RELEASE",
            "PENDING_CONTRACT",
            "PENDING_DEVELOPER_RELEASE",
            "PREPARE_FOR_SUBMISSION",
            "PREORDER_READY_FOR_SALE",
            "PROCESSING_FOR_APP_STORE",
            "READY_FOR_REVIEW",
            "READY_FOR_SALE",
            "REJECTED",
            "REMOVED_FROM_SALE",
            "WAITING_FOR_EXPORT_COMPLIANCE",
            "WAITING_FOR_REVIEW",
            "REPLACED_WITH_NEW_VERSION",
            "NOT_APPLICABLE",
        ]
    ] = _PydanticField(alias="appStoreState", default=None)
    brazil_age_rating: typing.Optional[
        typing_extensions.Literal[
            "L", "TEN", "TWELVE", "FOURTEEN", "SIXTEEN", "EIGHTEEN"
        ]
    ] = _PydanticField(alias="brazilAgeRating", default=None)
    brazil_age_rating_v2: typing.Optional[
        typing_extensions.Literal[
            "SELF_RATED_L",
            "SELF_RATED_TEN",
            "SELF_RATED_TWELVE",
            "SELF_RATED_FOURTEEN",
            "SELF_RATED_SIXTEEN",
            "SELF_RATED_EIGHTEEN",
            "OFFICIAL_L",
            "OFFICIAL_TEN",
            "OFFICIAL_TWELVE",
            "OFFICIAL_FOURTEEN",
            "OFFICIAL_SIXTEEN",
            "OFFICIAL_EIGHTEEN",
        ]
    ] = _PydanticField(alias="brazilAgeRatingV2", default=None)
    kids_age_band: typing.Optional[
        typing_extensions.Literal["FIVE_AND_UNDER", "SIX_TO_EIGHT", "NINE_TO_ELEVEN"]
    ] = _PydanticField(alias="kidsAgeBand", default=None)
    state: typing.Optional[
        typing_extensions.Literal[
            "ACCEPTED",
            "DEVELOPER_REJECTED",
            "IN_REVIEW",
            "PENDING_RELEASE",
            "PREPARE_FOR_SUBMISSION",
            "READY_FOR_DISTRIBUTION",
            "READY_FOR_REVIEW",
            "REJECTED",
            "REPLACED_WITH_NEW_INFO",
            "WAITING_FOR_REVIEW",
        ]
    ] = _PydanticField(alias="state", default=None)


class AppInfoRelationshipsAgeRatingDeclarationData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["ageRatingDeclarations"] = _PydanticField(
        alias="type"
    )


class AppInfoRelationshipsAgeRatingDeclarationLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppInfoRelationshipsAppData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["apps"] = _PydanticField(alias="type")


class AppInfoRelationshipsAppLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppInfoRelationshipsAppInfoLocalizationsDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["appInfoLocalizations"] = _PydanticField(
        alias="type"
    )


class AppInfoRelationshipsAppInfoLocalizationsLinks(_PydanticBaseModel):
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


class AppInfoRelationshipsPrimaryCategoryData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["appCategories"] = _PydanticField(alias="type")


class AppInfoRelationshipsPrimaryCategoryLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppInfoRelationshipsPrimarySubcategoryOneData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["appCategories"] = _PydanticField(alias="type")


class AppInfoRelationshipsPrimarySubcategoryOneLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppInfoRelationshipsPrimarySubcategoryTwoData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["appCategories"] = _PydanticField(alias="type")


class AppInfoRelationshipsPrimarySubcategoryTwoLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppInfoRelationshipsSecondaryCategoryData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["appCategories"] = _PydanticField(alias="type")


class AppInfoRelationshipsSecondaryCategoryLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppInfoRelationshipsSecondarySubcategoryOneData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["appCategories"] = _PydanticField(alias="type")


class AppInfoRelationshipsSecondarySubcategoryOneLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppInfoRelationshipsSecondarySubcategoryTwoData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["appCategories"] = _PydanticField(alias="type")


class AppInfoRelationshipsSecondarySubcategoryTwoLinks(_PydanticBaseModel):
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


class AppInfoLocalizationRelationshipsAppInfo(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[AppInfoLocalizationRelationshipsAppInfoData] = _PydanticField(
        alias="data", default=None
    )
    links: typing.Optional[AppInfoLocalizationRelationshipsAppInfoLinks] = (
        _PydanticField(alias="links", default=None)
    )


class AppInfoRelationshipsAgeRatingDeclaration(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[AppInfoRelationshipsAgeRatingDeclarationData] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[AppInfoRelationshipsAgeRatingDeclarationLinks] = (
        _PydanticField(alias="links", default=None)
    )


class AppInfoRelationshipsApp(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[AppInfoRelationshipsAppData] = _PydanticField(
        alias="data", default=None
    )
    links: typing.Optional[AppInfoRelationshipsAppLinks] = _PydanticField(
        alias="links", default=None
    )


class PagingInformation(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    paging: PagingInformationPaging = _PydanticField(alias="paging")


class AppInfoRelationshipsPrimaryCategory(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[AppInfoRelationshipsPrimaryCategoryData] = _PydanticField(
        alias="data", default=None
    )
    links: typing.Optional[AppInfoRelationshipsPrimaryCategoryLinks] = _PydanticField(
        alias="links", default=None
    )


class AppInfoRelationshipsPrimarySubcategoryOne(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[AppInfoRelationshipsPrimarySubcategoryOneData] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[AppInfoRelationshipsPrimarySubcategoryOneLinks] = (
        _PydanticField(alias="links", default=None)
    )


class AppInfoRelationshipsPrimarySubcategoryTwo(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[AppInfoRelationshipsPrimarySubcategoryTwoData] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[AppInfoRelationshipsPrimarySubcategoryTwoLinks] = (
        _PydanticField(alias="links", default=None)
    )


class AppInfoRelationshipsSecondaryCategory(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[AppInfoRelationshipsSecondaryCategoryData] = _PydanticField(
        alias="data", default=None
    )
    links: typing.Optional[AppInfoRelationshipsSecondaryCategoryLinks] = _PydanticField(
        alias="links", default=None
    )


class AppInfoRelationshipsSecondarySubcategoryOne(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[AppInfoRelationshipsSecondarySubcategoryOneData] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[AppInfoRelationshipsSecondarySubcategoryOneLinks] = (
        _PydanticField(alias="links", default=None)
    )


class AppInfoRelationshipsSecondarySubcategoryTwo(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[AppInfoRelationshipsSecondarySubcategoryTwoData] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[AppInfoRelationshipsSecondarySubcategoryTwoLinks] = (
        _PydanticField(alias="links", default=None)
    )


class AppInfoLocalizationRelationships(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    app_info: typing.Optional[AppInfoLocalizationRelationshipsAppInfo] = _PydanticField(
        alias="appInfo", default=None
    )


class AppInfoRelationshipsAppInfoLocalizations(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        typing.List[AppInfoRelationshipsAppInfoLocalizationsDataItem]
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[AppInfoRelationshipsAppInfoLocalizationsLinks] = (
        _PydanticField(alias="links", default=None)
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class AppInfoLocalization(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[AppInfoLocalizationAttributes] = _PydanticField(
        alias="attributes", default=None
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    relationships: typing.Optional[AppInfoLocalizationRelationships] = _PydanticField(
        alias="relationships", default=None
    )
    type: typing_extensions.Literal["appInfoLocalizations"] = _PydanticField(
        alias="type"
    )


class AppInfoRelationships(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    age_rating_declaration: typing.Optional[
        AppInfoRelationshipsAgeRatingDeclaration
    ] = _PydanticField(alias="ageRatingDeclaration", default=None)
    app: typing.Optional[AppInfoRelationshipsApp] = _PydanticField(
        alias="app", default=None
    )
    app_info_localizations: typing.Optional[
        AppInfoRelationshipsAppInfoLocalizations
    ] = _PydanticField(alias="appInfoLocalizations", default=None)
    primary_category: typing.Optional[AppInfoRelationshipsPrimaryCategory] = (
        _PydanticField(alias="primaryCategory", default=None)
    )
    primary_subcategory_one: typing.Optional[
        AppInfoRelationshipsPrimarySubcategoryOne
    ] = _PydanticField(alias="primarySubcategoryOne", default=None)
    primary_subcategory_two: typing.Optional[
        AppInfoRelationshipsPrimarySubcategoryTwo
    ] = _PydanticField(alias="primarySubcategoryTwo", default=None)
    secondary_category: typing.Optional[AppInfoRelationshipsSecondaryCategory] = (
        _PydanticField(alias="secondaryCategory", default=None)
    )
    secondary_subcategory_one: typing.Optional[
        AppInfoRelationshipsSecondarySubcategoryOne
    ] = _PydanticField(alias="secondarySubcategoryOne", default=None)
    secondary_subcategory_two: typing.Optional[
        AppInfoRelationshipsSecondarySubcategoryTwo
    ] = _PydanticField(alias="secondarySubcategoryTwo", default=None)


class AppInfo(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[AppInfoAttributes] = _PydanticField(
        alias="attributes", default=None
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    relationships: typing.Optional[AppInfoRelationships] = _PydanticField(
        alias="relationships", default=None
    )
    type: typing_extensions.Literal["appInfos"] = _PydanticField(alias="type")


class AppInfoLocalizationResponse(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: AppInfoLocalization = _PydanticField(alias="data")
    included: typing.Optional[typing.List[AppInfo]] = _PydanticField(
        alias="included", default=None
    )
    links: DocumentLinks = _PydanticField(alias="links")
