"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class SubscriptionOfferCodeCustomCodeUpdateRequestDataAttributes(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    active: typing_extensions.NotRequired[bool]


class _SerializerSubscriptionOfferCodeCustomCodeUpdateRequestDataAttributes(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionOfferCodeCustomCodeUpdateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    active: typing.Optional[bool] = pydantic.Field(alias="active", default=None)


class SubscriptionOfferCodeCustomCodeCreateRequestDataAttributes(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    custom_code: typing_extensions.Required[str]
    expiration_date: typing_extensions.NotRequired[str]
    number_of_codes: typing_extensions.Required[int]


class _SerializerSubscriptionOfferCodeCustomCodeCreateRequestDataAttributes(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionOfferCodeCustomCodeCreateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    custom_code: str = pydantic.Field(alias="customCode")
    expiration_date: typing.Optional[str] = pydantic.Field(
        alias="expirationDate", default=None
    )
    number_of_codes: int = pydantic.Field(alias="numberOfCodes")


class SubscriptionOfferCodeCustomCodeCreateRequestDataRelationshipsOfferCodeData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[
        typing_extensions.Literal["subscriptionOfferCodes"]
    ]


class _SerializerSubscriptionOfferCodeCustomCodeCreateRequestDataRelationshipsOfferCodeData(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionOfferCodeCustomCodeCreateRequestDataRelationshipsOfferCodeData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["subscriptionOfferCodes"] = pydantic.Field(
        alias="type"
    )


class SubscriptionOfferCodeCustomCodeUpdateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.NotRequired[
        SubscriptionOfferCodeCustomCodeUpdateRequestDataAttributes
    ]
    id: typing_extensions.Required[str]
    type: typing_extensions.Required[
        typing_extensions.Literal["subscriptionOfferCodeCustomCodes"]
    ]


class _SerializerSubscriptionOfferCodeCustomCodeUpdateRequestData(pydantic.BaseModel):
    """
    Serializer for SubscriptionOfferCodeCustomCodeUpdateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: typing.Optional[
        _SerializerSubscriptionOfferCodeCustomCodeUpdateRequestDataAttributes
    ] = pydantic.Field(alias="attributes", default=None)
    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["subscriptionOfferCodeCustomCodes"] = (
        pydantic.Field(alias="type")
    )


class SubscriptionOfferCodeCustomCodeCreateRequestDataRelationshipsOfferCode(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.Required[
        SubscriptionOfferCodeCustomCodeCreateRequestDataRelationshipsOfferCodeData
    ]


class _SerializerSubscriptionOfferCodeCustomCodeCreateRequestDataRelationshipsOfferCode(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionOfferCodeCustomCodeCreateRequestDataRelationshipsOfferCode handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerSubscriptionOfferCodeCustomCodeCreateRequestDataRelationshipsOfferCodeData = pydantic.Field(
        alias="data"
    )


class SubscriptionOfferCodeCustomCodeUpdateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[SubscriptionOfferCodeCustomCodeUpdateRequestData]


class _SerializerSubscriptionOfferCodeCustomCodeUpdateRequest(pydantic.BaseModel):
    """
    Serializer for SubscriptionOfferCodeCustomCodeUpdateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerSubscriptionOfferCodeCustomCodeUpdateRequestData = pydantic.Field(
        alias="data"
    )


class SubscriptionOfferCodeCustomCodeCreateRequestDataRelationships(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    offer_code: typing_extensions.Required[
        SubscriptionOfferCodeCustomCodeCreateRequestDataRelationshipsOfferCode
    ]


class _SerializerSubscriptionOfferCodeCustomCodeCreateRequestDataRelationships(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionOfferCodeCustomCodeCreateRequestDataRelationships handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    offer_code: _SerializerSubscriptionOfferCodeCustomCodeCreateRequestDataRelationshipsOfferCode = pydantic.Field(
        alias="offerCode"
    )


class SubscriptionOfferCodeCustomCodeCreateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.Required[
        SubscriptionOfferCodeCustomCodeCreateRequestDataAttributes
    ]
    relationships: typing_extensions.Required[
        SubscriptionOfferCodeCustomCodeCreateRequestDataRelationships
    ]
    type: typing_extensions.Required[
        typing_extensions.Literal["subscriptionOfferCodeCustomCodes"]
    ]


class _SerializerSubscriptionOfferCodeCustomCodeCreateRequestData(pydantic.BaseModel):
    """
    Serializer for SubscriptionOfferCodeCustomCodeCreateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: _SerializerSubscriptionOfferCodeCustomCodeCreateRequestDataAttributes = pydantic.Field(
        alias="attributes"
    )
    relationships: _SerializerSubscriptionOfferCodeCustomCodeCreateRequestDataRelationships = pydantic.Field(
        alias="relationships"
    )
    type: typing_extensions.Literal["subscriptionOfferCodeCustomCodes"] = (
        pydantic.Field(alias="type")
    )


class SubscriptionOfferCodeCustomCodeCreateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[SubscriptionOfferCodeCustomCodeCreateRequestData]


class _SerializerSubscriptionOfferCodeCustomCodeCreateRequest(pydantic.BaseModel):
    """
    Serializer for SubscriptionOfferCodeCustomCodeCreateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerSubscriptionOfferCodeCustomCodeCreateRequestData = pydantic.Field(
        alias="data"
    )
