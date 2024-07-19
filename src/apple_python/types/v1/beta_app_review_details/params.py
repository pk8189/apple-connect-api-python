"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class BetaAppReviewDetailUpdateRequestDataAttributes(typing_extensions.TypedDict):
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


class _SerializerBetaAppReviewDetailUpdateRequestDataAttributes(pydantic.BaseModel):
    """
    Serializer for BetaAppReviewDetailUpdateRequestDataAttributes handling case conversions
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


class BetaAppReviewDetailUpdateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.NotRequired[
        BetaAppReviewDetailUpdateRequestDataAttributes
    ]
    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["betaAppReviewDetails"]]


class _SerializerBetaAppReviewDetailUpdateRequestData(pydantic.BaseModel):
    """
    Serializer for BetaAppReviewDetailUpdateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: typing.Optional[
        _SerializerBetaAppReviewDetailUpdateRequestDataAttributes
    ] = pydantic.Field(alias="attributes", default=None)
    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["betaAppReviewDetails"] = pydantic.Field(
        alias="type"
    )


class BetaAppReviewDetailUpdateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[BetaAppReviewDetailUpdateRequestData]


class _SerializerBetaAppReviewDetailUpdateRequest(pydantic.BaseModel):
    """
    Serializer for BetaAppReviewDetailUpdateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerBetaAppReviewDetailUpdateRequestData = pydantic.Field(alias="data")