"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class AppStoreVersionReleaseRequestCreateRequestDataRelationshipsAppStoreVersionData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["appStoreVersions"]]


class _SerializerAppStoreVersionReleaseRequestCreateRequestDataRelationshipsAppStoreVersionData(
    pydantic.BaseModel
):
    """
    Serializer for AppStoreVersionReleaseRequestCreateRequestDataRelationshipsAppStoreVersionData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["appStoreVersions"] = pydantic.Field(alias="type")


class AppStoreVersionReleaseRequestCreateRequestDataRelationshipsAppStoreVersion(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.Required[
        AppStoreVersionReleaseRequestCreateRequestDataRelationshipsAppStoreVersionData
    ]


class _SerializerAppStoreVersionReleaseRequestCreateRequestDataRelationshipsAppStoreVersion(
    pydantic.BaseModel
):
    """
    Serializer for AppStoreVersionReleaseRequestCreateRequestDataRelationshipsAppStoreVersion handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerAppStoreVersionReleaseRequestCreateRequestDataRelationshipsAppStoreVersionData = pydantic.Field(
        alias="data"
    )


class AppStoreVersionReleaseRequestCreateRequestDataRelationships(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    app_store_version: typing_extensions.Required[
        AppStoreVersionReleaseRequestCreateRequestDataRelationshipsAppStoreVersion
    ]


class _SerializerAppStoreVersionReleaseRequestCreateRequestDataRelationships(
    pydantic.BaseModel
):
    """
    Serializer for AppStoreVersionReleaseRequestCreateRequestDataRelationships handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    app_store_version: _SerializerAppStoreVersionReleaseRequestCreateRequestDataRelationshipsAppStoreVersion = pydantic.Field(
        alias="appStoreVersion"
    )


class AppStoreVersionReleaseRequestCreateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    relationships: typing_extensions.Required[
        AppStoreVersionReleaseRequestCreateRequestDataRelationships
    ]
    type: typing_extensions.Required[
        typing_extensions.Literal["appStoreVersionReleaseRequests"]
    ]


class _SerializerAppStoreVersionReleaseRequestCreateRequestData(pydantic.BaseModel):
    """
    Serializer for AppStoreVersionReleaseRequestCreateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    relationships: _SerializerAppStoreVersionReleaseRequestCreateRequestDataRelationships = pydantic.Field(
        alias="relationships"
    )
    type: typing_extensions.Literal["appStoreVersionReleaseRequests"] = pydantic.Field(
        alias="type"
    )


class AppStoreVersionReleaseRequestCreateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[AppStoreVersionReleaseRequestCreateRequestData]


class _SerializerAppStoreVersionReleaseRequestCreateRequest(pydantic.BaseModel):
    """
    Serializer for AppStoreVersionReleaseRequestCreateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerAppStoreVersionReleaseRequestCreateRequestData = pydantic.Field(
        alias="data"
    )