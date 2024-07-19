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


class ResourceLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class PagedDocumentLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    first: typing.Optional[str] = _PydanticField(alias="first", default=None)
    next: typing.Optional[str] = _PydanticField(alias="next", default=None)
    self: str = _PydanticField(alias="self")


class PagingInformationPaging(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    limit: int = _PydanticField(alias="limit")
    total: typing.Optional[int] = _PydanticField(alias="total", default=None)


class BuildIconAttributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    icon_asset: typing.Optional[ImageAsset] = _PydanticField(
        alias="iconAsset", default=None
    )
    icon_type: typing.Optional[
        typing_extensions.Literal[
            "APP_STORE",
            "MESSAGES_APP_STORE",
            "WATCH_APP_STORE",
            "TV_OS_HOME_SCREEN",
            "TV_OS_TOP_SHELF",
            "ALTERNATE_EXPERIMENT",
        ]
    ] = _PydanticField(alias="iconType", default=None)
    name: typing.Optional[str] = _PydanticField(alias="name", default=None)


class PagingInformation(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    paging: PagingInformationPaging = _PydanticField(alias="paging")


class BuildIcon(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[BuildIconAttributes] = _PydanticField(
        alias="attributes", default=None
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    type: typing_extensions.Literal["buildIcons"] = _PydanticField(alias="type")


class BuildIconsWithoutIncludesResponse(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.List[BuildIcon] = _PydanticField(alias="data")
    links: PagedDocumentLinks = _PydanticField(alias="links")
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )
