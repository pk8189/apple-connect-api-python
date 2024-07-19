"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class BuildUpdateRequestDataAttributes(typing_extensions.TypedDict):
    """
    No description specified
    """

    expired: typing_extensions.NotRequired[bool]
    uses_non_exempt_encryption: typing_extensions.NotRequired[bool]


class _SerializerBuildUpdateRequestDataAttributes(pydantic.BaseModel):
    """
    Serializer for BuildUpdateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    expired: typing.Optional[bool] = pydantic.Field(alias="expired", default=None)
    uses_non_exempt_encryption: typing.Optional[bool] = pydantic.Field(
        alias="usesNonExemptEncryption", default=None
    )


class BuildUpdateRequestDataRelationshipsAppEncryptionDeclarationData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[
        typing_extensions.Literal["appEncryptionDeclarations"]
    ]


class _SerializerBuildUpdateRequestDataRelationshipsAppEncryptionDeclarationData(
    pydantic.BaseModel
):
    """
    Serializer for BuildUpdateRequestDataRelationshipsAppEncryptionDeclarationData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["appEncryptionDeclarations"] = pydantic.Field(
        alias="type"
    )


class BuildUpdateRequestDataRelationshipsAppEncryptionDeclaration(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.NotRequired[
        BuildUpdateRequestDataRelationshipsAppEncryptionDeclarationData
    ]


class _SerializerBuildUpdateRequestDataRelationshipsAppEncryptionDeclaration(
    pydantic.BaseModel
):
    """
    Serializer for BuildUpdateRequestDataRelationshipsAppEncryptionDeclaration handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: typing.Optional[
        _SerializerBuildUpdateRequestDataRelationshipsAppEncryptionDeclarationData
    ] = pydantic.Field(alias="data", default=None)


class BuildUpdateRequestDataRelationships(typing_extensions.TypedDict):
    """
    No description specified
    """

    app_encryption_declaration: typing_extensions.NotRequired[
        BuildUpdateRequestDataRelationshipsAppEncryptionDeclaration
    ]


class _SerializerBuildUpdateRequestDataRelationships(pydantic.BaseModel):
    """
    Serializer for BuildUpdateRequestDataRelationships handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    app_encryption_declaration: typing.Optional[
        _SerializerBuildUpdateRequestDataRelationshipsAppEncryptionDeclaration
    ] = pydantic.Field(alias="appEncryptionDeclaration", default=None)


class BuildUpdateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.NotRequired[BuildUpdateRequestDataAttributes]
    id: typing_extensions.Required[str]
    relationships: typing_extensions.NotRequired[BuildUpdateRequestDataRelationships]
    type: typing_extensions.Required[typing_extensions.Literal["builds"]]


class _SerializerBuildUpdateRequestData(pydantic.BaseModel):
    """
    Serializer for BuildUpdateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: typing.Optional[_SerializerBuildUpdateRequestDataAttributes] = (
        pydantic.Field(alias="attributes", default=None)
    )
    id: str = pydantic.Field(alias="id")
    relationships: typing.Optional[_SerializerBuildUpdateRequestDataRelationships] = (
        pydantic.Field(alias="relationships", default=None)
    )
    type: typing_extensions.Literal["builds"] = pydantic.Field(alias="type")


class BuildUpdateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[BuildUpdateRequestData]


class _SerializerBuildUpdateRequest(pydantic.BaseModel):
    """
    Serializer for BuildUpdateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerBuildUpdateRequestData = pydantic.Field(alias="data")