"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class BuildAppEncryptionDeclarationLinkageRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[
        typing_extensions.Literal["appEncryptionDeclarations"]
    ]


class _SerializerBuildAppEncryptionDeclarationLinkageRequestData(pydantic.BaseModel):
    """
    Serializer for BuildAppEncryptionDeclarationLinkageRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["appEncryptionDeclarations"] = pydantic.Field(
        alias="type"
    )


class BuildAppEncryptionDeclarationLinkageRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[BuildAppEncryptionDeclarationLinkageRequestData]


class _SerializerBuildAppEncryptionDeclarationLinkageRequest(pydantic.BaseModel):
    """
    Serializer for BuildAppEncryptionDeclarationLinkageRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerBuildAppEncryptionDeclarationLinkageRequestData = pydantic.Field(
        alias="data"
    )
