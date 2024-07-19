"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class AppScreenshotSetAppScreenshotsLinkagesRequestDataItem(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["appScreenshots"]]


class _SerializerAppScreenshotSetAppScreenshotsLinkagesRequestDataItem(
    pydantic.BaseModel
):
    """
    Serializer for AppScreenshotSetAppScreenshotsLinkagesRequestDataItem handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["appScreenshots"] = pydantic.Field(alias="type")


class AppScreenshotSetAppScreenshotsLinkagesRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[
        typing.List[AppScreenshotSetAppScreenshotsLinkagesRequestDataItem]
    ]


class _SerializerAppScreenshotSetAppScreenshotsLinkagesRequest(pydantic.BaseModel):
    """
    Serializer for AppScreenshotSetAppScreenshotsLinkagesRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: typing.List[
        _SerializerAppScreenshotSetAppScreenshotsLinkagesRequestDataItem
    ] = pydantic.Field(alias="data")