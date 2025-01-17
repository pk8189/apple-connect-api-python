"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    RequestOptions,
    encode_param,
    default_request_options,
    to_encodable,
    QueryParams,
    SyncBaseClient,
    AsyncBaseClient,
)
import typing
import typing_extensions
from apple_python.types.v1.subscription_grace_periods import models, params


class SubscriptionGracePeriodsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def patch(
        self,
        *,
        data: params.SubscriptionGracePeriodUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionGracePeriodResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerSubscriptionGracePeriodUpdateRequest
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="PATCH",
            path=f"/v1/subscriptionGracePeriods/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.SubscriptionGracePeriodResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def get(
        self,
        *,
        id: str,
        fields_subscription_grace_periods: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "duration", "optIn", "renewalType", "sandboxOptIn"
                ]
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionGracePeriodResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_subscription_grace_periods is not None:
            _query["fields[subscriptionGracePeriods]"] = encode_param(
                fields_subscription_grace_periods, False
            )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/subscriptionGracePeriods/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.SubscriptionGracePeriodResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncSubscriptionGracePeriodsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def patch(
        self,
        *,
        data: params.SubscriptionGracePeriodUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionGracePeriodResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerSubscriptionGracePeriodUpdateRequest
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="PATCH",
            path=f"/v1/subscriptionGracePeriods/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.SubscriptionGracePeriodResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def get(
        self,
        *,
        id: str,
        fields_subscription_grace_periods: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "duration", "optIn", "renewalType", "sandboxOptIn"
                ]
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionGracePeriodResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_subscription_grace_periods is not None:
            _query["fields[subscriptionGracePeriods]"] = encode_param(
                fields_subscription_grace_periods, False
            )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/subscriptionGracePeriods/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.SubscriptionGracePeriodResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
