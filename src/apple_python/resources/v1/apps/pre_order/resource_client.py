"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    AsyncBaseClient,
    SyncBaseClient,
    default_request_options,
    QueryParams,
    encode_param,
    RequestOptions,
)
import typing
import typing_extensions
from apple_python.types.v1.apps.pre_order import models


class PreOrderClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        id: str,
        fields_app_pre_orders: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app", "appReleaseDate", "preOrderAvailableDate"
                ]
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppPreOrderWithoutIncludesResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_app_pre_orders is not None:
            _query["fields[appPreOrders]"] = encode_param(fields_app_pre_orders, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/apps/{id}/preOrder",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppPreOrderWithoutIncludesResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncPreOrderClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        id: str,
        fields_app_pre_orders: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app", "appReleaseDate", "preOrderAvailableDate"
                ]
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppPreOrderWithoutIncludesResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_app_pre_orders is not None:
            _query["fields[appPreOrders]"] = encode_param(fields_app_pre_orders, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/apps/{id}/preOrder",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppPreOrderWithoutIncludesResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
