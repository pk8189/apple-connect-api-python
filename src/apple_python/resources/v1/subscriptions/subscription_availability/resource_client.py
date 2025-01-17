"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    default_request_options,
    encode_param,
    SyncBaseClient,
    RequestOptions,
    AsyncBaseClient,
    QueryParams,
)
import typing
import typing_extensions
from apple_python.types.v1.subscriptions.subscription_availability import models


class SubscriptionAvailabilityClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        id: str,
        fields_subscription_availabilities: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "availableInNewTerritories", "availableTerritories", "subscription"
                ]
            ]
        ] = None,
        fields_subscriptions: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appStoreReviewScreenshot",
                    "familySharable",
                    "group",
                    "groupLevel",
                    "introductoryOffers",
                    "name",
                    "offerCodes",
                    "pricePoints",
                    "prices",
                    "productId",
                    "promotedPurchase",
                    "promotionalOffers",
                    "reviewNote",
                    "state",
                    "subscriptionAvailability",
                    "subscriptionLocalizations",
                    "subscriptionPeriod",
                ]
            ]
        ] = None,
        fields_territories: typing.Optional[
            typing.List[typing_extensions.Literal["currency"]]
        ] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal["availableTerritories", "subscription"]
            ]
        ] = None,
        limit_available_territories: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionAvailabilityResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_subscription_availabilities is not None:
            _query["fields[subscriptionAvailabilities]"] = encode_param(
                fields_subscription_availabilities, False
            )
        if fields_subscriptions is not None:
            _query["fields[subscriptions]"] = encode_param(fields_subscriptions, False)
        if fields_territories is not None:
            _query["fields[territories]"] = encode_param(fields_territories, False)
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit_available_territories is not None:
            _query["limit[availableTerritories]"] = encode_param(
                limit_available_territories, False
            )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/subscriptions/{id}/subscriptionAvailability",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.SubscriptionAvailabilityResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncSubscriptionAvailabilityClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        id: str,
        fields_subscription_availabilities: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "availableInNewTerritories", "availableTerritories", "subscription"
                ]
            ]
        ] = None,
        fields_subscriptions: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appStoreReviewScreenshot",
                    "familySharable",
                    "group",
                    "groupLevel",
                    "introductoryOffers",
                    "name",
                    "offerCodes",
                    "pricePoints",
                    "prices",
                    "productId",
                    "promotedPurchase",
                    "promotionalOffers",
                    "reviewNote",
                    "state",
                    "subscriptionAvailability",
                    "subscriptionLocalizations",
                    "subscriptionPeriod",
                ]
            ]
        ] = None,
        fields_territories: typing.Optional[
            typing.List[typing_extensions.Literal["currency"]]
        ] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal["availableTerritories", "subscription"]
            ]
        ] = None,
        limit_available_territories: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionAvailabilityResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_subscription_availabilities is not None:
            _query["fields[subscriptionAvailabilities]"] = encode_param(
                fields_subscription_availabilities, False
            )
        if fields_subscriptions is not None:
            _query["fields[subscriptions]"] = encode_param(fields_subscriptions, False)
        if fields_territories is not None:
            _query["fields[territories]"] = encode_param(fields_territories, False)
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit_available_territories is not None:
            _query["limit[availableTerritories]"] = encode_param(
                limit_available_territories, False
            )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/subscriptions/{id}/subscriptionAvailability",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.SubscriptionAvailabilityResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
