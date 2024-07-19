"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class AppStoreReviewDetailUpdateRequestDataAttributes(typing_extensions.TypedDict):
    """
    No description specified
    """

    contact_email: typing_extensions.NotRequired[str]
    contact_first_name: typing_extensions.NotRequired[str]
    contact_last_name: typing_extensions.NotRequired[str]
    contact_phone: typing_extensions.NotRequired[str]
    demo_account_name: typing_extensions.NotRequired[str]
    demo_account_password: typing_extensions.NotRequired[str]
    demo_account_required: typing_extensions.NotRequired[bool]
    notes: typing_extensions.NotRequired[str]


class _SerializerAppStoreReviewDetailUpdateRequestDataAttributes(pydantic.BaseModel):
    """
    Serializer for AppStoreReviewDetailUpdateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    contact_email: typing.Optional[str] = pydantic.Field(
        alias="contactEmail", default=None
    )
    contact_first_name: typing.Optional[str] = pydantic.Field(
        alias="contactFirstName", default=None
    )
    contact_last_name: typing.Optional[str] = pydantic.Field(
        alias="contactLastName", default=None
    )
    contact_phone: typing.Optional[str] = pydantic.Field(
        alias="contactPhone", default=None
    )
    demo_account_name: typing.Optional[str] = pydantic.Field(
        alias="demoAccountName", default=None
    )
    demo_account_password: typing.Optional[str] = pydantic.Field(
        alias="demoAccountPassword", default=None
    )
    demo_account_required: typing.Optional[bool] = pydantic.Field(
        alias="demoAccountRequired", default=None
    )
    notes: typing.Optional[str] = pydantic.Field(alias="notes", default=None)


class AppStoreReviewDetailCreateRequestDataAttributes(typing_extensions.TypedDict):
    """
    No description specified
    """

    contact_email: typing_extensions.NotRequired[str]
    contact_first_name: typing_extensions.NotRequired[str]
    contact_last_name: typing_extensions.NotRequired[str]
    contact_phone: typing_extensions.NotRequired[str]
    demo_account_name: typing_extensions.NotRequired[str]
    demo_account_password: typing_extensions.NotRequired[str]
    demo_account_required: typing_extensions.NotRequired[bool]
    notes: typing_extensions.NotRequired[str]


class _SerializerAppStoreReviewDetailCreateRequestDataAttributes(pydantic.BaseModel):
    """
    Serializer for AppStoreReviewDetailCreateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    contact_email: typing.Optional[str] = pydantic.Field(
        alias="contactEmail", default=None
    )
    contact_first_name: typing.Optional[str] = pydantic.Field(
        alias="contactFirstName", default=None
    )
    contact_last_name: typing.Optional[str] = pydantic.Field(
        alias="contactLastName", default=None
    )
    contact_phone: typing.Optional[str] = pydantic.Field(
        alias="contactPhone", default=None
    )
    demo_account_name: typing.Optional[str] = pydantic.Field(
        alias="demoAccountName", default=None
    )
    demo_account_password: typing.Optional[str] = pydantic.Field(
        alias="demoAccountPassword", default=None
    )
    demo_account_required: typing.Optional[bool] = pydantic.Field(
        alias="demoAccountRequired", default=None
    )
    notes: typing.Optional[str] = pydantic.Field(alias="notes", default=None)


class AppStoreReviewDetailCreateRequestDataRelationshipsAppStoreVersionData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["appStoreVersions"]]


class _SerializerAppStoreReviewDetailCreateRequestDataRelationshipsAppStoreVersionData(
    pydantic.BaseModel
):
    """
    Serializer for AppStoreReviewDetailCreateRequestDataRelationshipsAppStoreVersionData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["appStoreVersions"] = pydantic.Field(alias="type")


class AppStoreReviewDetailUpdateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.NotRequired[
        AppStoreReviewDetailUpdateRequestDataAttributes
    ]
    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["appStoreReviewDetails"]]


class _SerializerAppStoreReviewDetailUpdateRequestData(pydantic.BaseModel):
    """
    Serializer for AppStoreReviewDetailUpdateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: typing.Optional[
        _SerializerAppStoreReviewDetailUpdateRequestDataAttributes
    ] = pydantic.Field(alias="attributes", default=None)
    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["appStoreReviewDetails"] = pydantic.Field(
        alias="type"
    )


class AppStoreReviewDetailCreateRequestDataRelationshipsAppStoreVersion(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.Required[
        AppStoreReviewDetailCreateRequestDataRelationshipsAppStoreVersionData
    ]


class _SerializerAppStoreReviewDetailCreateRequestDataRelationshipsAppStoreVersion(
    pydantic.BaseModel
):
    """
    Serializer for AppStoreReviewDetailCreateRequestDataRelationshipsAppStoreVersion handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerAppStoreReviewDetailCreateRequestDataRelationshipsAppStoreVersionData = pydantic.Field(
        alias="data"
    )


class AppStoreReviewDetailUpdateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[AppStoreReviewDetailUpdateRequestData]


class _SerializerAppStoreReviewDetailUpdateRequest(pydantic.BaseModel):
    """
    Serializer for AppStoreReviewDetailUpdateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerAppStoreReviewDetailUpdateRequestData = pydantic.Field(
        alias="data"
    )


class AppStoreReviewDetailCreateRequestDataRelationships(typing_extensions.TypedDict):
    """
    No description specified
    """

    app_store_version: typing_extensions.Required[
        AppStoreReviewDetailCreateRequestDataRelationshipsAppStoreVersion
    ]


class _SerializerAppStoreReviewDetailCreateRequestDataRelationships(pydantic.BaseModel):
    """
    Serializer for AppStoreReviewDetailCreateRequestDataRelationships handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    app_store_version: _SerializerAppStoreReviewDetailCreateRequestDataRelationshipsAppStoreVersion = pydantic.Field(
        alias="appStoreVersion"
    )


class AppStoreReviewDetailCreateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.NotRequired[
        AppStoreReviewDetailCreateRequestDataAttributes
    ]
    relationships: typing_extensions.Required[
        AppStoreReviewDetailCreateRequestDataRelationships
    ]
    type: typing_extensions.Required[typing_extensions.Literal["appStoreReviewDetails"]]


class _SerializerAppStoreReviewDetailCreateRequestData(pydantic.BaseModel):
    """
    Serializer for AppStoreReviewDetailCreateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: typing.Optional[
        _SerializerAppStoreReviewDetailCreateRequestDataAttributes
    ] = pydantic.Field(alias="attributes", default=None)
    relationships: _SerializerAppStoreReviewDetailCreateRequestDataRelationships = (
        pydantic.Field(alias="relationships")
    )
    type: typing_extensions.Literal["appStoreReviewDetails"] = pydantic.Field(
        alias="type"
    )


class AppStoreReviewDetailCreateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[AppStoreReviewDetailCreateRequestData]


class _SerializerAppStoreReviewDetailCreateRequest(pydantic.BaseModel):
    """
    Serializer for AppStoreReviewDetailCreateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerAppStoreReviewDetailCreateRequestData = pydantic.Field(
        alias="data"
    )