"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    to_encodable,
    default_request_options,
    AsyncBaseClient,
    encode_param,
    RequestOptions,
    QueryParams,
    SyncBaseClient,
)
from apple_python.resources.v1.subscription_offer_code_one_time_use_codes.values import (
    ValuesClient,
    AsyncValuesClient,
)
import typing
import typing_extensions
from apple_python.types.v1.subscription_offer_code_one_time_use_codes import (
    models,
    params,
)


class SubscriptionOfferCodeOneTimeUseCodesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.values = ValuesClient(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.SubscriptionOfferCodeOneTimeUseCodeCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionOfferCodeOneTimeUseCodeResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerSubscriptionOfferCodeOneTimeUseCodeCreateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/v1/subscriptionOfferCodeOneTimeUseCodes",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.SubscriptionOfferCodeOneTimeUseCodeResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def patch(
        self,
        *,
        data: params.SubscriptionOfferCodeOneTimeUseCodeUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionOfferCodeOneTimeUseCodeResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerSubscriptionOfferCodeOneTimeUseCodeUpdateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="PATCH",
            path=f"/v1/subscriptionOfferCodeOneTimeUseCodes/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.SubscriptionOfferCodeOneTimeUseCodeResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def get(
        self,
        *,
        id: str,
        fields_subscription_offer_code_one_time_use_codes: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "active",
                    "createdDate",
                    "expirationDate",
                    "numberOfCodes",
                    "offerCode",
                    "values",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[typing_extensions.Literal["offerCode"]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionOfferCodeOneTimeUseCodeResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_subscription_offer_code_one_time_use_codes is not None:
            _query["fields[subscriptionOfferCodeOneTimeUseCodes]"] = encode_param(
                fields_subscription_offer_code_one_time_use_codes, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/subscriptionOfferCodeOneTimeUseCodes/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.SubscriptionOfferCodeOneTimeUseCodeResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncSubscriptionOfferCodeOneTimeUseCodesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.values = AsyncValuesClient(base_client=self._base_client)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.SubscriptionOfferCodeOneTimeUseCodeCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionOfferCodeOneTimeUseCodeResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerSubscriptionOfferCodeOneTimeUseCodeCreateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/v1/subscriptionOfferCodeOneTimeUseCodes",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.SubscriptionOfferCodeOneTimeUseCodeResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def patch(
        self,
        *,
        data: params.SubscriptionOfferCodeOneTimeUseCodeUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionOfferCodeOneTimeUseCodeResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerSubscriptionOfferCodeOneTimeUseCodeUpdateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="PATCH",
            path=f"/v1/subscriptionOfferCodeOneTimeUseCodes/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.SubscriptionOfferCodeOneTimeUseCodeResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def get(
        self,
        *,
        id: str,
        fields_subscription_offer_code_one_time_use_codes: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "active",
                    "createdDate",
                    "expirationDate",
                    "numberOfCodes",
                    "offerCode",
                    "values",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[typing_extensions.Literal["offerCode"]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionOfferCodeOneTimeUseCodeResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_subscription_offer_code_one_time_use_codes is not None:
            _query["fields[subscriptionOfferCodeOneTimeUseCodes]"] = encode_param(
                fields_subscription_offer_code_one_time_use_codes, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/subscriptionOfferCodeOneTimeUseCodes/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.SubscriptionOfferCodeOneTimeUseCodeResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
