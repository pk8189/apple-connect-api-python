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


class BuildBundleFileSizeAttributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    device_model: typing.Optional[str] = _PydanticField(
        alias="deviceModel", default=None
    )
    download_bytes: typing.Optional[int] = _PydanticField(
        alias="downloadBytes", default=None
    )
    install_bytes: typing.Optional[int] = _PydanticField(
        alias="installBytes", default=None
    )
    os_version: typing.Optional[str] = _PydanticField(alias="osVersion", default=None)


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


class BuildBundleFileSize(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[BuildBundleFileSizeAttributes] = _PydanticField(
        alias="attributes", default=None
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    type: typing_extensions.Literal["buildBundleFileSizes"] = _PydanticField(
        alias="type"
    )


class PagingInformation(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    paging: PagingInformationPaging = _PydanticField(alias="paging")


class BuildBundleFileSizesResponse(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.List[BuildBundleFileSize] = _PydanticField(alias="data")
    links: PagedDocumentLinks = _PydanticField(alias="links")
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )