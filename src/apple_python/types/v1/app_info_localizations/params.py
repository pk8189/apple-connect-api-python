"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class AppInfoLocalizationUpdateRequestDataAttributes(typing_extensions.TypedDict):
    """
    No description specified
    """

    name: typing_extensions.NotRequired[str]
    privacy_choices_url: typing_extensions.NotRequired[str]
    privacy_policy_text: typing_extensions.NotRequired[str]
    privacy_policy_url: typing_extensions.NotRequired[str]
    subtitle: typing_extensions.NotRequired[str]


class _SerializerAppInfoLocalizationUpdateRequestDataAttributes(pydantic.BaseModel):
    """
    Serializer for AppInfoLocalizationUpdateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    privacy_choices_url: typing.Optional[str] = pydantic.Field(
        alias="privacyChoicesUrl", default=None
    )
    privacy_policy_text: typing.Optional[str] = pydantic.Field(
        alias="privacyPolicyText", default=None
    )
    privacy_policy_url: typing.Optional[str] = pydantic.Field(
        alias="privacyPolicyUrl", default=None
    )
    subtitle: typing.Optional[str] = pydantic.Field(alias="subtitle", default=None)


class AppInfoLocalizationCreateRequestDataAttributes(typing_extensions.TypedDict):
    """
    No description specified
    """

    locale_field: typing_extensions.Required[str]
    name: typing_extensions.NotRequired[str]
    privacy_choices_url: typing_extensions.NotRequired[str]
    privacy_policy_text: typing_extensions.NotRequired[str]
    privacy_policy_url: typing_extensions.NotRequired[str]
    subtitle: typing_extensions.NotRequired[str]


class _SerializerAppInfoLocalizationCreateRequestDataAttributes(pydantic.BaseModel):
    """
    Serializer for AppInfoLocalizationCreateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    locale_field: str = pydantic.Field(alias="locale")
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    privacy_choices_url: typing.Optional[str] = pydantic.Field(
        alias="privacyChoicesUrl", default=None
    )
    privacy_policy_text: typing.Optional[str] = pydantic.Field(
        alias="privacyPolicyText", default=None
    )
    privacy_policy_url: typing.Optional[str] = pydantic.Field(
        alias="privacyPolicyUrl", default=None
    )
    subtitle: typing.Optional[str] = pydantic.Field(alias="subtitle", default=None)


class AppInfoLocalizationCreateRequestDataRelationshipsAppInfoData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["appInfos"]]


class _SerializerAppInfoLocalizationCreateRequestDataRelationshipsAppInfoData(
    pydantic.BaseModel
):
    """
    Serializer for AppInfoLocalizationCreateRequestDataRelationshipsAppInfoData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["appInfos"] = pydantic.Field(alias="type")


class AppInfoLocalizationUpdateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.NotRequired[
        AppInfoLocalizationUpdateRequestDataAttributes
    ]
    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["appInfoLocalizations"]]


class _SerializerAppInfoLocalizationUpdateRequestData(pydantic.BaseModel):
    """
    Serializer for AppInfoLocalizationUpdateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: typing.Optional[
        _SerializerAppInfoLocalizationUpdateRequestDataAttributes
    ] = pydantic.Field(alias="attributes", default=None)
    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["appInfoLocalizations"] = pydantic.Field(
        alias="type"
    )


class AppInfoLocalizationCreateRequestDataRelationshipsAppInfo(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.Required[
        AppInfoLocalizationCreateRequestDataRelationshipsAppInfoData
    ]


class _SerializerAppInfoLocalizationCreateRequestDataRelationshipsAppInfo(
    pydantic.BaseModel
):
    """
    Serializer for AppInfoLocalizationCreateRequestDataRelationshipsAppInfo handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerAppInfoLocalizationCreateRequestDataRelationshipsAppInfoData = (
        pydantic.Field(alias="data")
    )


class AppInfoLocalizationUpdateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[AppInfoLocalizationUpdateRequestData]


class _SerializerAppInfoLocalizationUpdateRequest(pydantic.BaseModel):
    """
    Serializer for AppInfoLocalizationUpdateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerAppInfoLocalizationUpdateRequestData = pydantic.Field(alias="data")


class AppInfoLocalizationCreateRequestDataRelationships(typing_extensions.TypedDict):
    """
    No description specified
    """

    app_info: typing_extensions.Required[
        AppInfoLocalizationCreateRequestDataRelationshipsAppInfo
    ]


class _SerializerAppInfoLocalizationCreateRequestDataRelationships(pydantic.BaseModel):
    """
    Serializer for AppInfoLocalizationCreateRequestDataRelationships handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    app_info: _SerializerAppInfoLocalizationCreateRequestDataRelationshipsAppInfo = (
        pydantic.Field(alias="appInfo")
    )


class AppInfoLocalizationCreateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.Required[
        AppInfoLocalizationCreateRequestDataAttributes
    ]
    relationships: typing_extensions.Required[
        AppInfoLocalizationCreateRequestDataRelationships
    ]
    type: typing_extensions.Required[typing_extensions.Literal["appInfoLocalizations"]]


class _SerializerAppInfoLocalizationCreateRequestData(pydantic.BaseModel):
    """
    Serializer for AppInfoLocalizationCreateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: _SerializerAppInfoLocalizationCreateRequestDataAttributes = (
        pydantic.Field(alias="attributes")
    )
    relationships: _SerializerAppInfoLocalizationCreateRequestDataRelationships = (
        pydantic.Field(alias="relationships")
    )
    type: typing_extensions.Literal["appInfoLocalizations"] = pydantic.Field(
        alias="type"
    )


class AppInfoLocalizationCreateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[AppInfoLocalizationCreateRequestData]


class _SerializerAppInfoLocalizationCreateRequest(pydantic.BaseModel):
    """
    Serializer for AppInfoLocalizationCreateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerAppInfoLocalizationCreateRequestData = pydantic.Field(alias="data")