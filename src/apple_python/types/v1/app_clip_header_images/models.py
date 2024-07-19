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


class ResourceLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppClipHeaderImageRelationshipsAppClipDefaultExperienceLocalizationData(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["appClipDefaultExperienceLocalizations"] = (
        _PydanticField(alias="type")
    )


class AppClipHeaderImageRelationshipsAppClipDefaultExperienceLocalizationLinks(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppClipDefaultExperienceLocalizationAttributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    locale_field: typing.Optional[str] = _PydanticField(alias="locale", default=None)
    subtitle: typing.Optional[str] = _PydanticField(alias="subtitle", default=None)


class AppClipDefaultExperienceLocalizationRelationshipsAppClipDefaultExperienceData(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["appClipDefaultExperiences"] = _PydanticField(
        alias="type"
    )


class AppClipDefaultExperienceLocalizationRelationshipsAppClipDefaultExperienceLinks(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppClipDefaultExperienceLocalizationRelationshipsAppClipHeaderImageData(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["appClipHeaderImages"] = _PydanticField(
        alias="type"
    )


class AppClipDefaultExperienceLocalizationRelationshipsAppClipHeaderImageLinks(
    _PydanticBaseModel
):
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


class AppClipHeaderImageRelationshipsAppClipDefaultExperienceLocalization(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        AppClipHeaderImageRelationshipsAppClipDefaultExperienceLocalizationData
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[
        AppClipHeaderImageRelationshipsAppClipDefaultExperienceLocalizationLinks
    ] = _PydanticField(alias="links", default=None)


class AppClipDefaultExperienceLocalizationRelationshipsAppClipDefaultExperience(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        AppClipDefaultExperienceLocalizationRelationshipsAppClipDefaultExperienceData
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[
        AppClipDefaultExperienceLocalizationRelationshipsAppClipDefaultExperienceLinks
    ] = _PydanticField(alias="links", default=None)


class AppClipDefaultExperienceLocalizationRelationshipsAppClipHeaderImage(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        AppClipDefaultExperienceLocalizationRelationshipsAppClipHeaderImageData
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[
        AppClipDefaultExperienceLocalizationRelationshipsAppClipHeaderImageLinks
    ] = _PydanticField(alias="links", default=None)


class AppClipHeaderImageAttributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    asset_delivery_state: typing.Optional[AppMediaAssetState] = _PydanticField(
        alias="assetDeliveryState", default=None
    )
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


class AppClipHeaderImageRelationships(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    app_clip_default_experience_localization: typing.Optional[
        AppClipHeaderImageRelationshipsAppClipDefaultExperienceLocalization
    ] = _PydanticField(alias="appClipDefaultExperienceLocalization", default=None)


class AppClipDefaultExperienceLocalizationRelationships(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    app_clip_default_experience: typing.Optional[
        AppClipDefaultExperienceLocalizationRelationshipsAppClipDefaultExperience
    ] = _PydanticField(alias="appClipDefaultExperience", default=None)
    app_clip_header_image: typing.Optional[
        AppClipDefaultExperienceLocalizationRelationshipsAppClipHeaderImage
    ] = _PydanticField(alias="appClipHeaderImage", default=None)


class AppClipHeaderImage(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[AppClipHeaderImageAttributes] = _PydanticField(
        alias="attributes", default=None
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    relationships: typing.Optional[AppClipHeaderImageRelationships] = _PydanticField(
        alias="relationships", default=None
    )
    type: typing_extensions.Literal["appClipHeaderImages"] = _PydanticField(
        alias="type"
    )


class AppClipDefaultExperienceLocalization(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[AppClipDefaultExperienceLocalizationAttributes] = (
        _PydanticField(alias="attributes", default=None)
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    relationships: typing.Optional[
        AppClipDefaultExperienceLocalizationRelationships
    ] = _PydanticField(alias="relationships", default=None)
    type: typing_extensions.Literal["appClipDefaultExperienceLocalizations"] = (
        _PydanticField(alias="type")
    )


class AppClipHeaderImageResponse(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: AppClipHeaderImage = _PydanticField(alias="data")
    included: typing.Optional[typing.List[AppClipDefaultExperienceLocalization]] = (
        _PydanticField(alias="included", default=None)
    )
    links: DocumentLinks = _PydanticField(alias="links")
