"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class SubscriptionIntroductoryOfferUpdateRequestDataAttributes(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    end_date: typing_extensions.NotRequired[str]


class _SerializerSubscriptionIntroductoryOfferUpdateRequestDataAttributes(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionIntroductoryOfferUpdateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    end_date: typing.Optional[str] = pydantic.Field(alias="endDate", default=None)


class SubscriptionIntroductoryOfferCreateRequestDataAttributes(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    duration: typing_extensions.Required[
        typing_extensions.Literal[
            "ONE_DAY",
            "THREE_DAYS",
            "ONE_WEEK",
            "TWO_WEEKS",
            "ONE_MONTH",
            "TWO_MONTHS",
            "THREE_MONTHS",
            "SIX_MONTHS",
            "ONE_YEAR",
        ]
    ]
    end_date: typing_extensions.NotRequired[str]
    number_of_periods: typing_extensions.Required[int]
    offer_mode: typing_extensions.Required[
        typing_extensions.Literal["PAY_AS_YOU_GO", "PAY_UP_FRONT", "FREE_TRIAL"]
    ]
    start_date: typing_extensions.NotRequired[str]


class _SerializerSubscriptionIntroductoryOfferCreateRequestDataAttributes(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionIntroductoryOfferCreateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    duration: typing_extensions.Literal[
        "ONE_DAY",
        "THREE_DAYS",
        "ONE_WEEK",
        "TWO_WEEKS",
        "ONE_MONTH",
        "TWO_MONTHS",
        "THREE_MONTHS",
        "SIX_MONTHS",
        "ONE_YEAR",
    ] = pydantic.Field(alias="duration")
    end_date: typing.Optional[str] = pydantic.Field(alias="endDate", default=None)
    number_of_periods: int = pydantic.Field(alias="numberOfPeriods")
    offer_mode: typing_extensions.Literal[
        "PAY_AS_YOU_GO", "PAY_UP_FRONT", "FREE_TRIAL"
    ] = pydantic.Field(alias="offerMode")
    start_date: typing.Optional[str] = pydantic.Field(alias="startDate", default=None)


class SubscriptionIntroductoryOfferCreateRequestDataRelationshipsSubscriptionData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["subscriptions"]]


class _SerializerSubscriptionIntroductoryOfferCreateRequestDataRelationshipsSubscriptionData(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionIntroductoryOfferCreateRequestDataRelationshipsSubscriptionData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["subscriptions"] = pydantic.Field(alias="type")


class SubscriptionIntroductoryOfferCreateRequestDataRelationshipsSubscriptionPricePointData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[
        typing_extensions.Literal["subscriptionPricePoints"]
    ]


class _SerializerSubscriptionIntroductoryOfferCreateRequestDataRelationshipsSubscriptionPricePointData(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionIntroductoryOfferCreateRequestDataRelationshipsSubscriptionPricePointData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["subscriptionPricePoints"] = pydantic.Field(
        alias="type"
    )


class SubscriptionIntroductoryOfferCreateRequestDataRelationshipsTerritoryData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["territories"]]


class _SerializerSubscriptionIntroductoryOfferCreateRequestDataRelationshipsTerritoryData(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionIntroductoryOfferCreateRequestDataRelationshipsTerritoryData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["territories"] = pydantic.Field(alias="type")


class SubscriptionPricePointInlineCreate(typing_extensions.TypedDict):
    """
    No description specified
    """

    id: typing_extensions.NotRequired[str]
    type: typing_extensions.Required[
        typing_extensions.Literal["subscriptionPricePoints"]
    ]


class _SerializerSubscriptionPricePointInlineCreate(pydantic.BaseModel):
    """
    Serializer for SubscriptionPricePointInlineCreate handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    type: typing_extensions.Literal["subscriptionPricePoints"] = pydantic.Field(
        alias="type"
    )


class SubscriptionIntroductoryOfferUpdateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.NotRequired[
        SubscriptionIntroductoryOfferUpdateRequestDataAttributes
    ]
    id: typing_extensions.Required[str]
    type: typing_extensions.Required[
        typing_extensions.Literal["subscriptionIntroductoryOffers"]
    ]


class _SerializerSubscriptionIntroductoryOfferUpdateRequestData(pydantic.BaseModel):
    """
    Serializer for SubscriptionIntroductoryOfferUpdateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: typing.Optional[
        _SerializerSubscriptionIntroductoryOfferUpdateRequestDataAttributes
    ] = pydantic.Field(alias="attributes", default=None)
    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["subscriptionIntroductoryOffers"] = pydantic.Field(
        alias="type"
    )


class SubscriptionIntroductoryOfferCreateRequestDataRelationshipsSubscription(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.Required[
        SubscriptionIntroductoryOfferCreateRequestDataRelationshipsSubscriptionData
    ]


class _SerializerSubscriptionIntroductoryOfferCreateRequestDataRelationshipsSubscription(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionIntroductoryOfferCreateRequestDataRelationshipsSubscription handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerSubscriptionIntroductoryOfferCreateRequestDataRelationshipsSubscriptionData = pydantic.Field(
        alias="data"
    )


class SubscriptionIntroductoryOfferCreateRequestDataRelationshipsSubscriptionPricePoint(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.NotRequired[
        SubscriptionIntroductoryOfferCreateRequestDataRelationshipsSubscriptionPricePointData
    ]


class _SerializerSubscriptionIntroductoryOfferCreateRequestDataRelationshipsSubscriptionPricePoint(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionIntroductoryOfferCreateRequestDataRelationshipsSubscriptionPricePoint handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: typing.Optional[
        _SerializerSubscriptionIntroductoryOfferCreateRequestDataRelationshipsSubscriptionPricePointData
    ] = pydantic.Field(alias="data", default=None)


class SubscriptionIntroductoryOfferCreateRequestDataRelationshipsTerritory(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.NotRequired[
        SubscriptionIntroductoryOfferCreateRequestDataRelationshipsTerritoryData
    ]


class _SerializerSubscriptionIntroductoryOfferCreateRequestDataRelationshipsTerritory(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionIntroductoryOfferCreateRequestDataRelationshipsTerritory handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: typing.Optional[
        _SerializerSubscriptionIntroductoryOfferCreateRequestDataRelationshipsTerritoryData
    ] = pydantic.Field(alias="data", default=None)


class SubscriptionIntroductoryOfferUpdateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[SubscriptionIntroductoryOfferUpdateRequestData]


class _SerializerSubscriptionIntroductoryOfferUpdateRequest(pydantic.BaseModel):
    """
    Serializer for SubscriptionIntroductoryOfferUpdateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerSubscriptionIntroductoryOfferUpdateRequestData = pydantic.Field(
        alias="data"
    )


class SubscriptionIntroductoryOfferCreateRequestDataRelationships(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    subscription: typing_extensions.Required[
        SubscriptionIntroductoryOfferCreateRequestDataRelationshipsSubscription
    ]
    subscription_price_point: typing_extensions.NotRequired[
        SubscriptionIntroductoryOfferCreateRequestDataRelationshipsSubscriptionPricePoint
    ]
    territory: typing_extensions.NotRequired[
        SubscriptionIntroductoryOfferCreateRequestDataRelationshipsTerritory
    ]


class _SerializerSubscriptionIntroductoryOfferCreateRequestDataRelationships(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionIntroductoryOfferCreateRequestDataRelationships handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    subscription: _SerializerSubscriptionIntroductoryOfferCreateRequestDataRelationshipsSubscription = pydantic.Field(
        alias="subscription"
    )
    subscription_price_point: typing.Optional[
        _SerializerSubscriptionIntroductoryOfferCreateRequestDataRelationshipsSubscriptionPricePoint
    ] = pydantic.Field(alias="subscriptionPricePoint", default=None)
    territory: typing.Optional[
        _SerializerSubscriptionIntroductoryOfferCreateRequestDataRelationshipsTerritory
    ] = pydantic.Field(alias="territory", default=None)


class SubscriptionIntroductoryOfferCreateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.Required[
        SubscriptionIntroductoryOfferCreateRequestDataAttributes
    ]
    relationships: typing_extensions.Required[
        SubscriptionIntroductoryOfferCreateRequestDataRelationships
    ]
    type: typing_extensions.Required[
        typing_extensions.Literal["subscriptionIntroductoryOffers"]
    ]


class _SerializerSubscriptionIntroductoryOfferCreateRequestData(pydantic.BaseModel):
    """
    Serializer for SubscriptionIntroductoryOfferCreateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: _SerializerSubscriptionIntroductoryOfferCreateRequestDataAttributes = (
        pydantic.Field(alias="attributes")
    )
    relationships: _SerializerSubscriptionIntroductoryOfferCreateRequestDataRelationships = pydantic.Field(
        alias="relationships"
    )
    type: typing_extensions.Literal["subscriptionIntroductoryOffers"] = pydantic.Field(
        alias="type"
    )


class SubscriptionIntroductoryOfferCreateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[SubscriptionIntroductoryOfferCreateRequestData]
    included: typing_extensions.NotRequired[
        typing.List[SubscriptionPricePointInlineCreate]
    ]


class _SerializerSubscriptionIntroductoryOfferCreateRequest(pydantic.BaseModel):
    """
    Serializer for SubscriptionIntroductoryOfferCreateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerSubscriptionIntroductoryOfferCreateRequestData = pydantic.Field(
        alias="data"
    )
    included: typing.Optional[
        typing.List[_SerializerSubscriptionPricePointInlineCreate]
    ] = pydantic.Field(alias="included", default=None)
