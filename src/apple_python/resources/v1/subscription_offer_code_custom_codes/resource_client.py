"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    RequestOptions,
    to_encodable,
    default_request_options,
    SyncBaseClient,
    encode_param,
    AsyncBaseClient,
    QueryParams,
)
import typing
import typing_extensions
from apple_python.types.v1.subscription_offer_code_custom_codes import params, models


class SubscriptionOfferCodeCustomCodesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.SubscriptionOfferCodeCustomCodeCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionOfferCodeCustomCodeResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerSubscriptionOfferCodeCustomCodeCreateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/v1/subscriptionOfferCodeCustomCodes",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.SubscriptionOfferCodeCustomCodeResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def patch(
        self,
        *,
        data: params.SubscriptionOfferCodeCustomCodeUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionOfferCodeCustomCodeResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerSubscriptionOfferCodeCustomCodeUpdateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="PATCH",
            path=f"/v1/subscriptionOfferCodeCustomCodes/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.SubscriptionOfferCodeCustomCodeResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def get(
        self,
        *,
        id: str,
        fields_subscription_offer_code_custom_codes: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "active",
                    "createdDate",
                    "customCode",
                    "expirationDate",
                    "numberOfCodes",
                    "offerCode",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[typing_extensions.Literal["offerCode"]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionOfferCodeCustomCodeResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_subscription_offer_code_custom_codes is not None:
            _query["fields[subscriptionOfferCodeCustomCodes]"] = encode_param(
                fields_subscription_offer_code_custom_codes, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/subscriptionOfferCodeCustomCodes/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.SubscriptionOfferCodeCustomCodeResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncSubscriptionOfferCodeCustomCodesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.SubscriptionOfferCodeCustomCodeCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionOfferCodeCustomCodeResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerSubscriptionOfferCodeCustomCodeCreateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/v1/subscriptionOfferCodeCustomCodes",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.SubscriptionOfferCodeCustomCodeResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def patch(
        self,
        *,
        data: params.SubscriptionOfferCodeCustomCodeUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionOfferCodeCustomCodeResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerSubscriptionOfferCodeCustomCodeUpdateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="PATCH",
            path=f"/v1/subscriptionOfferCodeCustomCodes/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.SubscriptionOfferCodeCustomCodeResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def get(
        self,
        *,
        id: str,
        fields_subscription_offer_code_custom_codes: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "active",
                    "createdDate",
                    "customCode",
                    "expirationDate",
                    "numberOfCodes",
                    "offerCode",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[typing_extensions.Literal["offerCode"]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionOfferCodeCustomCodeResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_subscription_offer_code_custom_codes is not None:
            _query["fields[subscriptionOfferCodeCustomCodes]"] = encode_param(
                fields_subscription_offer_code_custom_codes, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/subscriptionOfferCodeCustomCodes/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.SubscriptionOfferCodeCustomCodeResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
