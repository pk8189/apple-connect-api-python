"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class AppClipDefaultExperienceLocalizationUpdateRequestDataAttributes(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    subtitle: typing_extensions.NotRequired[str]


class _SerializerAppClipDefaultExperienceLocalizationUpdateRequestDataAttributes(
    pydantic.BaseModel
):
    """
    Serializer for AppClipDefaultExperienceLocalizationUpdateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    subtitle: typing.Optional[str] = pydantic.Field(alias="subtitle", default=None)


class AppClipDefaultExperienceLocalizationCreateRequestDataAttributes(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    locale_field: typing_extensions.Required[str]
    subtitle: typing_extensions.NotRequired[str]


class _SerializerAppClipDefaultExperienceLocalizationCreateRequestDataAttributes(
    pydantic.BaseModel
):
    """
    Serializer for AppClipDefaultExperienceLocalizationCreateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    locale_field: str = pydantic.Field(alias="locale")
    subtitle: typing.Optional[str] = pydantic.Field(alias="subtitle", default=None)


class AppClipDefaultExperienceLocalizationCreateRequestDataRelationshipsAppClipDefaultExperienceData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[
        typing_extensions.Literal["appClipDefaultExperiences"]
    ]


class _SerializerAppClipDefaultExperienceLocalizationCreateRequestDataRelationshipsAppClipDefaultExperienceData(
    pydantic.BaseModel
):
    """
    Serializer for AppClipDefaultExperienceLocalizationCreateRequestDataRelationshipsAppClipDefaultExperienceData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["appClipDefaultExperiences"] = pydantic.Field(
        alias="type"
    )


class AppClipDefaultExperienceLocalizationUpdateRequestData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    attributes: typing_extensions.NotRequired[
        AppClipDefaultExperienceLocalizationUpdateRequestDataAttributes
    ]
    id: typing_extensions.Required[str]
    type: typing_extensions.Required[
        typing_extensions.Literal["appClipDefaultExperienceLocalizations"]
    ]


class _SerializerAppClipDefaultExperienceLocalizationUpdateRequestData(
    pydantic.BaseModel
):
    """
    Serializer for AppClipDefaultExperienceLocalizationUpdateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: typing.Optional[
        _SerializerAppClipDefaultExperienceLocalizationUpdateRequestDataAttributes
    ] = pydantic.Field(alias="attributes", default=None)
    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["appClipDefaultExperienceLocalizations"] = (
        pydantic.Field(alias="type")
    )


class AppClipDefaultExperienceLocalizationCreateRequestDataRelationshipsAppClipDefaultExperience(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.Required[
        AppClipDefaultExperienceLocalizationCreateRequestDataRelationshipsAppClipDefaultExperienceData
    ]


class _SerializerAppClipDefaultExperienceLocalizationCreateRequestDataRelationshipsAppClipDefaultExperience(
    pydantic.BaseModel
):
    """
    Serializer for AppClipDefaultExperienceLocalizationCreateRequestDataRelationshipsAppClipDefaultExperience handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerAppClipDefaultExperienceLocalizationCreateRequestDataRelationshipsAppClipDefaultExperienceData = pydantic.Field(
        alias="data"
    )


class AppClipDefaultExperienceLocalizationUpdateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[
        AppClipDefaultExperienceLocalizationUpdateRequestData
    ]


class _SerializerAppClipDefaultExperienceLocalizationUpdateRequest(pydantic.BaseModel):
    """
    Serializer for AppClipDefaultExperienceLocalizationUpdateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerAppClipDefaultExperienceLocalizationUpdateRequestData = (
        pydantic.Field(alias="data")
    )


class AppClipDefaultExperienceLocalizationCreateRequestDataRelationships(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    app_clip_default_experience: typing_extensions.Required[
        AppClipDefaultExperienceLocalizationCreateRequestDataRelationshipsAppClipDefaultExperience
    ]


class _SerializerAppClipDefaultExperienceLocalizationCreateRequestDataRelationships(
    pydantic.BaseModel
):
    """
    Serializer for AppClipDefaultExperienceLocalizationCreateRequestDataRelationships handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    app_clip_default_experience: _SerializerAppClipDefaultExperienceLocalizationCreateRequestDataRelationshipsAppClipDefaultExperience = pydantic.Field(
        alias="appClipDefaultExperience"
    )


class AppClipDefaultExperienceLocalizationCreateRequestData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    attributes: typing_extensions.Required[
        AppClipDefaultExperienceLocalizationCreateRequestDataAttributes
    ]
    relationships: typing_extensions.Required[
        AppClipDefaultExperienceLocalizationCreateRequestDataRelationships
    ]
    type: typing_extensions.Required[
        typing_extensions.Literal["appClipDefaultExperienceLocalizations"]
    ]


class _SerializerAppClipDefaultExperienceLocalizationCreateRequestData(
    pydantic.BaseModel
):
    """
    Serializer for AppClipDefaultExperienceLocalizationCreateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: _SerializerAppClipDefaultExperienceLocalizationCreateRequestDataAttributes = pydantic.Field(
        alias="attributes"
    )
    relationships: _SerializerAppClipDefaultExperienceLocalizationCreateRequestDataRelationships = pydantic.Field(
        alias="relationships"
    )
    type: typing_extensions.Literal["appClipDefaultExperienceLocalizations"] = (
        pydantic.Field(alias="type")
    )


class AppClipDefaultExperienceLocalizationCreateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[
        AppClipDefaultExperienceLocalizationCreateRequestData
    ]


class _SerializerAppClipDefaultExperienceLocalizationCreateRequest(pydantic.BaseModel):
    """
    Serializer for AppClipDefaultExperienceLocalizationCreateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerAppClipDefaultExperienceLocalizationCreateRequestData = (
        pydantic.Field(alias="data")
    )
