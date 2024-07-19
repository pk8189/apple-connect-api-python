"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    encode_param,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    AsyncBaseClient,
    default_request_options,
)
import typing
import typing_extensions
from apple_python.types.v1.app_price_schedules.manual_prices import models


class ManualPricesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        id: str,
        fields_app_price_points: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app", "customerPrice", "equalizations", "proceeds", "territory"
                ]
            ]
        ] = None,
        fields_app_prices: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appPricePoint", "endDate", "manual", "startDate", "territory"
                ]
            ]
        ] = None,
        fields_territories: typing.Optional[
            typing.List[typing_extensions.Literal["currency"]]
        ] = None,
        filter_end_date: typing.Optional[typing.List[str]] = None,
        filter_start_date: typing.Optional[typing.List[str]] = None,
        filter_territory: typing.Optional[typing.List[str]] = None,
        include: typing.Optional[
            typing.List[typing_extensions.Literal["appPricePoint", "territory"]]
        ] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppPricesV2Response:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_app_price_points is not None:
            _query["fields[appPricePoints]"] = encode_param(
                fields_app_price_points, False
            )
        if fields_app_prices is not None:
            _query["fields[appPrices]"] = encode_param(fields_app_prices, False)
        if fields_territories is not None:
            _query["fields[territories]"] = encode_param(fields_territories, False)
        if filter_end_date is not None:
            _query["filter[endDate]"] = encode_param(filter_end_date, False)
        if filter_start_date is not None:
            _query["filter[startDate]"] = encode_param(filter_start_date, False)
        if filter_territory is not None:
            _query["filter[territory]"] = encode_param(filter_territory, False)
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/appPriceSchedules/{id}/manualPrices",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppPricesV2Response,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncManualPricesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        id: str,
        fields_app_price_points: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app", "customerPrice", "equalizations", "proceeds", "territory"
                ]
            ]
        ] = None,
        fields_app_prices: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appPricePoint", "endDate", "manual", "startDate", "territory"
                ]
            ]
        ] = None,
        fields_territories: typing.Optional[
            typing.List[typing_extensions.Literal["currency"]]
        ] = None,
        filter_end_date: typing.Optional[typing.List[str]] = None,
        filter_start_date: typing.Optional[typing.List[str]] = None,
        filter_territory: typing.Optional[typing.List[str]] = None,
        include: typing.Optional[
            typing.List[typing_extensions.Literal["appPricePoint", "territory"]]
        ] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppPricesV2Response:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_app_price_points is not None:
            _query["fields[appPricePoints]"] = encode_param(
                fields_app_price_points, False
            )
        if fields_app_prices is not None:
            _query["fields[appPrices]"] = encode_param(fields_app_prices, False)
        if fields_territories is not None:
            _query["fields[territories]"] = encode_param(fields_territories, False)
        if filter_end_date is not None:
            _query["filter[endDate]"] = encode_param(filter_end_date, False)
        if filter_start_date is not None:
            _query["filter[startDate]"] = encode_param(filter_start_date, False)
        if filter_territory is not None:
            _query["filter[territory]"] = encode_param(filter_territory, False)
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/appPriceSchedules/{id}/manualPrices",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppPricesV2Response,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
