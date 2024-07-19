"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class BetaAppClipInvocationLocalizationUpdateRequestDataAttributes(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    title: typing_extensions.NotRequired[str]


class _SerializerBetaAppClipInvocationLocalizationUpdateRequestDataAttributes(
    pydantic.BaseModel
):
    """
    Serializer for BetaAppClipInvocationLocalizationUpdateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    title: typing.Optional[str] = pydantic.Field(alias="title", default=None)


class BetaAppClipInvocationLocalizationCreateRequestDataAttributes(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    locale_field: typing_extensions.Required[str]
    title: typing_extensions.Required[str]


class _SerializerBetaAppClipInvocationLocalizationCreateRequestDataAttributes(
    pydantic.BaseModel
):
    """
    Serializer for BetaAppClipInvocationLocalizationCreateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    locale_field: str = pydantic.Field(alias="locale")
    title: str = pydantic.Field(alias="title")


class BetaAppClipInvocationLocalizationCreateRequestDataRelationshipsBetaAppClipInvocationData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[
        typing_extensions.Literal["betaAppClipInvocations"]
    ]


class _SerializerBetaAppClipInvocationLocalizationCreateRequestDataRelationshipsBetaAppClipInvocationData(
    pydantic.BaseModel
):
    """
    Serializer for BetaAppClipInvocationLocalizationCreateRequestDataRelationshipsBetaAppClipInvocationData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["betaAppClipInvocations"] = pydantic.Field(
        alias="type"
    )


class BetaAppClipInvocationLocalizationUpdateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.NotRequired[
        BetaAppClipInvocationLocalizationUpdateRequestDataAttributes
    ]
    id: typing_extensions.Required[str]
    type: typing_extensions.Required[
        typing_extensions.Literal["betaAppClipInvocationLocalizations"]
    ]


class _SerializerBetaAppClipInvocationLocalizationUpdateRequestData(pydantic.BaseModel):
    """
    Serializer for BetaAppClipInvocationLocalizationUpdateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: typing.Optional[
        _SerializerBetaAppClipInvocationLocalizationUpdateRequestDataAttributes
    ] = pydantic.Field(alias="attributes", default=None)
    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["betaAppClipInvocationLocalizations"] = (
        pydantic.Field(alias="type")
    )


class BetaAppClipInvocationLocalizationCreateRequestDataRelationshipsBetaAppClipInvocation(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.Required[
        BetaAppClipInvocationLocalizationCreateRequestDataRelationshipsBetaAppClipInvocationData
    ]


class _SerializerBetaAppClipInvocationLocalizationCreateRequestDataRelationshipsBetaAppClipInvocation(
    pydantic.BaseModel
):
    """
    Serializer for BetaAppClipInvocationLocalizationCreateRequestDataRelationshipsBetaAppClipInvocation handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerBetaAppClipInvocationLocalizationCreateRequestDataRelationshipsBetaAppClipInvocationData = pydantic.Field(
        alias="data"
    )


class BetaAppClipInvocationLocalizationUpdateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[BetaAppClipInvocationLocalizationUpdateRequestData]


class _SerializerBetaAppClipInvocationLocalizationUpdateRequest(pydantic.BaseModel):
    """
    Serializer for BetaAppClipInvocationLocalizationUpdateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerBetaAppClipInvocationLocalizationUpdateRequestData = (
        pydantic.Field(alias="data")
    )


class BetaAppClipInvocationLocalizationCreateRequestDataRelationships(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    beta_app_clip_invocation: typing_extensions.Required[
        BetaAppClipInvocationLocalizationCreateRequestDataRelationshipsBetaAppClipInvocation
    ]


class _SerializerBetaAppClipInvocationLocalizationCreateRequestDataRelationships(
    pydantic.BaseModel
):
    """
    Serializer for BetaAppClipInvocationLocalizationCreateRequestDataRelationships handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    beta_app_clip_invocation: _SerializerBetaAppClipInvocationLocalizationCreateRequestDataRelationshipsBetaAppClipInvocation = pydantic.Field(
        alias="betaAppClipInvocation"
    )


class BetaAppClipInvocationLocalizationCreateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.Required[
        BetaAppClipInvocationLocalizationCreateRequestDataAttributes
    ]
    relationships: typing_extensions.Required[
        BetaAppClipInvocationLocalizationCreateRequestDataRelationships
    ]
    type: typing_extensions.Required[
        typing_extensions.Literal["betaAppClipInvocationLocalizations"]
    ]


class _SerializerBetaAppClipInvocationLocalizationCreateRequestData(pydantic.BaseModel):
    """
    Serializer for BetaAppClipInvocationLocalizationCreateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: _SerializerBetaAppClipInvocationLocalizationCreateRequestDataAttributes = pydantic.Field(
        alias="attributes"
    )
    relationships: _SerializerBetaAppClipInvocationLocalizationCreateRequestDataRelationships = pydantic.Field(
        alias="relationships"
    )
    type: typing_extensions.Literal["betaAppClipInvocationLocalizations"] = (
        pydantic.Field(alias="type")
    )


class BetaAppClipInvocationLocalizationCreateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[BetaAppClipInvocationLocalizationCreateRequestData]


class _SerializerBetaAppClipInvocationLocalizationCreateRequest(pydantic.BaseModel):
    """
    Serializer for BetaAppClipInvocationLocalizationCreateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerBetaAppClipInvocationLocalizationCreateRequestData = (
        pydantic.Field(alias="data")
    )