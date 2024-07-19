"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    encode_param,
    default_request_options,
    SyncBaseClient,
    AsyncBaseClient,
    RequestOptions,
    QueryParams,
)
from apple_python.resources.v1.analytics_report_instances.segments import (
    AsyncSegmentsClient,
    SegmentsClient,
)
import typing
import typing_extensions
from apple_python.types.v1.analytics_report_instances import models


class AnalyticsReportInstancesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.segments = SegmentsClient(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)
    def get(
        self,
        *,
        id: str,
        fields_analytics_report_instances: typing.Optional[
            typing.List[
                typing_extensions.Literal["granularity", "processingDate", "segments"]
            ]
        ] = None,
        fields_analytics_report_segments: typing.Optional[
            typing.List[typing_extensions.Literal["checksum", "sizeInBytes", "url"]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AnalyticsReportInstanceResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_analytics_report_instances is not None:
            _query["fields[analyticsReportInstances]"] = encode_param(
                fields_analytics_report_instances, False
            )
        if fields_analytics_report_segments is not None:
            _query["fields[analyticsReportSegments]"] = encode_param(
                fields_analytics_report_segments, False
            )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/analyticsReportInstances/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AnalyticsReportInstanceResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncAnalyticsReportInstancesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.segments = AsyncSegmentsClient(base_client=self._base_client)

    # register async api methods (keep comment for code generation)
    async def get(
        self,
        *,
        id: str,
        fields_analytics_report_instances: typing.Optional[
            typing.List[
                typing_extensions.Literal["granularity", "processingDate", "segments"]
            ]
        ] = None,
        fields_analytics_report_segments: typing.Optional[
            typing.List[typing_extensions.Literal["checksum", "sizeInBytes", "url"]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AnalyticsReportInstanceResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_analytics_report_instances is not None:
            _query["fields[analyticsReportInstances]"] = encode_param(
                fields_analytics_report_instances, False
            )
        if fields_analytics_report_segments is not None:
            _query["fields[analyticsReportSegments]"] = encode_param(
                fields_analytics_report_segments, False
            )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/analyticsReportInstances/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AnalyticsReportInstanceResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
