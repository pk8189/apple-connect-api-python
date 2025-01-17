"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    encode_param,
    QueryParams,
    RequestOptions,
    AsyncBaseClient,
    default_request_options,
    SyncBaseClient,
)
import typing
import typing_extensions
from apple_python.types.v1.builds.perf_power_metrics import models


class PerfPowerMetricsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        id: str,
        filter_device_type: typing.Optional[typing.List[str]] = None,
        filter_metric_type: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "DISK",
                    "HANG",
                    "BATTERY",
                    "LAUNCH",
                    "MEMORY",
                    "ANIMATION",
                    "TERMINATION",
                ]
            ]
        ] = None,
        filter_platform: typing.Optional[
            typing.List[typing_extensions.Literal["IOS"]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.XcodeMetrics:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if filter_device_type is not None:
            _query["filter[deviceType]"] = encode_param(filter_device_type, False)
        if filter_metric_type is not None:
            _query["filter[metricType]"] = encode_param(filter_metric_type, False)
        if filter_platform is not None:
            _query["filter[platform]"] = encode_param(filter_platform, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/builds/{id}/perfPowerMetrics",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.XcodeMetrics,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncPerfPowerMetricsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        id: str,
        filter_device_type: typing.Optional[typing.List[str]] = None,
        filter_metric_type: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "DISK",
                    "HANG",
                    "BATTERY",
                    "LAUNCH",
                    "MEMORY",
                    "ANIMATION",
                    "TERMINATION",
                ]
            ]
        ] = None,
        filter_platform: typing.Optional[
            typing.List[typing_extensions.Literal["IOS"]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.XcodeMetrics:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if filter_device_type is not None:
            _query["filter[deviceType]"] = encode_param(filter_device_type, False)
        if filter_metric_type is not None:
            _query["filter[metricType]"] = encode_param(filter_metric_type, False)
        if filter_platform is not None:
            _query["filter[platform]"] = encode_param(filter_platform, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/builds/{id}/perfPowerMetrics",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.XcodeMetrics,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
