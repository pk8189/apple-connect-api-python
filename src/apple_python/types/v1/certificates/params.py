"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class CertificateCreateRequestDataAttributes(typing_extensions.TypedDict):
    """
    No description specified
    """

    certificate_type: typing_extensions.Required[
        typing_extensions.Literal[
            "IOS_DEVELOPMENT",
            "IOS_DISTRIBUTION",
            "MAC_APP_DISTRIBUTION",
            "MAC_INSTALLER_DISTRIBUTION",
            "MAC_APP_DEVELOPMENT",
            "DEVELOPER_ID_KEXT",
            "DEVELOPER_ID_APPLICATION",
            "DEVELOPMENT",
            "DISTRIBUTION",
            "PASS_TYPE_ID",
            "PASS_TYPE_ID_WITH_NFC",
        ]
    ]
    csr_content: typing_extensions.Required[str]


class _SerializerCertificateCreateRequestDataAttributes(pydantic.BaseModel):
    """
    Serializer for CertificateCreateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    certificate_type: typing_extensions.Literal[
        "IOS_DEVELOPMENT",
        "IOS_DISTRIBUTION",
        "MAC_APP_DISTRIBUTION",
        "MAC_INSTALLER_DISTRIBUTION",
        "MAC_APP_DEVELOPMENT",
        "DEVELOPER_ID_KEXT",
        "DEVELOPER_ID_APPLICATION",
        "DEVELOPMENT",
        "DISTRIBUTION",
        "PASS_TYPE_ID",
        "PASS_TYPE_ID_WITH_NFC",
    ] = pydantic.Field(alias="certificateType")
    csr_content: str = pydantic.Field(alias="csrContent")


class CertificateCreateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.Required[CertificateCreateRequestDataAttributes]
    type: typing_extensions.Required[typing_extensions.Literal["certificates"]]


class _SerializerCertificateCreateRequestData(pydantic.BaseModel):
    """
    Serializer for CertificateCreateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: _SerializerCertificateCreateRequestDataAttributes = pydantic.Field(
        alias="attributes"
    )
    type: typing_extensions.Literal["certificates"] = pydantic.Field(alias="type")


class CertificateCreateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[CertificateCreateRequestData]


class _SerializerCertificateCreateRequest(pydantic.BaseModel):
    """
    Serializer for CertificateCreateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerCertificateCreateRequestData = pydantic.Field(alias="data")
