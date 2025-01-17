"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    default_request_options,
    RequestOptions,
    QueryParams,
    SyncBaseClient,
    AsyncBaseClient,
    encode_param,
)
import typing
import typing_extensions
from apple_python.types.v1.apps.analytics_report_requests import models


class AnalyticsReportRequestsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        id: str,
        fields_analytics_report_requests: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "accessType", "app", "reports", "stoppedDueToInactivity"
                ]
            ]
        ] = None,
        fields_analytics_reports: typing.Optional[
            typing.List[typing_extensions.Literal["category", "instances", "name"]]
        ] = None,
        filter_access_type: typing.Optional[
            typing.List[typing_extensions.Literal["ONE_TIME_SNAPSHOT", "ONGOING"]]
        ] = None,
        include: typing.Optional[
            typing.List[typing_extensions.Literal["reports"]]
        ] = None,
        limit: typing.Optional[int] = None,
        limit_reports: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AnalyticsReportRequestsResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_analytics_report_requests is not None:
            _query["fields[analyticsReportRequests]"] = encode_param(
                fields_analytics_report_requests, False
            )
        if fields_analytics_reports is not None:
            _query["fields[analyticsReports]"] = encode_param(
                fields_analytics_reports, False
            )
        if filter_access_type is not None:
            _query["filter[accessType]"] = encode_param(filter_access_type, False)
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        if limit_reports is not None:
            _query["limit[reports]"] = encode_param(limit_reports, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/apps/{id}/analyticsReportRequests",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AnalyticsReportRequestsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncAnalyticsReportRequestsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        id: str,
        fields_analytics_report_requests: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "accessType", "app", "reports", "stoppedDueToInactivity"
                ]
            ]
        ] = None,
        fields_analytics_reports: typing.Optional[
            typing.List[typing_extensions.Literal["category", "instances", "name"]]
        ] = None,
        filter_access_type: typing.Optional[
            typing.List[typing_extensions.Literal["ONE_TIME_SNAPSHOT", "ONGOING"]]
        ] = None,
        include: typing.Optional[
            typing.List[typing_extensions.Literal["reports"]]
        ] = None,
        limit: typing.Optional[int] = None,
        limit_reports: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AnalyticsReportRequestsResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_analytics_report_requests is not None:
            _query["fields[analyticsReportRequests]"] = encode_param(
                fields_analytics_report_requests, False
            )
        if fields_analytics_reports is not None:
            _query["fields[analyticsReports]"] = encode_param(
                fields_analytics_reports, False
            )
        if filter_access_type is not None:
            _query["filter[accessType]"] = encode_param(filter_access_type, False)
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        if limit_reports is not None:
            _query["limit[reports]"] = encode_param(limit_reports, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/apps/{id}/analyticsReportRequests",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AnalyticsReportRequestsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
