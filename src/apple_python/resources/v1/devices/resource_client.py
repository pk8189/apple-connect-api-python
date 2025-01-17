"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    QueryParams,
    AsyncBaseClient,
    to_encodable,
    encode_param,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
import typing
import typing_extensions
from apple_python.types.v1.devices import models, params


class DevicesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.DeviceCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeviceResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(item=data, dump_with=params._SerializerDeviceCreateRequest)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/v1/devices",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.DeviceResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def patch(
        self,
        *,
        data: params.DeviceUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeviceResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(item=data, dump_with=params._SerializerDeviceUpdateRequest)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="PATCH",
            path=f"/v1/devices/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.DeviceResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def get(
        self,
        *,
        id: str,
        fields_devices: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "addedDate",
                    "deviceClass",
                    "model",
                    "name",
                    "platform",
                    "status",
                    "udid",
                ]
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeviceResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_devices is not None:
            _query["fields[devices]"] = encode_param(fields_devices, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/devices/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.DeviceResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def list(
        self,
        *,
        fields_devices: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "addedDate",
                    "deviceClass",
                    "model",
                    "name",
                    "platform",
                    "status",
                    "udid",
                ]
            ]
        ] = None,
        filter_id: typing.Optional[typing.List[str]] = None,
        filter_name: typing.Optional[typing.List[str]] = None,
        filter_platform: typing.Optional[
            typing.List[typing_extensions.Literal["IOS", "MAC_OS"]]
        ] = None,
        filter_status: typing.Optional[
            typing.List[typing_extensions.Literal["ENABLED", "DISABLED"]]
        ] = None,
        filter_udid: typing.Optional[typing.List[str]] = None,
        limit: typing.Optional[int] = None,
        sort: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "id",
                    "-id",
                    "name",
                    "-name",
                    "platform",
                    "-platform",
                    "status",
                    "-status",
                    "udid",
                    "-udid",
                ]
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DevicesResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_devices is not None:
            _query["fields[devices]"] = encode_param(fields_devices, False)
        if filter_id is not None:
            _query["filter[id]"] = encode_param(filter_id, False)
        if filter_name is not None:
            _query["filter[name]"] = encode_param(filter_name, False)
        if filter_platform is not None:
            _query["filter[platform]"] = encode_param(filter_platform, False)
        if filter_status is not None:
            _query["filter[status]"] = encode_param(filter_status, False)
        if filter_udid is not None:
            _query["filter[udid]"] = encode_param(filter_udid, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        if sort is not None:
            _query["sort"] = encode_param(sort, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path="/v1/devices",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.DevicesResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncDevicesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.DeviceCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeviceResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(item=data, dump_with=params._SerializerDeviceCreateRequest)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/v1/devices",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.DeviceResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def patch(
        self,
        *,
        data: params.DeviceUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeviceResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(item=data, dump_with=params._SerializerDeviceUpdateRequest)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="PATCH",
            path=f"/v1/devices/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.DeviceResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def get(
        self,
        *,
        id: str,
        fields_devices: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "addedDate",
                    "deviceClass",
                    "model",
                    "name",
                    "platform",
                    "status",
                    "udid",
                ]
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeviceResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_devices is not None:
            _query["fields[devices]"] = encode_param(fields_devices, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/devices/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.DeviceResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def list(
        self,
        *,
        fields_devices: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "addedDate",
                    "deviceClass",
                    "model",
                    "name",
                    "platform",
                    "status",
                    "udid",
                ]
            ]
        ] = None,
        filter_id: typing.Optional[typing.List[str]] = None,
        filter_name: typing.Optional[typing.List[str]] = None,
        filter_platform: typing.Optional[
            typing.List[typing_extensions.Literal["IOS", "MAC_OS"]]
        ] = None,
        filter_status: typing.Optional[
            typing.List[typing_extensions.Literal["ENABLED", "DISABLED"]]
        ] = None,
        filter_udid: typing.Optional[typing.List[str]] = None,
        limit: typing.Optional[int] = None,
        sort: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "id",
                    "-id",
                    "name",
                    "-name",
                    "platform",
                    "-platform",
                    "status",
                    "-status",
                    "udid",
                    "-udid",
                ]
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DevicesResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_devices is not None:
            _query["fields[devices]"] = encode_param(fields_devices, False)
        if filter_id is not None:
            _query["filter[id]"] = encode_param(filter_id, False)
        if filter_name is not None:
            _query["filter[name]"] = encode_param(filter_name, False)
        if filter_platform is not None:
            _query["filter[platform]"] = encode_param(filter_platform, False)
        if filter_status is not None:
            _query["filter[status]"] = encode_param(filter_status, False)
        if filter_udid is not None:
            _query["filter[udid]"] = encode_param(filter_udid, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        if sort is not None:
            _query["sort"] = encode_param(sort, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path="/v1/devices",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.DevicesResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
