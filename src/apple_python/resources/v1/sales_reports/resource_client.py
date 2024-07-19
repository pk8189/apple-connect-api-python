"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    RequestOptions,
    default_request_options,
    QueryParams,
    SyncBaseClient,
    encode_param,
    AsyncBaseClient,
)
import typing
import typing_extensions
from apple_python.types.binary_response import BinaryResponse


class SalesReportsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        filter_frequency: typing.List[
            typing_extensions.Literal["DAILY", "WEEKLY", "MONTHLY", "YEARLY"]
        ],
        filter_report_sub_type: typing.List[
            typing_extensions.Literal[
                "SUMMARY",
                "DETAILED",
                "SUMMARY_INSTALL_TYPE",
                "SUMMARY_TERRITORY",
                "SUMMARY_CHANNEL",
            ]
        ],
        filter_report_type: typing.List[
            typing_extensions.Literal[
                "SALES",
                "PRE_ORDER",
                "NEWSSTAND",
                "SUBSCRIPTION",
                "SUBSCRIPTION_EVENT",
                "SUBSCRIBER",
                "SUBSCRIPTION_OFFER_CODE_REDEMPTION",
                "INSTALLS",
                "FIRST_ANNUAL",
            ]
        ],
        filter_vendor_number: typing.List[str],
        filter_report_date: typing.Optional[typing.List[str]] = None,
        filter_version: typing.Optional[typing.List[str]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BinaryResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        _query["filter[frequency]"] = encode_param(filter_frequency, False)
        _query["filter[reportSubType]"] = encode_param(filter_report_sub_type, False)
        _query["filter[reportType]"] = encode_param(filter_report_type, False)
        _query["filter[vendorNumber]"] = encode_param(filter_vendor_number, False)
        if filter_report_date is not None:
            _query["filter[reportDate]"] = encode_param(filter_report_date, False)
        if filter_version is not None:
            _query["filter[version]"] = encode_param(filter_version, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path="/v1/salesReports",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncSalesReportsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        filter_frequency: typing.List[
            typing_extensions.Literal["DAILY", "WEEKLY", "MONTHLY", "YEARLY"]
        ],
        filter_report_sub_type: typing.List[
            typing_extensions.Literal[
                "SUMMARY",
                "DETAILED",
                "SUMMARY_INSTALL_TYPE",
                "SUMMARY_TERRITORY",
                "SUMMARY_CHANNEL",
            ]
        ],
        filter_report_type: typing.List[
            typing_extensions.Literal[
                "SALES",
                "PRE_ORDER",
                "NEWSSTAND",
                "SUBSCRIPTION",
                "SUBSCRIPTION_EVENT",
                "SUBSCRIBER",
                "SUBSCRIPTION_OFFER_CODE_REDEMPTION",
                "INSTALLS",
                "FIRST_ANNUAL",
            ]
        ],
        filter_vendor_number: typing.List[str],
        filter_report_date: typing.Optional[typing.List[str]] = None,
        filter_version: typing.Optional[typing.List[str]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BinaryResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        _query["filter[frequency]"] = encode_param(filter_frequency, False)
        _query["filter[reportSubType]"] = encode_param(filter_report_sub_type, False)
        _query["filter[reportType]"] = encode_param(filter_report_type, False)
        _query["filter[vendorNumber]"] = encode_param(filter_vendor_number, False)
        if filter_report_date is not None:
            _query["filter[reportDate]"] = encode_param(filter_report_date, False)
        if filter_version is not None:
            _query["filter[version]"] = encode_param(filter_version, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path="/v1/salesReports",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
