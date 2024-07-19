"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    SyncBaseClient,
    encode_param,
    default_request_options,
    AsyncBaseClient,
    RequestOptions,
    QueryParams,
)
import typing
import typing_extensions
from apple_python.types.binary_response import BinaryResponse


class FinanceReportsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        filter_region_code: typing.List[str],
        filter_report_date: typing.List[str],
        filter_report_type: typing.List[
            typing_extensions.Literal["FINANCIAL", "FINANCE_DETAIL"]
        ],
        filter_vendor_number: typing.List[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BinaryResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        _query["filter[regionCode]"] = encode_param(filter_region_code, False)
        _query["filter[reportDate]"] = encode_param(filter_report_date, False)
        _query["filter[reportType]"] = encode_param(filter_report_type, False)
        _query["filter[vendorNumber]"] = encode_param(filter_vendor_number, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path="/v1/financeReports",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncFinanceReportsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        filter_region_code: typing.List[str],
        filter_report_date: typing.List[str],
        filter_report_type: typing.List[
            typing_extensions.Literal["FINANCIAL", "FINANCE_DETAIL"]
        ],
        filter_vendor_number: typing.List[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BinaryResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        _query["filter[regionCode]"] = encode_param(filter_region_code, False)
        _query["filter[reportDate]"] = encode_param(filter_report_date, False)
        _query["filter[reportType]"] = encode_param(filter_report_type, False)
        _query["filter[vendorNumber]"] = encode_param(filter_vendor_number, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path="/v1/financeReports",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
