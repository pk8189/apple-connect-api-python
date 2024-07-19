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


class PromotedPurchaseImageRelationshipsPromotedPurchaseData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["promotedPurchases"] = _PydanticField(alias="type")


class PromotedPurchaseImageRelationshipsPromotedPurchaseLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class PromotedPurchaseAttributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    enabled: typing.Optional[bool] = _PydanticField(alias="enabled", default=None)
    state: typing.Optional[
        typing_extensions.Literal[
            "APPROVED", "IN_REVIEW", "PREPARE_FOR_SUBMISSION", "REJECTED"
        ]
    ] = _PydanticField(alias="state", default=None)
    visible_for_all_users: typing.Optional[bool] = _PydanticField(
        alias="visibleForAllUsers", default=None
    )


class PromotedPurchaseRelationshipsInAppPurchaseV2Data(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["inAppPurchases"] = _PydanticField(alias="type")


class PromotedPurchaseRelationshipsInAppPurchaseV2Links(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class PromotedPurchaseRelationshipsPromotionImagesDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["promotedPurchaseImages"] = _PydanticField(
        alias="type"
    )


class PromotedPurchaseRelationshipsPromotionImagesLinks(_PydanticBaseModel):
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


class PromotedPurchaseRelationshipsSubscriptionData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["subscriptions"] = _PydanticField(alias="type")


class PromotedPurchaseRelationshipsSubscriptionLinks(_PydanticBaseModel):
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


class PromotedPurchaseImageRelationshipsPromotedPurchase(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[PromotedPurchaseImageRelationshipsPromotedPurchaseData] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[PromotedPurchaseImageRelationshipsPromotedPurchaseLinks] = (
        _PydanticField(alias="links", default=None)
    )


class PromotedPurchaseRelationshipsInAppPurchaseV2(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[PromotedPurchaseRelationshipsInAppPurchaseV2Data] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[PromotedPurchaseRelationshipsInAppPurchaseV2Links] = (
        _PydanticField(alias="links", default=None)
    )


class PagingInformation(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    paging: PagingInformationPaging = _PydanticField(alias="paging")


class PromotedPurchaseRelationshipsSubscription(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[PromotedPurchaseRelationshipsSubscriptionData] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[PromotedPurchaseRelationshipsSubscriptionLinks] = (
        _PydanticField(alias="links", default=None)
    )


class PromotedPurchaseImageAttributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
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
    state: typing.Optional[
        typing_extensions.Literal[
            "AWAITING_UPLOAD",
            "UPLOAD_COMPLETE",
            "FAILED",
            "PREPARE_FOR_SUBMISSION",
            "WAITING_FOR_REVIEW",
            "APPROVED",
            "REJECTED",
        ]
    ] = _PydanticField(alias="state", default=None)
    upload_operations: typing.Optional[typing.List[UploadOperation]] = _PydanticField(
        alias="uploadOperations", default=None
    )


class PromotedPurchaseImageRelationships(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    promoted_purchase: typing.Optional[
        PromotedPurchaseImageRelationshipsPromotedPurchase
    ] = _PydanticField(alias="promotedPurchase", default=None)


class PromotedPurchaseRelationshipsPromotionImages(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        typing.List[PromotedPurchaseRelationshipsPromotionImagesDataItem]
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[PromotedPurchaseRelationshipsPromotionImagesLinks] = (
        _PydanticField(alias="links", default=None)
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class PromotedPurchaseImage(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[PromotedPurchaseImageAttributes] = _PydanticField(
        alias="attributes", default=None
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    relationships: typing.Optional[PromotedPurchaseImageRelationships] = _PydanticField(
        alias="relationships", default=None
    )
    type: typing_extensions.Literal["promotedPurchaseImages"] = _PydanticField(
        alias="type"
    )


class PromotedPurchaseRelationships(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    in_app_purchase_v2: typing.Optional[
        PromotedPurchaseRelationshipsInAppPurchaseV2
    ] = _PydanticField(alias="inAppPurchaseV2", default=None)
    promotion_images: typing.Optional[PromotedPurchaseRelationshipsPromotionImages] = (
        _PydanticField(alias="promotionImages", default=None)
    )
    subscription: typing.Optional[PromotedPurchaseRelationshipsSubscription] = (
        _PydanticField(alias="subscription", default=None)
    )


class PromotedPurchase(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[PromotedPurchaseAttributes] = _PydanticField(
        alias="attributes", default=None
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    relationships: typing.Optional[PromotedPurchaseRelationships] = _PydanticField(
        alias="relationships", default=None
    )
    type: typing_extensions.Literal["promotedPurchases"] = _PydanticField(alias="type")


class PromotedPurchaseImagesResponse(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.List[PromotedPurchaseImage] = _PydanticField(alias="data")
    included: typing.Optional[typing.List[PromotedPurchase]] = _PydanticField(
        alias="included", default=None
    )
    links: PagedDocumentLinks = _PydanticField(alias="links")
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )