"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    SyncBaseClient,
    RequestOptions,
    AsyncBaseClient,
    default_request_options,
    encode_param,
    QueryParams,
)
import typing
import typing_extensions
from apple_python.types.v1.analytics_reports.instances import models


class InstancesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        id: str,
        fields_analytics_report_instances: typing.Optional[
            typing.List[
                typing_extensions.Literal["granularity", "processingDate", "segments"]
            ]
        ] = None,
        filter_granularity: typing.Optional[
            typing.List[typing_extensions.Literal["DAILY", "WEEKLY", "MONTHLY"]]
        ] = None,
        filter_processing_date: typing.Optional[typing.List[str]] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AnalyticsReportInstancesResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_analytics_report_instances is not None:
            _query["fields[analyticsReportInstances]"] = encode_param(
                fields_analytics_report_instances, False
            )
        if filter_granularity is not None:
            _query["filter[granularity]"] = encode_param(filter_granularity, False)
        if filter_processing_date is not None:
            _query["filter[processingDate]"] = encode_param(
                filter_processing_date, False
            )
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/analyticsReports/{id}/instances",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AnalyticsReportInstancesResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncInstancesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        id: str,
        fields_analytics_report_instances: typing.Optional[
            typing.List[
                typing_extensions.Literal["granularity", "processingDate", "segments"]
            ]
        ] = None,
        filter_granularity: typing.Optional[
            typing.List[typing_extensions.Literal["DAILY", "WEEKLY", "MONTHLY"]]
        ] = None,
        filter_processing_date: typing.Optional[typing.List[str]] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AnalyticsReportInstancesResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_analytics_report_instances is not None:
            _query["fields[analyticsReportInstances]"] = encode_param(
                fields_analytics_report_instances, False
            )
        if filter_granularity is not None:
            _query["filter[granularity]"] = encode_param(filter_granularity, False)
        if filter_processing_date is not None:
            _query["filter[processingDate]"] = encode_param(
                filter_processing_date, False
            )
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/analyticsReports/{id}/instances",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AnalyticsReportInstancesResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
