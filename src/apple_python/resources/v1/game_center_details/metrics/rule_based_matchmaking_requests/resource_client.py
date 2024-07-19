"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    AsyncBaseClient,
    RequestOptions,
    QueryParams,
    SyncBaseClient,
    encode_param,
    default_request_options,
)
import typing_extensions
import typing
from apple_python.types.v1.game_center_details.metrics.rule_based_matchmaking_requests import (
    models,
)


class RuleBasedMatchmakingRequestsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        id: str,
        granularity: typing_extensions.Literal["P1D", "PT1H", "PT15M"],
        filter_result: typing.Optional[
            typing_extensions.Literal["MATCHED", "CANCELED", "EXPIRED"]
        ] = None,
        group_by: typing.Optional[
            typing.List[typing_extensions.Literal["result"]]
        ] = None,
        limit: typing.Optional[int] = None,
        sort: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "averageSecondsInQueue",
                    "-averageSecondsInQueue",
                    "count",
                    "-count",
                    "p50SecondsInQueue",
                    "-p50SecondsInQueue",
                    "p95SecondsInQueue",
                    "-p95SecondsInQueue",
                ]
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterMatchmakingAppRequestsV1MetricResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        _query["granularity"] = encode_param(granularity, False)
        if filter_result is not None:
            _query["filter[result]"] = encode_param(filter_result, False)
        if group_by is not None:
            _query["groupBy"] = encode_param(group_by, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        if sort is not None:
            _query["sort"] = encode_param(sort, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/gameCenterDetails/{id}/metrics/ruleBasedMatchmakingRequests",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.GameCenterMatchmakingAppRequestsV1MetricResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncRuleBasedMatchmakingRequestsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        id: str,
        granularity: typing_extensions.Literal["P1D", "PT1H", "PT15M"],
        filter_result: typing.Optional[
            typing_extensions.Literal["MATCHED", "CANCELED", "EXPIRED"]
        ] = None,
        group_by: typing.Optional[
            typing.List[typing_extensions.Literal["result"]]
        ] = None,
        limit: typing.Optional[int] = None,
        sort: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "averageSecondsInQueue",
                    "-averageSecondsInQueue",
                    "count",
                    "-count",
                    "p50SecondsInQueue",
                    "-p50SecondsInQueue",
                    "p95SecondsInQueue",
                    "-p95SecondsInQueue",
                ]
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterMatchmakingAppRequestsV1MetricResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        _query["granularity"] = encode_param(granularity, False)
        if filter_result is not None:
            _query["filter[result]"] = encode_param(filter_result, False)
        if group_by is not None:
            _query["groupBy"] = encode_param(group_by, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        if sort is not None:
            _query["sort"] = encode_param(sort, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/gameCenterDetails/{id}/metrics/ruleBasedMatchmakingRequests",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.GameCenterMatchmakingAppRequestsV1MetricResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
