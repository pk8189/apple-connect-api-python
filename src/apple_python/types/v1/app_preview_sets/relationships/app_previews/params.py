"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class AppPreviewSetAppPreviewsLinkagesRequestDataItem(typing_extensions.TypedDict):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["appPreviews"]]


class _SerializerAppPreviewSetAppPreviewsLinkagesRequestDataItem(pydantic.BaseModel):
    """
    Serializer for AppPreviewSetAppPreviewsLinkagesRequestDataItem handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["appPreviews"] = pydantic.Field(alias="type")


class AppPreviewSetAppPreviewsLinkagesRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[
        typing.List[AppPreviewSetAppPreviewsLinkagesRequestDataItem]
    ]


class _SerializerAppPreviewSetAppPreviewsLinkagesRequest(pydantic.BaseModel):
    """
    Serializer for AppPreviewSetAppPreviewsLinkagesRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: typing.List[_SerializerAppPreviewSetAppPreviewsLinkagesRequestDataItem] = (
        pydantic.Field(alias="data")
    )