"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class SubscriptionOfferCodeOneTimeUseCodeUpdateRequestDataAttributes(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    active: typing_extensions.NotRequired[bool]


class _SerializerSubscriptionOfferCodeOneTimeUseCodeUpdateRequestDataAttributes(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionOfferCodeOneTimeUseCodeUpdateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    active: typing.Optional[bool] = pydantic.Field(alias="active", default=None)


class SubscriptionOfferCodeOneTimeUseCodeCreateRequestDataAttributes(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    expiration_date: typing_extensions.Required[str]
    number_of_codes: typing_extensions.Required[int]


class _SerializerSubscriptionOfferCodeOneTimeUseCodeCreateRequestDataAttributes(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionOfferCodeOneTimeUseCodeCreateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    expiration_date: str = pydantic.Field(alias="expirationDate")
    number_of_codes: int = pydantic.Field(alias="numberOfCodes")


class SubscriptionOfferCodeOneTimeUseCodeCreateRequestDataRelationshipsOfferCodeData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[
        typing_extensions.Literal["subscriptionOfferCodes"]
    ]


class _SerializerSubscriptionOfferCodeOneTimeUseCodeCreateRequestDataRelationshipsOfferCodeData(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionOfferCodeOneTimeUseCodeCreateRequestDataRelationshipsOfferCodeData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["subscriptionOfferCodes"] = pydantic.Field(
        alias="type"
    )


class SubscriptionOfferCodeOneTimeUseCodeUpdateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.NotRequired[
        SubscriptionOfferCodeOneTimeUseCodeUpdateRequestDataAttributes
    ]
    id: typing_extensions.Required[str]
    type: typing_extensions.Required[
        typing_extensions.Literal["subscriptionOfferCodeOneTimeUseCodes"]
    ]


class _SerializerSubscriptionOfferCodeOneTimeUseCodeUpdateRequestData(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionOfferCodeOneTimeUseCodeUpdateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: typing.Optional[
        _SerializerSubscriptionOfferCodeOneTimeUseCodeUpdateRequestDataAttributes
    ] = pydantic.Field(alias="attributes", default=None)
    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["subscriptionOfferCodeOneTimeUseCodes"] = (
        pydantic.Field(alias="type")
    )


class SubscriptionOfferCodeOneTimeUseCodeCreateRequestDataRelationshipsOfferCode(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.Required[
        SubscriptionOfferCodeOneTimeUseCodeCreateRequestDataRelationshipsOfferCodeData
    ]


class _SerializerSubscriptionOfferCodeOneTimeUseCodeCreateRequestDataRelationshipsOfferCode(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionOfferCodeOneTimeUseCodeCreateRequestDataRelationshipsOfferCode handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerSubscriptionOfferCodeOneTimeUseCodeCreateRequestDataRelationshipsOfferCodeData = pydantic.Field(
        alias="data"
    )


class SubscriptionOfferCodeOneTimeUseCodeUpdateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[
        SubscriptionOfferCodeOneTimeUseCodeUpdateRequestData
    ]


class _SerializerSubscriptionOfferCodeOneTimeUseCodeUpdateRequest(pydantic.BaseModel):
    """
    Serializer for SubscriptionOfferCodeOneTimeUseCodeUpdateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerSubscriptionOfferCodeOneTimeUseCodeUpdateRequestData = (
        pydantic.Field(alias="data")
    )


class SubscriptionOfferCodeOneTimeUseCodeCreateRequestDataRelationships(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    offer_code: typing_extensions.Required[
        SubscriptionOfferCodeOneTimeUseCodeCreateRequestDataRelationshipsOfferCode
    ]


class _SerializerSubscriptionOfferCodeOneTimeUseCodeCreateRequestDataRelationships(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionOfferCodeOneTimeUseCodeCreateRequestDataRelationships handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    offer_code: _SerializerSubscriptionOfferCodeOneTimeUseCodeCreateRequestDataRelationshipsOfferCode = pydantic.Field(
        alias="offerCode"
    )


class SubscriptionOfferCodeOneTimeUseCodeCreateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.Required[
        SubscriptionOfferCodeOneTimeUseCodeCreateRequestDataAttributes
    ]
    relationships: typing_extensions.Required[
        SubscriptionOfferCodeOneTimeUseCodeCreateRequestDataRelationships
    ]
    type: typing_extensions.Required[
        typing_extensions.Literal["subscriptionOfferCodeOneTimeUseCodes"]
    ]


class _SerializerSubscriptionOfferCodeOneTimeUseCodeCreateRequestData(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionOfferCodeOneTimeUseCodeCreateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: _SerializerSubscriptionOfferCodeOneTimeUseCodeCreateRequestDataAttributes = pydantic.Field(
        alias="attributes"
    )
    relationships: _SerializerSubscriptionOfferCodeOneTimeUseCodeCreateRequestDataRelationships = pydantic.Field(
        alias="relationships"
    )
    type: typing_extensions.Literal["subscriptionOfferCodeOneTimeUseCodes"] = (
        pydantic.Field(alias="type")
    )


class SubscriptionOfferCodeOneTimeUseCodeCreateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[
        SubscriptionOfferCodeOneTimeUseCodeCreateRequestData
    ]


class _SerializerSubscriptionOfferCodeOneTimeUseCodeCreateRequest(pydantic.BaseModel):
    """
    Serializer for SubscriptionOfferCodeOneTimeUseCodeCreateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerSubscriptionOfferCodeOneTimeUseCodeCreateRequestData = (
        pydantic.Field(alias="data")
    )
