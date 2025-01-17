"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class SubscriptionGracePeriodUpdateRequestDataAttributes(typing_extensions.TypedDict):
    """
    No description specified
    """

    duration: typing_extensions.NotRequired[
        typing_extensions.Literal["THREE_DAYS", "SIXTEEN_DAYS", "TWENTY_EIGHT_DAYS"]
    ]
    opt_in: typing_extensions.NotRequired[bool]
    renewal_type: typing_extensions.NotRequired[
        typing_extensions.Literal["ALL_RENEWALS", "PAID_TO_PAID_ONLY"]
    ]
    sandbox_opt_in: typing_extensions.NotRequired[bool]


class _SerializerSubscriptionGracePeriodUpdateRequestDataAttributes(pydantic.BaseModel):
    """
    Serializer for SubscriptionGracePeriodUpdateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    duration: typing.Optional[
        typing_extensions.Literal["THREE_DAYS", "SIXTEEN_DAYS", "TWENTY_EIGHT_DAYS"]
    ] = pydantic.Field(alias="duration", default=None)
    opt_in: typing.Optional[bool] = pydantic.Field(alias="optIn", default=None)
    renewal_type: typing.Optional[
        typing_extensions.Literal["ALL_RENEWALS", "PAID_TO_PAID_ONLY"]
    ] = pydantic.Field(alias="renewalType", default=None)
    sandbox_opt_in: typing.Optional[bool] = pydantic.Field(
        alias="sandboxOptIn", default=None
    )


class SubscriptionGracePeriodUpdateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.NotRequired[
        SubscriptionGracePeriodUpdateRequestDataAttributes
    ]
    id: typing_extensions.Required[str]
    type: typing_extensions.Required[
        typing_extensions.Literal["subscriptionGracePeriods"]
    ]


class _SerializerSubscriptionGracePeriodUpdateRequestData(pydantic.BaseModel):
    """
    Serializer for SubscriptionGracePeriodUpdateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: typing.Optional[
        _SerializerSubscriptionGracePeriodUpdateRequestDataAttributes
    ] = pydantic.Field(alias="attributes", default=None)
    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["subscriptionGracePeriods"] = pydantic.Field(
        alias="type"
    )


class SubscriptionGracePeriodUpdateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[SubscriptionGracePeriodUpdateRequestData]


class _SerializerSubscriptionGracePeriodUpdateRequest(pydantic.BaseModel):
    """
    Serializer for SubscriptionGracePeriodUpdateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerSubscriptionGracePeriodUpdateRequestData = pydantic.Field(
        alias="data"
    )
