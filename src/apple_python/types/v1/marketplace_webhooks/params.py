"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class MarketplaceWebhookUpdateRequestDataAttributes(typing_extensions.TypedDict):
    """
    No description specified
    """

    endpoint_url: typing_extensions.NotRequired[str]
    secret: typing_extensions.NotRequired[str]


class _SerializerMarketplaceWebhookUpdateRequestDataAttributes(pydantic.BaseModel):
    """
    Serializer for MarketplaceWebhookUpdateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    endpoint_url: typing.Optional[str] = pydantic.Field(
        alias="endpointUrl", default=None
    )
    secret: typing.Optional[str] = pydantic.Field(alias="secret", default=None)


class MarketplaceWebhookCreateRequestDataAttributes(typing_extensions.TypedDict):
    """
    No description specified
    """

    endpoint_url: typing_extensions.Required[str]
    secret: typing_extensions.Required[str]


class _SerializerMarketplaceWebhookCreateRequestDataAttributes(pydantic.BaseModel):
    """
    Serializer for MarketplaceWebhookCreateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    endpoint_url: str = pydantic.Field(alias="endpointUrl")
    secret: str = pydantic.Field(alias="secret")


class MarketplaceWebhookUpdateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.NotRequired[
        MarketplaceWebhookUpdateRequestDataAttributes
    ]
    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["marketplaceWebhooks"]]


class _SerializerMarketplaceWebhookUpdateRequestData(pydantic.BaseModel):
    """
    Serializer for MarketplaceWebhookUpdateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: typing.Optional[
        _SerializerMarketplaceWebhookUpdateRequestDataAttributes
    ] = pydantic.Field(alias="attributes", default=None)
    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["marketplaceWebhooks"] = pydantic.Field(
        alias="type"
    )


class MarketplaceWebhookCreateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.Required[
        MarketplaceWebhookCreateRequestDataAttributes
    ]
    type: typing_extensions.Required[typing_extensions.Literal["marketplaceWebhooks"]]


class _SerializerMarketplaceWebhookCreateRequestData(pydantic.BaseModel):
    """
    Serializer for MarketplaceWebhookCreateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: _SerializerMarketplaceWebhookCreateRequestDataAttributes = (
        pydantic.Field(alias="attributes")
    )
    type: typing_extensions.Literal["marketplaceWebhooks"] = pydantic.Field(
        alias="type"
    )


class MarketplaceWebhookUpdateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[MarketplaceWebhookUpdateRequestData]


class _SerializerMarketplaceWebhookUpdateRequest(pydantic.BaseModel):
    """
    Serializer for MarketplaceWebhookUpdateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerMarketplaceWebhookUpdateRequestData = pydantic.Field(alias="data")


class MarketplaceWebhookCreateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[MarketplaceWebhookCreateRequestData]


class _SerializerMarketplaceWebhookCreateRequest(pydantic.BaseModel):
    """
    Serializer for MarketplaceWebhookCreateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerMarketplaceWebhookCreateRequestData = pydantic.Field(alias="data")
