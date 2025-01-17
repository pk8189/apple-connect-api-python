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


class GameCenterLeaderboardSetLocalizationAttributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    locale_field: typing.Optional[str] = _PydanticField(alias="locale", default=None)
    name: typing.Optional[str] = _PydanticField(alias="name", default=None)


class ResourceLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class GameCenterLeaderboardSetLocalizationRelationshipsGameCenterLeaderboardSetData(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["gameCenterLeaderboardSets"] = _PydanticField(
        alias="type"
    )


class GameCenterLeaderboardSetLocalizationRelationshipsGameCenterLeaderboardSetLinks(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class GameCenterLeaderboardSetLocalizationRelationshipsGameCenterLeaderboardSetImageData(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["gameCenterLeaderboardSetImages"] = _PydanticField(
        alias="type"
    )


class GameCenterLeaderboardSetLocalizationRelationshipsGameCenterLeaderboardSetImageLinks(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class GameCenterLeaderboardSetAttributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    reference_name: typing.Optional[str] = _PydanticField(
        alias="referenceName", default=None
    )
    vendor_identifier: typing.Optional[str] = _PydanticField(
        alias="vendorIdentifier", default=None
    )


class GameCenterLeaderboardSetRelationshipsGameCenterDetailData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["gameCenterDetails"] = _PydanticField(alias="type")


class GameCenterLeaderboardSetRelationshipsGameCenterDetailLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class GameCenterLeaderboardSetRelationshipsGameCenterGroupData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["gameCenterGroups"] = _PydanticField(alias="type")


class GameCenterLeaderboardSetRelationshipsGameCenterGroupLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class GameCenterLeaderboardSetRelationshipsGameCenterLeaderboardsDataItem(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["gameCenterLeaderboards"] = _PydanticField(
        alias="type"
    )


class GameCenterLeaderboardSetRelationshipsGameCenterLeaderboardsLinks(
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


class GameCenterLeaderboardSetRelationshipsGroupLeaderboardSetData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["gameCenterLeaderboardSets"] = _PydanticField(
        alias="type"
    )


class GameCenterLeaderboardSetRelationshipsGroupLeaderboardSetLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class GameCenterLeaderboardSetRelationshipsLocalizationsDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["gameCenterLeaderboardSetLocalizations"] = (
        _PydanticField(alias="type")
    )


class GameCenterLeaderboardSetRelationshipsLocalizationsLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class GameCenterLeaderboardSetRelationshipsReleasesDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["gameCenterLeaderboardSetReleases"] = (
        _PydanticField(alias="type")
    )


class GameCenterLeaderboardSetRelationshipsReleasesLinks(_PydanticBaseModel):
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


class GameCenterLeaderboardSetImageRelationshipsGameCenterLeaderboardSetLocalizationData(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["gameCenterLeaderboardSetLocalizations"] = (
        _PydanticField(alias="type")
    )


class GameCenterLeaderboardSetImageRelationshipsGameCenterLeaderboardSetLocalizationLinks(
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


class GameCenterLeaderboardSetLocalizationRelationshipsGameCenterLeaderboardSet(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        GameCenterLeaderboardSetLocalizationRelationshipsGameCenterLeaderboardSetData
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[
        GameCenterLeaderboardSetLocalizationRelationshipsGameCenterLeaderboardSetLinks
    ] = _PydanticField(alias="links", default=None)


class GameCenterLeaderboardSetLocalizationRelationshipsGameCenterLeaderboardSetImage(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        GameCenterLeaderboardSetLocalizationRelationshipsGameCenterLeaderboardSetImageData
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[
        GameCenterLeaderboardSetLocalizationRelationshipsGameCenterLeaderboardSetImageLinks
    ] = _PydanticField(alias="links", default=None)


class GameCenterLeaderboardSetRelationshipsGameCenterDetail(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[GameCenterLeaderboardSetRelationshipsGameCenterDetailData] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[
        GameCenterLeaderboardSetRelationshipsGameCenterDetailLinks
    ] = _PydanticField(alias="links", default=None)


class GameCenterLeaderboardSetRelationshipsGameCenterGroup(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[GameCenterLeaderboardSetRelationshipsGameCenterGroupData] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[
        GameCenterLeaderboardSetRelationshipsGameCenterGroupLinks
    ] = _PydanticField(alias="links", default=None)


class PagingInformation(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    paging: PagingInformationPaging = _PydanticField(alias="paging")


class GameCenterLeaderboardSetRelationshipsGroupLeaderboardSet(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        GameCenterLeaderboardSetRelationshipsGroupLeaderboardSetData
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[
        GameCenterLeaderboardSetRelationshipsGroupLeaderboardSetLinks
    ] = _PydanticField(alias="links", default=None)


class GameCenterLeaderboardSetRelationshipsLocalizations(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        typing.List[GameCenterLeaderboardSetRelationshipsLocalizationsDataItem]
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[GameCenterLeaderboardSetRelationshipsLocalizationsLinks] = (
        _PydanticField(alias="links", default=None)
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class GameCenterLeaderboardSetRelationshipsReleases(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        typing.List[GameCenterLeaderboardSetRelationshipsReleasesDataItem]
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[GameCenterLeaderboardSetRelationshipsReleasesLinks] = (
        _PydanticField(alias="links", default=None)
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


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


class GameCenterLeaderboardSetImageRelationshipsGameCenterLeaderboardSetLocalization(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        GameCenterLeaderboardSetImageRelationshipsGameCenterLeaderboardSetLocalizationData
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[
        GameCenterLeaderboardSetImageRelationshipsGameCenterLeaderboardSetLocalizationLinks
    ] = _PydanticField(alias="links", default=None)


class GameCenterLeaderboardSetLocalizationRelationships(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    game_center_leaderboard_set: typing.Optional[
        GameCenterLeaderboardSetLocalizationRelationshipsGameCenterLeaderboardSet
    ] = _PydanticField(alias="gameCenterLeaderboardSet", default=None)
    game_center_leaderboard_set_image: typing.Optional[
        GameCenterLeaderboardSetLocalizationRelationshipsGameCenterLeaderboardSetImage
    ] = _PydanticField(alias="gameCenterLeaderboardSetImage", default=None)


class GameCenterLeaderboardSetRelationshipsGameCenterLeaderboards(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        typing.List[GameCenterLeaderboardSetRelationshipsGameCenterLeaderboardsDataItem]
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[
        GameCenterLeaderboardSetRelationshipsGameCenterLeaderboardsLinks
    ] = _PydanticField(alias="links", default=None)
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class GameCenterLeaderboardSetImageAttributes(_PydanticBaseModel):
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


class GameCenterLeaderboardSetImageRelationships(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    game_center_leaderboard_set_localization: typing.Optional[
        GameCenterLeaderboardSetImageRelationshipsGameCenterLeaderboardSetLocalization
    ] = _PydanticField(alias="gameCenterLeaderboardSetLocalization", default=None)


class GameCenterLeaderboardSetLocalization(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[GameCenterLeaderboardSetLocalizationAttributes] = (
        _PydanticField(alias="attributes", default=None)
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    relationships: typing.Optional[
        GameCenterLeaderboardSetLocalizationRelationships
    ] = _PydanticField(alias="relationships", default=None)
    type: typing_extensions.Literal["gameCenterLeaderboardSetLocalizations"] = (
        _PydanticField(alias="type")
    )


class GameCenterLeaderboardSetRelationships(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    game_center_detail: typing.Optional[
        GameCenterLeaderboardSetRelationshipsGameCenterDetail
    ] = _PydanticField(alias="gameCenterDetail", default=None)
    game_center_group: typing.Optional[
        GameCenterLeaderboardSetRelationshipsGameCenterGroup
    ] = _PydanticField(alias="gameCenterGroup", default=None)
    game_center_leaderboards: typing.Optional[
        GameCenterLeaderboardSetRelationshipsGameCenterLeaderboards
    ] = _PydanticField(alias="gameCenterLeaderboards", default=None)
    group_leaderboard_set: typing.Optional[
        GameCenterLeaderboardSetRelationshipsGroupLeaderboardSet
    ] = _PydanticField(alias="groupLeaderboardSet", default=None)
    localizations: typing.Optional[
        GameCenterLeaderboardSetRelationshipsLocalizations
    ] = _PydanticField(alias="localizations", default=None)
    releases: typing.Optional[GameCenterLeaderboardSetRelationshipsReleases] = (
        _PydanticField(alias="releases", default=None)
    )


class GameCenterLeaderboardSetImage(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[GameCenterLeaderboardSetImageAttributes] = (
        _PydanticField(alias="attributes", default=None)
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    relationships: typing.Optional[GameCenterLeaderboardSetImageRelationships] = (
        _PydanticField(alias="relationships", default=None)
    )
    type: typing_extensions.Literal["gameCenterLeaderboardSetImages"] = _PydanticField(
        alias="type"
    )


class GameCenterLeaderboardSet(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[GameCenterLeaderboardSetAttributes] = _PydanticField(
        alias="attributes", default=None
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    relationships: typing.Optional[GameCenterLeaderboardSetRelationships] = (
        _PydanticField(alias="relationships", default=None)
    )
    type: typing_extensions.Literal["gameCenterLeaderboardSets"] = _PydanticField(
        alias="type"
    )


class GameCenterLeaderboardSetLocalizationsResponse(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.List[GameCenterLeaderboardSetLocalization] = _PydanticField(
        alias="data"
    )
    included: typing.Optional[
        typing.List[
            typing.Union[GameCenterLeaderboardSet, GameCenterLeaderboardSetImage]
        ]
    ] = _PydanticField(alias="included", default=None)
    links: PagedDocumentLinks = _PydanticField(alias="links")
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )
