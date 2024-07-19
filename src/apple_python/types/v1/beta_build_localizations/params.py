"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class BetaBuildLocalizationUpdateRequestDataAttributes(typing_extensions.TypedDict):
    """
    No description specified
    """

    whats_new: typing_extensions.NotRequired[str]


class _SerializerBetaBuildLocalizationUpdateRequestDataAttributes(pydantic.BaseModel):
    """
    Serializer for BetaBuildLocalizationUpdateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    whats_new: typing.Optional[str] = pydantic.Field(alias="whatsNew", default=None)


class BetaBuildLocalizationCreateRequestDataAttributes(typing_extensions.TypedDict):
    """
    No description specified
    """

    locale_field: typing_extensions.Required[str]
    whats_new: typing_extensions.NotRequired[str]


class _SerializerBetaBuildLocalizationCreateRequestDataAttributes(pydantic.BaseModel):
    """
    Serializer for BetaBuildLocalizationCreateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    locale_field: str = pydantic.Field(alias="locale")
    whats_new: typing.Optional[str] = pydantic.Field(alias="whatsNew", default=None)


class BetaBuildLocalizationCreateRequestDataRelationshipsBuildData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["builds"]]


class _SerializerBetaBuildLocalizationCreateRequestDataRelationshipsBuildData(
    pydantic.BaseModel
):
    """
    Serializer for BetaBuildLocalizationCreateRequestDataRelationshipsBuildData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["builds"] = pydantic.Field(alias="type")


class BetaBuildLocalizationUpdateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.NotRequired[
        BetaBuildLocalizationUpdateRequestDataAttributes
    ]
    id: typing_extensions.Required[str]
    type: typing_extensions.Required[
        typing_extensions.Literal["betaBuildLocalizations"]
    ]


class _SerializerBetaBuildLocalizationUpdateRequestData(pydantic.BaseModel):
    """
    Serializer for BetaBuildLocalizationUpdateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: typing.Optional[
        _SerializerBetaBuildLocalizationUpdateRequestDataAttributes
    ] = pydantic.Field(alias="attributes", default=None)
    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["betaBuildLocalizations"] = pydantic.Field(
        alias="type"
    )


class BetaBuildLocalizationCreateRequestDataRelationshipsBuild(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.Required[
        BetaBuildLocalizationCreateRequestDataRelationshipsBuildData
    ]


class _SerializerBetaBuildLocalizationCreateRequestDataRelationshipsBuild(
    pydantic.BaseModel
):
    """
    Serializer for BetaBuildLocalizationCreateRequestDataRelationshipsBuild handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerBetaBuildLocalizationCreateRequestDataRelationshipsBuildData = (
        pydantic.Field(alias="data")
    )


class BetaBuildLocalizationUpdateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[BetaBuildLocalizationUpdateRequestData]


class _SerializerBetaBuildLocalizationUpdateRequest(pydantic.BaseModel):
    """
    Serializer for BetaBuildLocalizationUpdateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerBetaBuildLocalizationUpdateRequestData = pydantic.Field(
        alias="data"
    )


class BetaBuildLocalizationCreateRequestDataRelationships(typing_extensions.TypedDict):
    """
    No description specified
    """

    build: typing_extensions.Required[
        BetaBuildLocalizationCreateRequestDataRelationshipsBuild
    ]


class _SerializerBetaBuildLocalizationCreateRequestDataRelationships(
    pydantic.BaseModel
):
    """
    Serializer for BetaBuildLocalizationCreateRequestDataRelationships handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    build: _SerializerBetaBuildLocalizationCreateRequestDataRelationshipsBuild = (
        pydantic.Field(alias="build")
    )


class BetaBuildLocalizationCreateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.Required[
        BetaBuildLocalizationCreateRequestDataAttributes
    ]
    relationships: typing_extensions.Required[
        BetaBuildLocalizationCreateRequestDataRelationships
    ]
    type: typing_extensions.Required[
        typing_extensions.Literal["betaBuildLocalizations"]
    ]


class _SerializerBetaBuildLocalizationCreateRequestData(pydantic.BaseModel):
    """
    Serializer for BetaBuildLocalizationCreateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: _SerializerBetaBuildLocalizationCreateRequestDataAttributes = (
        pydantic.Field(alias="attributes")
    )
    relationships: _SerializerBetaBuildLocalizationCreateRequestDataRelationships = (
        pydantic.Field(alias="relationships")
    )
    type: typing_extensions.Literal["betaBuildLocalizations"] = pydantic.Field(
        alias="type"
    )


class BetaBuildLocalizationCreateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[BetaBuildLocalizationCreateRequestData]


class _SerializerBetaBuildLocalizationCreateRequest(pydantic.BaseModel):
    """
    Serializer for BetaBuildLocalizationCreateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerBetaBuildLocalizationCreateRequestData = pydantic.Field(
        alias="data"
    )
