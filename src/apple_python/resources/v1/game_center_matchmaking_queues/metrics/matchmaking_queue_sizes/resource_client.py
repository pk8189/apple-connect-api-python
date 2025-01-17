"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    SyncBaseClient,
    encode_param,
    RequestOptions,
    AsyncBaseClient,
    QueryParams,
    default_request_options,
)
import typing_extensions
import typing
from apple_python.types.v1.game_center_matchmaking_queues.metrics.matchmaking_queue_sizes import (
    models,
)


class MatchmakingQueueSizesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        id: str,
        granularity: typing_extensions.Literal["P1D", "PT1H", "PT15M"],
        limit: typing.Optional[int] = None,
        sort: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "averageNumberOfRequests",
                    "-averageNumberOfRequests",
                    "count",
                    "-count",
                    "p50NumberOfRequests",
                    "-p50NumberOfRequests",
                    "p95NumberOfRequests",
                    "-p95NumberOfRequests",
                ]
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterMatchmakingQueueSizesV1MetricResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        _query["granularity"] = encode_param(granularity, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        if sort is not None:
            _query["sort"] = encode_param(sort, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/gameCenterMatchmakingQueues/{id}/metrics/matchmakingQueueSizes",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.GameCenterMatchmakingQueueSizesV1MetricResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncMatchmakingQueueSizesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        id: str,
        granularity: typing_extensions.Literal["P1D", "PT1H", "PT15M"],
        limit: typing.Optional[int] = None,
        sort: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "averageNumberOfRequests",
                    "-averageNumberOfRequests",
                    "count",
                    "-count",
                    "p50NumberOfRequests",
                    "-p50NumberOfRequests",
                    "p95NumberOfRequests",
                    "-p95NumberOfRequests",
                ]
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterMatchmakingQueueSizesV1MetricResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        _query["granularity"] = encode_param(granularity, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        if sort is not None:
            _query["sort"] = encode_param(sort, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/gameCenterMatchmakingQueues/{id}/metrics/matchmakingQueueSizes",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.GameCenterMatchmakingQueueSizesV1MetricResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
