"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    QueryParams,
    default_request_options,
    AsyncBaseClient,
    SyncBaseClient,
    encode_param,
    RequestOptions,
)
import typing
import typing_extensions
from apple_python.types.v1.subscription_offer_codes.prices import models


class PricesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        id: str,
        fields_subscription_offer_code_prices: typing.Optional[
            typing.List[
                typing_extensions.Literal["subscriptionPricePoint", "territory"]
            ]
        ] = None,
        fields_subscription_price_points: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "customerPrice",
                    "equalizations",
                    "proceeds",
                    "proceedsYear2",
                    "subscription",
                    "territory",
                ]
            ]
        ] = None,
        fields_territories: typing.Optional[
            typing.List[typing_extensions.Literal["currency"]]
        ] = None,
        filter_territory: typing.Optional[typing.List[str]] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal["subscriptionPricePoint", "territory"]
            ]
        ] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionOfferCodePricesResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_subscription_offer_code_prices is not None:
            _query["fields[subscriptionOfferCodePrices]"] = encode_param(
                fields_subscription_offer_code_prices, False
            )
        if fields_subscription_price_points is not None:
            _query["fields[subscriptionPricePoints]"] = encode_param(
                fields_subscription_price_points, False
            )
        if fields_territories is not None:
            _query["fields[territories]"] = encode_param(fields_territories, False)
        if filter_territory is not None:
            _query["filter[territory]"] = encode_param(filter_territory, False)
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/subscriptionOfferCodes/{id}/prices",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.SubscriptionOfferCodePricesResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncPricesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        id: str,
        fields_subscription_offer_code_prices: typing.Optional[
            typing.List[
                typing_extensions.Literal["subscriptionPricePoint", "territory"]
            ]
        ] = None,
        fields_subscription_price_points: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "customerPrice",
                    "equalizations",
                    "proceeds",
                    "proceedsYear2",
                    "subscription",
                    "territory",
                ]
            ]
        ] = None,
        fields_territories: typing.Optional[
            typing.List[typing_extensions.Literal["currency"]]
        ] = None,
        filter_territory: typing.Optional[typing.List[str]] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal["subscriptionPricePoint", "territory"]
            ]
        ] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionOfferCodePricesResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_subscription_offer_code_prices is not None:
            _query["fields[subscriptionOfferCodePrices]"] = encode_param(
                fields_subscription_offer_code_prices, False
            )
        if fields_subscription_price_points is not None:
            _query["fields[subscriptionPricePoints]"] = encode_param(
                fields_subscription_price_points, False
            )
        if fields_territories is not None:
            _query["fields[territories]"] = encode_param(fields_territories, False)
        if filter_territory is not None:
            _query["filter[territory]"] = encode_param(filter_territory, False)
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/subscriptionOfferCodes/{id}/prices",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.SubscriptionOfferCodePricesResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
