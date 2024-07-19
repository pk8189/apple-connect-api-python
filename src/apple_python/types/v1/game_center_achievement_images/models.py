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


class GameCenterAchievementImageRelationshipsGameCenterAchievementLocalizationData(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["gameCenterAchievementLocalizations"] = (
        _PydanticField(alias="type")
    )


class GameCenterAchievementImageRelationshipsGameCenterAchievementLocalizationLinks(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class GameCenterAchievementLocalizationAttributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    after_earned_description: typing.Optional[str] = _PydanticField(
        alias="afterEarnedDescription", default=None
    )
    before_earned_description: typing.Optional[str] = _PydanticField(
        alias="beforeEarnedDescription", default=None
    )
    locale_field: typing.Optional[str] = _PydanticField(alias="locale", default=None)
    name: typing.Optional[str] = _PydanticField(alias="name", default=None)


class GameCenterAchievementLocalizationRelationshipsGameCenterAchievementData(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["gameCenterAchievements"] = _PydanticField(
        alias="type"
    )


class GameCenterAchievementLocalizationRelationshipsGameCenterAchievementLinks(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class GameCenterAchievementLocalizationRelationshipsGameCenterAchievementImageData(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["gameCenterAchievementImages"] = _PydanticField(
        alias="type"
    )


class GameCenterAchievementLocalizationRelationshipsGameCenterAchievementImageLinks(
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


class GameCenterAchievementImageRelationshipsGameCenterAchievementLocalization(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        GameCenterAchievementImageRelationshipsGameCenterAchievementLocalizationData
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[
        GameCenterAchievementImageRelationshipsGameCenterAchievementLocalizationLinks
    ] = _PydanticField(alias="links", default=None)


class GameCenterAchievementLocalizationRelationshipsGameCenterAchievement(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        GameCenterAchievementLocalizationRelationshipsGameCenterAchievementData
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[
        GameCenterAchievementLocalizationRelationshipsGameCenterAchievementLinks
    ] = _PydanticField(alias="links", default=None)


class GameCenterAchievementLocalizationRelationshipsGameCenterAchievementImage(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        GameCenterAchievementLocalizationRelationshipsGameCenterAchievementImageData
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[
        GameCenterAchievementLocalizationRelationshipsGameCenterAchievementImageLinks
    ] = _PydanticField(alias="links", default=None)


class GameCenterAchievementImageAttributes(_PydanticBaseModel):
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
    upload_operations: typing.Optional[typing.List[UploadOperation]] = _PydanticField(
        alias="uploadOperations", default=None
    )


class GameCenterAchievementImageRelationships(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    game_center_achievement_localization: typing.Optional[
        GameCenterAchievementImageRelationshipsGameCenterAchievementLocalization
    ] = _PydanticField(alias="gameCenterAchievementLocalization", default=None)


class GameCenterAchievementLocalizationRelationships(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    game_center_achievement: typing.Optional[
        GameCenterAchievementLocalizationRelationshipsGameCenterAchievement
    ] = _PydanticField(alias="gameCenterAchievement", default=None)
    game_center_achievement_image: typing.Optional[
        GameCenterAchievementLocalizationRelationshipsGameCenterAchievementImage
    ] = _PydanticField(alias="gameCenterAchievementImage", default=None)


class GameCenterAchievementImage(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[GameCenterAchievementImageAttributes] = _PydanticField(
        alias="attributes", default=None
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    relationships: typing.Optional[GameCenterAchievementImageRelationships] = (
        _PydanticField(alias="relationships", default=None)
    )
    type: typing_extensions.Literal["gameCenterAchievementImages"] = _PydanticField(
        alias="type"
    )


class GameCenterAchievementLocalization(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[GameCenterAchievementLocalizationAttributes] = (
        _PydanticField(alias="attributes", default=None)
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    relationships: typing.Optional[GameCenterAchievementLocalizationRelationships] = (
        _PydanticField(alias="relationships", default=None)
    )
    type: typing_extensions.Literal["gameCenterAchievementLocalizations"] = (
        _PydanticField(alias="type")
    )


class GameCenterAchievementImageResponse(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: GameCenterAchievementImage = _PydanticField(alias="data")
    included: typing.Optional[typing.List[GameCenterAchievementLocalization]] = (
        _PydanticField(alias="included", default=None)
    )
    links: DocumentLinks = _PydanticField(alias="links")