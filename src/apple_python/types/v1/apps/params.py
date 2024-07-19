"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class AppUpdateRequestDataAttributes(typing_extensions.TypedDict):
    """
    No description specified
    """

    bundle_id: typing_extensions.NotRequired[str]
    content_rights_declaration: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "DOES_NOT_USE_THIRD_PARTY_CONTENT", "USES_THIRD_PARTY_CONTENT"
        ]
    ]
    primary_locale: typing_extensions.NotRequired[str]
    subscription_status_url: typing_extensions.NotRequired[str]
    subscription_status_url_for_sandbox: typing_extensions.NotRequired[str]
    subscription_status_url_version: typing_extensions.NotRequired[
        typing_extensions.Literal["V1", "V2", "v1", "v2"]
    ]
    subscription_status_url_version_for_sandbox: typing_extensions.NotRequired[
        typing_extensions.Literal["V1", "V2", "v1", "v2"]
    ]


class _SerializerAppUpdateRequestDataAttributes(pydantic.BaseModel):
    """
    Serializer for AppUpdateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    bundle_id: typing.Optional[str] = pydantic.Field(alias="bundleId", default=None)
    content_rights_declaration: typing.Optional[
        typing_extensions.Literal[
            "DOES_NOT_USE_THIRD_PARTY_CONTENT", "USES_THIRD_PARTY_CONTENT"
        ]
    ] = pydantic.Field(alias="contentRightsDeclaration", default=None)
    primary_locale: typing.Optional[str] = pydantic.Field(
        alias="primaryLocale", default=None
    )
    subscription_status_url: typing.Optional[str] = pydantic.Field(
        alias="subscriptionStatusUrl", default=None
    )
    subscription_status_url_for_sandbox: typing.Optional[str] = pydantic.Field(
        alias="subscriptionStatusUrlForSandbox", default=None
    )
    subscription_status_url_version: typing.Optional[
        typing_extensions.Literal["V1", "V2", "v1", "v2"]
    ] = pydantic.Field(alias="subscriptionStatusUrlVersion", default=None)
    subscription_status_url_version_for_sandbox: typing.Optional[
        typing_extensions.Literal["V1", "V2", "v1", "v2"]
    ] = pydantic.Field(alias="subscriptionStatusUrlVersionForSandbox", default=None)


class AppUpdateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.NotRequired[AppUpdateRequestDataAttributes]
    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["apps"]]


class _SerializerAppUpdateRequestData(pydantic.BaseModel):
    """
    Serializer for AppUpdateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: typing.Optional[_SerializerAppUpdateRequestDataAttributes] = (
        pydantic.Field(alias="attributes", default=None)
    )
    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["apps"] = pydantic.Field(alias="type")


class AppUpdateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[AppUpdateRequestData]


class _SerializerAppUpdateRequest(pydantic.BaseModel):
    """
    Serializer for AppUpdateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerAppUpdateRequestData = pydantic.Field(alias="data")