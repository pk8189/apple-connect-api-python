"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    default_request_options,
    to_encodable,
    encode_param,
    SyncBaseClient,
    RequestOptions,
    QueryParams,
    AsyncBaseClient,
)
from apple_python.resources.v1.subscription_promotional_offers.prices import (
    PricesClient,
    AsyncPricesClient,
)
import typing
import typing_extensions
from apple_python.types.v1.subscription_promotional_offers import models, params


class SubscriptionPromotionalOffersClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.prices = PricesClient(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.SubscriptionPromotionalOfferCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionPromotionalOfferResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerSubscriptionPromotionalOfferCreateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/v1/subscriptionPromotionalOffers",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.SubscriptionPromotionalOfferResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def patch(
        self,
        *,
        data: params.SubscriptionPromotionalOfferUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionPromotionalOfferResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerSubscriptionPromotionalOfferUpdateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="PATCH",
            path=f"/v1/subscriptionPromotionalOffers/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.SubscriptionPromotionalOfferResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def get(
        self,
        *,
        id: str,
        fields_subscription_promotional_offer_prices: typing.Optional[
            typing.List[
                typing_extensions.Literal["subscriptionPricePoint", "territory"]
            ]
        ] = None,
        fields_subscription_promotional_offers: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "duration",
                    "name",
                    "numberOfPeriods",
                    "offerCode",
                    "offerMode",
                    "prices",
                    "subscription",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[typing_extensions.Literal["prices", "subscription"]]
        ] = None,
        limit_prices: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionPromotionalOfferResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_subscription_promotional_offer_prices is not None:
            _query["fields[subscriptionPromotionalOfferPrices]"] = encode_param(
                fields_subscription_promotional_offer_prices, False
            )
        if fields_subscription_promotional_offers is not None:
            _query["fields[subscriptionPromotionalOffers]"] = encode_param(
                fields_subscription_promotional_offers, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit_prices is not None:
            _query["limit[prices]"] = encode_param(limit_prices, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/subscriptionPromotionalOffers/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.SubscriptionPromotionalOfferResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def delete(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="DELETE",
            path=f"/v1/subscriptionPromotionalOffers/{id}",
            auth_names=["itc-bearer-token"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncSubscriptionPromotionalOffersClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.prices = AsyncPricesClient(base_client=self._base_client)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.SubscriptionPromotionalOfferCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionPromotionalOfferResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerSubscriptionPromotionalOfferCreateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/v1/subscriptionPromotionalOffers",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.SubscriptionPromotionalOfferResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def patch(
        self,
        *,
        data: params.SubscriptionPromotionalOfferUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionPromotionalOfferResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerSubscriptionPromotionalOfferUpdateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="PATCH",
            path=f"/v1/subscriptionPromotionalOffers/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.SubscriptionPromotionalOfferResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def get(
        self,
        *,
        id: str,
        fields_subscription_promotional_offer_prices: typing.Optional[
            typing.List[
                typing_extensions.Literal["subscriptionPricePoint", "territory"]
            ]
        ] = None,
        fields_subscription_promotional_offers: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "duration",
                    "name",
                    "numberOfPeriods",
                    "offerCode",
                    "offerMode",
                    "prices",
                    "subscription",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[typing_extensions.Literal["prices", "subscription"]]
        ] = None,
        limit_prices: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionPromotionalOfferResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_subscription_promotional_offer_prices is not None:
            _query["fields[subscriptionPromotionalOfferPrices]"] = encode_param(
                fields_subscription_promotional_offer_prices, False
            )
        if fields_subscription_promotional_offers is not None:
            _query["fields[subscriptionPromotionalOffers]"] = encode_param(
                fields_subscription_promotional_offers, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit_prices is not None:
            _query["limit[prices]"] = encode_param(limit_prices, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/subscriptionPromotionalOffers/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.SubscriptionPromotionalOfferResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def delete(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="DELETE",
            path=f"/v1/subscriptionPromotionalOffers/{id}",
            auth_names=["itc-bearer-token"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)