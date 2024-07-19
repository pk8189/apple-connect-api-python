"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class AppStoreVersionBuildLinkageRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["builds"]]


class _SerializerAppStoreVersionBuildLinkageRequestData(pydantic.BaseModel):
    """
    Serializer for AppStoreVersionBuildLinkageRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["builds"] = pydantic.Field(alias="type")


class AppStoreVersionBuildLinkageRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[AppStoreVersionBuildLinkageRequestData]


class _SerializerAppStoreVersionBuildLinkageRequest(pydantic.BaseModel):
    """
    Serializer for AppStoreVersionBuildLinkageRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerAppStoreVersionBuildLinkageRequestData = pydantic.Field(
        alias="data"
    )
