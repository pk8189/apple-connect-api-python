"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    SyncBaseClient,
    RequestOptions,
    AsyncBaseClient,
    encode_param,
    default_request_options,
    QueryParams,
)
import typing
from apple_python.types.v1.builds.metrics.beta_build_usages import models


class BetaBuildUsagesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        id: str,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BetaBuildUsagesV1MetricResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/builds/{id}/metrics/betaBuildUsages",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.BetaBuildUsagesV1MetricResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncBetaBuildUsagesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        id: str,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BetaBuildUsagesV1MetricResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/builds/{id}/metrics/betaBuildUsages",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.BetaBuildUsagesV1MetricResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
