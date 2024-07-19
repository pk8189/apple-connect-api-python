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


class AppScreenshotSetAttributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    screenshot_display_type: typing.Optional[
        typing_extensions.Literal[
            "APP_IPHONE_67",
            "APP_IPHONE_61",
            "APP_IPHONE_65",
            "APP_IPHONE_58",
            "APP_IPHONE_55",
            "APP_IPHONE_47",
            "APP_IPHONE_40",
            "APP_IPHONE_35",
            "APP_IPAD_PRO_3GEN_129",
            "APP_IPAD_PRO_3GEN_11",
            "APP_IPAD_PRO_129",
            "APP_IPAD_105",
            "APP_IPAD_97",
            "APP_DESKTOP",
            "APP_WATCH_ULTRA",
            "APP_WATCH_SERIES_7",
            "APP_WATCH_SERIES_4",
            "APP_WATCH_SERIES_3",
            "APP_APPLE_TV",
            "APP_APPLE_VISION_PRO",
            "IMESSAGE_APP_IPHONE_67",
            "IMESSAGE_APP_IPHONE_61",
            "IMESSAGE_APP_IPHONE_65",
            "IMESSAGE_APP_IPHONE_58",
            "IMESSAGE_APP_IPHONE_55",
            "IMESSAGE_APP_IPHONE_47",
            "IMESSAGE_APP_IPHONE_40",
            "IMESSAGE_APP_IPAD_PRO_3GEN_129",
            "IMESSAGE_APP_IPAD_PRO_3GEN_11",
            "IMESSAGE_APP_IPAD_PRO_129",
            "IMESSAGE_APP_IPAD_105",
            "IMESSAGE_APP_IPAD_97",
        ]
    ] = _PydanticField(alias="screenshotDisplayType", default=None)


class ResourceLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppScreenshotSetRelationshipsAppCustomProductPageLocalizationData(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["appCustomProductPageLocalizations"] = (
        _PydanticField(alias="type")
    )


class AppScreenshotSetRelationshipsAppCustomProductPageLocalizationLinks(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppScreenshotSetRelationshipsAppScreenshotsDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["appScreenshots"] = _PydanticField(alias="type")


class AppScreenshotSetRelationshipsAppScreenshotsLinks(_PydanticBaseModel):
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


class AppScreenshotSetRelationshipsAppStoreVersionExperimentTreatmentLocalizationData(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal[
        "appStoreVersionExperimentTreatmentLocalizations"
    ] = _PydanticField(alias="type")


class AppScreenshotSetRelationshipsAppStoreVersionExperimentTreatmentLocalizationLinks(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppScreenshotSetRelationshipsAppStoreVersionLocalizationData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["appStoreVersionLocalizations"] = _PydanticField(
        alias="type"
    )


class AppScreenshotSetRelationshipsAppStoreVersionLocalizationLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppStoreVersionLocalizationAttributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    description: typing.Optional[str] = _PydanticField(
        alias="description", default=None
    )
    keywords: typing.Optional[str] = _PydanticField(alias="keywords", default=None)
    locale_field: typing.Optional[str] = _PydanticField(alias="locale", default=None)
    marketing_url: typing.Optional[str] = _PydanticField(
        alias="marketingUrl", default=None
    )
    promotional_text: typing.Optional[str] = _PydanticField(
        alias="promotionalText", default=None
    )
    support_url: typing.Optional[str] = _PydanticField(alias="supportUrl", default=None)
    whats_new: typing.Optional[str] = _PydanticField(alias="whatsNew", default=None)


class AppStoreVersionLocalizationRelationshipsAppPreviewSetsDataItem(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["appPreviewSets"] = _PydanticField(alias="type")


class AppStoreVersionLocalizationRelationshipsAppPreviewSetsLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppStoreVersionLocalizationRelationshipsAppScreenshotSetsDataItem(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["appScreenshotSets"] = _PydanticField(alias="type")


class AppStoreVersionLocalizationRelationshipsAppScreenshotSetsLinks(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppStoreVersionLocalizationRelationshipsAppStoreVersionData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["appStoreVersions"] = _PydanticField(alias="type")


class AppStoreVersionLocalizationRelationshipsAppStoreVersionLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppCustomProductPageLocalizationAttributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    locale_field: typing.Optional[str] = _PydanticField(alias="locale", default=None)
    promotional_text: typing.Optional[str] = _PydanticField(
        alias="promotionalText", default=None
    )


class AppCustomProductPageLocalizationRelationshipsAppCustomProductPageVersionData(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["appCustomProductPageVersions"] = _PydanticField(
        alias="type"
    )


class AppCustomProductPageLocalizationRelationshipsAppCustomProductPageVersionLinks(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppCustomProductPageLocalizationRelationshipsAppPreviewSetsDataItem(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["appPreviewSets"] = _PydanticField(alias="type")


class AppCustomProductPageLocalizationRelationshipsAppPreviewSetsLinks(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppCustomProductPageLocalizationRelationshipsAppScreenshotSetsDataItem(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["appScreenshotSets"] = _PydanticField(alias="type")


class AppCustomProductPageLocalizationRelationshipsAppScreenshotSetsLinks(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppStoreVersionExperimentTreatmentLocalizationAttributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    locale_field: typing.Optional[str] = _PydanticField(alias="locale", default=None)


class AppStoreVersionExperimentTreatmentLocalizationRelationshipsAppPreviewSetsDataItem(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["appPreviewSets"] = _PydanticField(alias="type")


class AppStoreVersionExperimentTreatmentLocalizationRelationshipsAppPreviewSetsLinks(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppStoreVersionExperimentTreatmentLocalizationRelationshipsAppScreenshotSetsDataItem(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["appScreenshotSets"] = _PydanticField(alias="type")


class AppStoreVersionExperimentTreatmentLocalizationRelationshipsAppScreenshotSetsLinks(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppStoreVersionExperimentTreatmentLocalizationRelationshipsAppStoreVersionExperimentTreatmentData(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["appStoreVersionExperimentTreatments"] = (
        _PydanticField(alias="type")
    )


class AppStoreVersionExperimentTreatmentLocalizationRelationshipsAppStoreVersionExperimentTreatmentLinks(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppMediaStateError(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    code_field: typing.Optional[str] = _PydanticField(alias="code", default=None)
    description: typing.Optional[str] = _PydanticField(
        alias="description", default=None
    )


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


class HttpHeader(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    name: typing.Optional[str] = _PydanticField(alias="name", default=None)
    value: typing.Optional[str] = _PydanticField(alias="value", default=None)


class AppScreenshotRelationshipsAppScreenshotSetData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["appScreenshotSets"] = _PydanticField(alias="type")


class AppScreenshotRelationshipsAppScreenshotSetLinks(_PydanticBaseModel):
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


class AppScreenshotSetRelationshipsAppCustomProductPageLocalization(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        AppScreenshotSetRelationshipsAppCustomProductPageLocalizationData
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[
        AppScreenshotSetRelationshipsAppCustomProductPageLocalizationLinks
    ] = _PydanticField(alias="links", default=None)


class PagingInformation(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    paging: PagingInformationPaging = _PydanticField(alias="paging")


class AppScreenshotSetRelationshipsAppStoreVersionExperimentTreatmentLocalization(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        AppScreenshotSetRelationshipsAppStoreVersionExperimentTreatmentLocalizationData
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[
        AppScreenshotSetRelationshipsAppStoreVersionExperimentTreatmentLocalizationLinks
    ] = _PydanticField(alias="links", default=None)


class AppScreenshotSetRelationshipsAppStoreVersionLocalization(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        AppScreenshotSetRelationshipsAppStoreVersionLocalizationData
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[
        AppScreenshotSetRelationshipsAppStoreVersionLocalizationLinks
    ] = _PydanticField(alias="links", default=None)


class AppStoreVersionLocalizationRelationshipsAppPreviewSets(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        typing.List[AppStoreVersionLocalizationRelationshipsAppPreviewSetsDataItem]
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[
        AppStoreVersionLocalizationRelationshipsAppPreviewSetsLinks
    ] = _PydanticField(alias="links", default=None)
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class AppStoreVersionLocalizationRelationshipsAppScreenshotSets(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        typing.List[AppStoreVersionLocalizationRelationshipsAppScreenshotSetsDataItem]
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[
        AppStoreVersionLocalizationRelationshipsAppScreenshotSetsLinks
    ] = _PydanticField(alias="links", default=None)
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class AppStoreVersionLocalizationRelationshipsAppStoreVersion(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        AppStoreVersionLocalizationRelationshipsAppStoreVersionData
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[
        AppStoreVersionLocalizationRelationshipsAppStoreVersionLinks
    ] = _PydanticField(alias="links", default=None)


class AppCustomProductPageLocalizationRelationshipsAppCustomProductPageVersion(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        AppCustomProductPageLocalizationRelationshipsAppCustomProductPageVersionData
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[
        AppCustomProductPageLocalizationRelationshipsAppCustomProductPageVersionLinks
    ] = _PydanticField(alias="links", default=None)


class AppCustomProductPageLocalizationRelationshipsAppPreviewSets(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        typing.List[AppCustomProductPageLocalizationRelationshipsAppPreviewSetsDataItem]
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[
        AppCustomProductPageLocalizationRelationshipsAppPreviewSetsLinks
    ] = _PydanticField(alias="links", default=None)
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class AppCustomProductPageLocalizationRelationshipsAppScreenshotSets(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        typing.List[
            AppCustomProductPageLocalizationRelationshipsAppScreenshotSetsDataItem
        ]
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[
        AppCustomProductPageLocalizationRelationshipsAppScreenshotSetsLinks
    ] = _PydanticField(alias="links", default=None)
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class AppStoreVersionExperimentTreatmentLocalizationRelationshipsAppPreviewSets(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        typing.List[
            AppStoreVersionExperimentTreatmentLocalizationRelationshipsAppPreviewSetsDataItem
        ]
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[
        AppStoreVersionExperimentTreatmentLocalizationRelationshipsAppPreviewSetsLinks
    ] = _PydanticField(alias="links", default=None)
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class AppStoreVersionExperimentTreatmentLocalizationRelationshipsAppScreenshotSets(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        typing.List[
            AppStoreVersionExperimentTreatmentLocalizationRelationshipsAppScreenshotSetsDataItem
        ]
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[
        AppStoreVersionExperimentTreatmentLocalizationRelationshipsAppScreenshotSetsLinks
    ] = _PydanticField(alias="links", default=None)
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class AppStoreVersionExperimentTreatmentLocalizationRelationshipsAppStoreVersionExperimentTreatment(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        AppStoreVersionExperimentTreatmentLocalizationRelationshipsAppStoreVersionExperimentTreatmentData
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[
        AppStoreVersionExperimentTreatmentLocalizationRelationshipsAppStoreVersionExperimentTreatmentLinks
    ] = _PydanticField(alias="links", default=None)


class AppMediaAssetState(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    errors: typing.Optional[typing.List[AppMediaStateError]] = _PydanticField(
        alias="errors", default=None
    )
    state: typing.Optional[
        typing_extensions.Literal[
            "AWAITING_UPLOAD", "UPLOAD_COMPLETE", "COMPLETE", "FAILED"
        ]
    ] = _PydanticField(alias="state", default=None)
    warnings_field: typing.Optional[typing.List[AppMediaStateError]] = _PydanticField(
        alias="warnings", default=None
    )


class UploadOperation(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    length: typing.Optional[int] = _PydanticField(alias="length", default=None)
    method: typing.Optional[str] = _PydanticField(alias="method", default=None)
    offset: typing.Optional[int] = _PydanticField(alias="offset", default=None)
    request_headers: typing.Optional[typing.List[HttpHeader]] = _PydanticField(
        alias="requestHeaders", default=None
    )
    url: typing.Optional[str] = _PydanticField(alias="url", default=None)


class AppScreenshotRelationshipsAppScreenshotSet(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[AppScreenshotRelationshipsAppScreenshotSetData] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[AppScreenshotRelationshipsAppScreenshotSetLinks] = (
        _PydanticField(alias="links", default=None)
    )


class AppScreenshotSetRelationshipsAppScreenshots(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        typing.List[AppScreenshotSetRelationshipsAppScreenshotsDataItem]
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[AppScreenshotSetRelationshipsAppScreenshotsLinks] = (
        _PydanticField(alias="links", default=None)
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class AppStoreVersionLocalizationRelationships(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    app_preview_sets: typing.Optional[
        AppStoreVersionLocalizationRelationshipsAppPreviewSets
    ] = _PydanticField(alias="appPreviewSets", default=None)
    app_screenshot_sets: typing.Optional[
        AppStoreVersionLocalizationRelationshipsAppScreenshotSets
    ] = _PydanticField(alias="appScreenshotSets", default=None)
    app_store_version: typing.Optional[
        AppStoreVersionLocalizationRelationshipsAppStoreVersion
    ] = _PydanticField(alias="appStoreVersion", default=None)


class AppCustomProductPageLocalizationRelationships(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    app_custom_product_page_version: typing.Optional[
        AppCustomProductPageLocalizationRelationshipsAppCustomProductPageVersion
    ] = _PydanticField(alias="appCustomProductPageVersion", default=None)
    app_preview_sets: typing.Optional[
        AppCustomProductPageLocalizationRelationshipsAppPreviewSets
    ] = _PydanticField(alias="appPreviewSets", default=None)
    app_screenshot_sets: typing.Optional[
        AppCustomProductPageLocalizationRelationshipsAppScreenshotSets
    ] = _PydanticField(alias="appScreenshotSets", default=None)


class AppStoreVersionExperimentTreatmentLocalizationRelationships(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    app_preview_sets: typing.Optional[
        AppStoreVersionExperimentTreatmentLocalizationRelationshipsAppPreviewSets
    ] = _PydanticField(alias="appPreviewSets", default=None)
    app_screenshot_sets: typing.Optional[
        AppStoreVersionExperimentTreatmentLocalizationRelationshipsAppScreenshotSets
    ] = _PydanticField(alias="appScreenshotSets", default=None)
    app_store_version_experiment_treatment: typing.Optional[
        AppStoreVersionExperimentTreatmentLocalizationRelationshipsAppStoreVersionExperimentTreatment
    ] = _PydanticField(alias="appStoreVersionExperimentTreatment", default=None)


class AppScreenshotAttributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    asset_delivery_state: typing.Optional[AppMediaAssetState] = _PydanticField(
        alias="assetDeliveryState", default=None
    )
    asset_token: typing.Optional[str] = _PydanticField(alias="assetToken", default=None)
    asset_type: typing.Optional[str] = _PydanticField(alias="assetType", default=None)
    file_name: typing.Optional[str] = _PydanticField(alias="fileName", default=None)
    file_size: typing.Optional[int] = _PydanticField(alias="fileSize", default=None)
    image_asset: typing.Optional[ImageAsset] = _PydanticField(
        alias="imageAsset", default=None
    )
    source_file_checksum: typing.Optional[str] = _PydanticField(
        alias="sourceFileChecksum", default=None
    )
    upload_operations: typing.Optional[typing.List[UploadOperation]] = _PydanticField(
        alias="uploadOperations", default=None
    )


class AppScreenshotRelationships(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    app_screenshot_set: typing.Optional[AppScreenshotRelationshipsAppScreenshotSet] = (
        _PydanticField(alias="appScreenshotSet", default=None)
    )


class AppScreenshotSetRelationships(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    app_custom_product_page_localization: typing.Optional[
        AppScreenshotSetRelationshipsAppCustomProductPageLocalization
    ] = _PydanticField(alias="appCustomProductPageLocalization", default=None)
    app_screenshots: typing.Optional[AppScreenshotSetRelationshipsAppScreenshots] = (
        _PydanticField(alias="appScreenshots", default=None)
    )
    app_store_version_experiment_treatment_localization: typing.Optional[
        AppScreenshotSetRelationshipsAppStoreVersionExperimentTreatmentLocalization
    ] = _PydanticField(
        alias="appStoreVersionExperimentTreatmentLocalization", default=None
    )
    app_store_version_localization: typing.Optional[
        AppScreenshotSetRelationshipsAppStoreVersionLocalization
    ] = _PydanticField(alias="appStoreVersionLocalization", default=None)


class AppStoreVersionLocalization(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[AppStoreVersionLocalizationAttributes] = _PydanticField(
        alias="attributes", default=None
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    relationships: typing.Optional[AppStoreVersionLocalizationRelationships] = (
        _PydanticField(alias="relationships", default=None)
    )
    type: typing_extensions.Literal["appStoreVersionLocalizations"] = _PydanticField(
        alias="type"
    )


class AppCustomProductPageLocalization(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[AppCustomProductPageLocalizationAttributes] = (
        _PydanticField(alias="attributes", default=None)
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    relationships: typing.Optional[AppCustomProductPageLocalizationRelationships] = (
        _PydanticField(alias="relationships", default=None)
    )
    type: typing_extensions.Literal["appCustomProductPageLocalizations"] = (
        _PydanticField(alias="type")
    )


class AppStoreVersionExperimentTreatmentLocalization(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[
        AppStoreVersionExperimentTreatmentLocalizationAttributes
    ] = _PydanticField(alias="attributes", default=None)
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    relationships: typing.Optional[
        AppStoreVersionExperimentTreatmentLocalizationRelationships
    ] = _PydanticField(alias="relationships", default=None)
    type: typing_extensions.Literal[
        "appStoreVersionExperimentTreatmentLocalizations"
    ] = _PydanticField(alias="type")


class AppScreenshot(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[AppScreenshotAttributes] = _PydanticField(
        alias="attributes", default=None
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    relationships: typing.Optional[AppScreenshotRelationships] = _PydanticField(
        alias="relationships", default=None
    )
    type: typing_extensions.Literal["appScreenshots"] = _PydanticField(alias="type")


class AppScreenshotSet(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[AppScreenshotSetAttributes] = _PydanticField(
        alias="attributes", default=None
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    relationships: typing.Optional[AppScreenshotSetRelationships] = _PydanticField(
        alias="relationships", default=None
    )
    type: typing_extensions.Literal["appScreenshotSets"] = _PydanticField(alias="type")


class AppScreenshotSetsResponse(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.List[AppScreenshotSet] = _PydanticField(alias="data")
    included: typing.Optional[
        typing.List[
            typing.Union[
                AppStoreVersionLocalization,
                AppCustomProductPageLocalization,
                AppStoreVersionExperimentTreatmentLocalization,
                AppScreenshot,
            ]
        ]
    ] = _PydanticField(alias="included", default=None)
    links: PagedDocumentLinks = _PydanticField(alias="links")
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )
