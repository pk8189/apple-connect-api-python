"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class SubscriptionOfferCodeUpdateRequestDataAttributes(typing_extensions.TypedDict):
    """
    No description specified
    """

    active: typing_extensions.NotRequired[bool]


class _SerializerSubscriptionOfferCodeUpdateRequestDataAttributes(pydantic.BaseModel):
    """
    Serializer for SubscriptionOfferCodeUpdateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    active: typing.Optional[bool] = pydantic.Field(alias="active", default=None)


class SubscriptionOfferCodeCreateRequestDataAttributes(typing_extensions.TypedDict):
    """
    No description specified
    """

    customer_eligibilities: typing_extensions.Required[
        typing.List[typing_extensions.Literal["NEW", "EXISTING", "EXPIRED"]]
    ]
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
    name: typing_extensions.Required[str]
    number_of_periods: typing_extensions.Required[int]
    offer_eligibility: typing_extensions.Required[
        typing_extensions.Literal["STACK_WITH_INTRO_OFFERS", "REPLACE_INTRO_OFFERS"]
    ]
    offer_mode: typing_extensions.Required[
        typing_extensions.Literal["PAY_AS_YOU_GO", "PAY_UP_FRONT", "FREE_TRIAL"]
    ]


class _SerializerSubscriptionOfferCodeCreateRequestDataAttributes(pydantic.BaseModel):
    """
    Serializer for SubscriptionOfferCodeCreateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    customer_eligibilities: typing.List[
        typing_extensions.Literal["NEW", "EXISTING", "EXPIRED"]
    ] = pydantic.Field(alias="customerEligibilities")
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
    name: str = pydantic.Field(alias="name")
    number_of_periods: int = pydantic.Field(alias="numberOfPeriods")
    offer_eligibility: typing_extensions.Literal[
        "STACK_WITH_INTRO_OFFERS", "REPLACE_INTRO_OFFERS"
    ] = pydantic.Field(alias="offerEligibility")
    offer_mode: typing_extensions.Literal[
        "PAY_AS_YOU_GO", "PAY_UP_FRONT", "FREE_TRIAL"
    ] = pydantic.Field(alias="offerMode")


class SubscriptionOfferCodeCreateRequestDataRelationshipsPricesDataItem(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[
        typing_extensions.Literal["subscriptionOfferCodePrices"]
    ]


class _SerializerSubscriptionOfferCodeCreateRequestDataRelationshipsPricesDataItem(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionOfferCodeCreateRequestDataRelationshipsPricesDataItem handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["subscriptionOfferCodePrices"] = pydantic.Field(
        alias="type"
    )


class SubscriptionOfferCodeCreateRequestDataRelationshipsSubscriptionData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["subscriptions"]]


class _SerializerSubscriptionOfferCodeCreateRequestDataRelationshipsSubscriptionData(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionOfferCodeCreateRequestDataRelationshipsSubscriptionData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["subscriptions"] = pydantic.Field(alias="type")


class SubscriptionOfferCodePriceInlineCreateRelationshipsSubscriptionPricePointData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[
        typing_extensions.Literal["subscriptionPricePoints"]
    ]


class _SerializerSubscriptionOfferCodePriceInlineCreateRelationshipsSubscriptionPricePointData(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionOfferCodePriceInlineCreateRelationshipsSubscriptionPricePointData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["subscriptionPricePoints"] = pydantic.Field(
        alias="type"
    )


class SubscriptionOfferCodePriceInlineCreateRelationshipsTerritoryData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["territories"]]


class _SerializerSubscriptionOfferCodePriceInlineCreateRelationshipsTerritoryData(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionOfferCodePriceInlineCreateRelationshipsTerritoryData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["territories"] = pydantic.Field(alias="type")


class SubscriptionOfferCodeUpdateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.NotRequired[
        SubscriptionOfferCodeUpdateRequestDataAttributes
    ]
    id: typing_extensions.Required[str]
    type: typing_extensions.Required[
        typing_extensions.Literal["subscriptionOfferCodes"]
    ]


class _SerializerSubscriptionOfferCodeUpdateRequestData(pydantic.BaseModel):
    """
    Serializer for SubscriptionOfferCodeUpdateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: typing.Optional[
        _SerializerSubscriptionOfferCodeUpdateRequestDataAttributes
    ] = pydantic.Field(alias="attributes", default=None)
    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["subscriptionOfferCodes"] = pydantic.Field(
        alias="type"
    )


class SubscriptionOfferCodeCreateRequestDataRelationshipsPrices(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.Required[
        typing.List[SubscriptionOfferCodeCreateRequestDataRelationshipsPricesDataItem]
    ]


class _SerializerSubscriptionOfferCodeCreateRequestDataRelationshipsPrices(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionOfferCodeCreateRequestDataRelationshipsPrices handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: typing.List[
        _SerializerSubscriptionOfferCodeCreateRequestDataRelationshipsPricesDataItem
    ] = pydantic.Field(alias="data")


class SubscriptionOfferCodeCreateRequestDataRelationshipsSubscription(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.Required[
        SubscriptionOfferCodeCreateRequestDataRelationshipsSubscriptionData
    ]


class _SerializerSubscriptionOfferCodeCreateRequestDataRelationshipsSubscription(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionOfferCodeCreateRequestDataRelationshipsSubscription handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerSubscriptionOfferCodeCreateRequestDataRelationshipsSubscriptionData = pydantic.Field(
        alias="data"
    )


class SubscriptionOfferCodePriceInlineCreateRelationshipsSubscriptionPricePoint(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.NotRequired[
        SubscriptionOfferCodePriceInlineCreateRelationshipsSubscriptionPricePointData
    ]


class _SerializerSubscriptionOfferCodePriceInlineCreateRelationshipsSubscriptionPricePoint(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionOfferCodePriceInlineCreateRelationshipsSubscriptionPricePoint handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: typing.Optional[
        _SerializerSubscriptionOfferCodePriceInlineCreateRelationshipsSubscriptionPricePointData
    ] = pydantic.Field(alias="data", default=None)


class SubscriptionOfferCodePriceInlineCreateRelationshipsTerritory(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.NotRequired[
        SubscriptionOfferCodePriceInlineCreateRelationshipsTerritoryData
    ]


class _SerializerSubscriptionOfferCodePriceInlineCreateRelationshipsTerritory(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionOfferCodePriceInlineCreateRelationshipsTerritory handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: typing.Optional[
        _SerializerSubscriptionOfferCodePriceInlineCreateRelationshipsTerritoryData
    ] = pydantic.Field(alias="data", default=None)


class SubscriptionOfferCodeUpdateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[SubscriptionOfferCodeUpdateRequestData]


class _SerializerSubscriptionOfferCodeUpdateRequest(pydantic.BaseModel):
    """
    Serializer for SubscriptionOfferCodeUpdateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerSubscriptionOfferCodeUpdateRequestData = pydantic.Field(
        alias="data"
    )


class SubscriptionOfferCodeCreateRequestDataRelationships(typing_extensions.TypedDict):
    """
    No description specified
    """

    prices: typing_extensions.Required[
        SubscriptionOfferCodeCreateRequestDataRelationshipsPrices
    ]
    subscription: typing_extensions.Required[
        SubscriptionOfferCodeCreateRequestDataRelationshipsSubscription
    ]


class _SerializerSubscriptionOfferCodeCreateRequestDataRelationships(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionOfferCodeCreateRequestDataRelationships handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    prices: _SerializerSubscriptionOfferCodeCreateRequestDataRelationshipsPrices = (
        pydantic.Field(alias="prices")
    )
    subscription: _SerializerSubscriptionOfferCodeCreateRequestDataRelationshipsSubscription = pydantic.Field(
        alias="subscription"
    )


class SubscriptionOfferCodePriceInlineCreateRelationships(typing_extensions.TypedDict):
    """
    No description specified
    """

    subscription_price_point: typing_extensions.NotRequired[
        SubscriptionOfferCodePriceInlineCreateRelationshipsSubscriptionPricePoint
    ]
    territory: typing_extensions.NotRequired[
        SubscriptionOfferCodePriceInlineCreateRelationshipsTerritory
    ]


class _SerializerSubscriptionOfferCodePriceInlineCreateRelationships(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionOfferCodePriceInlineCreateRelationships handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    subscription_price_point: typing.Optional[
        _SerializerSubscriptionOfferCodePriceInlineCreateRelationshipsSubscriptionPricePoint
    ] = pydantic.Field(alias="subscriptionPricePoint", default=None)
    territory: typing.Optional[
        _SerializerSubscriptionOfferCodePriceInlineCreateRelationshipsTerritory
    ] = pydantic.Field(alias="territory", default=None)


class SubscriptionOfferCodeCreateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.Required[
        SubscriptionOfferCodeCreateRequestDataAttributes
    ]
    relationships: typing_extensions.Required[
        SubscriptionOfferCodeCreateRequestDataRelationships
    ]
    type: typing_extensions.Required[
        typing_extensions.Literal["subscriptionOfferCodes"]
    ]


class _SerializerSubscriptionOfferCodeCreateRequestData(pydantic.BaseModel):
    """
    Serializer for SubscriptionOfferCodeCreateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: _SerializerSubscriptionOfferCodeCreateRequestDataAttributes = (
        pydantic.Field(alias="attributes")
    )
    relationships: _SerializerSubscriptionOfferCodeCreateRequestDataRelationships = (
        pydantic.Field(alias="relationships")
    )
    type: typing_extensions.Literal["subscriptionOfferCodes"] = pydantic.Field(
        alias="type"
    )


class SubscriptionOfferCodePriceInlineCreate(typing_extensions.TypedDict):
    """
    No description specified
    """

    id: typing_extensions.NotRequired[str]
    relationships: typing_extensions.NotRequired[
        SubscriptionOfferCodePriceInlineCreateRelationships
    ]
    type: typing_extensions.Required[
        typing_extensions.Literal["subscriptionOfferCodePrices"]
    ]


class _SerializerSubscriptionOfferCodePriceInlineCreate(pydantic.BaseModel):
    """
    Serializer for SubscriptionOfferCodePriceInlineCreate handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    relationships: typing.Optional[
        _SerializerSubscriptionOfferCodePriceInlineCreateRelationships
    ] = pydantic.Field(alias="relationships", default=None)
    type: typing_extensions.Literal["subscriptionOfferCodePrices"] = pydantic.Field(
        alias="type"
    )


class SubscriptionOfferCodeCreateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[SubscriptionOfferCodeCreateRequestData]
    included: typing_extensions.NotRequired[
        typing.List[SubscriptionOfferCodePriceInlineCreate]
    ]


class _SerializerSubscriptionOfferCodeCreateRequest(pydantic.BaseModel):
    """
    Serializer for SubscriptionOfferCodeCreateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerSubscriptionOfferCodeCreateRequestData = pydantic.Field(
        alias="data"
    )
    included: typing.Optional[
        typing.List[_SerializerSubscriptionOfferCodePriceInlineCreate]
    ] = pydantic.Field(alias="included", default=None)
