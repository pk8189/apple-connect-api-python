"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    default_request_options,
    RequestOptions,
    encode_param,
    AsyncBaseClient,
    to_encodable,
    QueryParams,
    SyncBaseClient,
)
from apple_python.resources.v1.app_availabilities.available_territories import (
    AsyncAvailableTerritoriesClient,
    AvailableTerritoriesClient,
)
import typing
import typing_extensions
from apple_python.types.v1.app_availabilities import models, params


class AppAvailabilitiesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.available_territories = AvailableTerritoriesClient(
            base_client=self._base_client
        )

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.AppAvailabilityCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppAvailabilityResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerAppAvailabilityCreateRequest
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/v1/appAvailabilities",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.AppAvailabilityResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def get(
        self,
        *,
        id: str,
        fields_app_availabilities: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app", "availableInNewTerritories", "availableTerritories"
                ]
            ]
        ] = None,
        fields_territories: typing.Optional[
            typing.List[typing_extensions.Literal["currency"]]
        ] = None,
        include: typing.Optional[
            typing.List[typing_extensions.Literal["app", "availableTerritories"]]
        ] = None,
        limit_available_territories: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppAvailabilityResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_app_availabilities is not None:
            _query["fields[appAvailabilities]"] = encode_param(
                fields_app_availabilities, False
            )
        if fields_territories is not None:
            _query["fields[territories]"] = encode_param(fields_territories, False)
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit_available_territories is not None:
            _query["limit[availableTerritories]"] = encode_param(
                limit_available_territories, False
            )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/appAvailabilities/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppAvailabilityResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncAppAvailabilitiesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.available_territories = AsyncAvailableTerritoriesClient(
            base_client=self._base_client
        )

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.AppAvailabilityCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppAvailabilityResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerAppAvailabilityCreateRequest
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/v1/appAvailabilities",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.AppAvailabilityResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def get(
        self,
        *,
        id: str,
        fields_app_availabilities: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app", "availableInNewTerritories", "availableTerritories"
                ]
            ]
        ] = None,
        fields_territories: typing.Optional[
            typing.List[typing_extensions.Literal["currency"]]
        ] = None,
        include: typing.Optional[
            typing.List[typing_extensions.Literal["app", "availableTerritories"]]
        ] = None,
        limit_available_territories: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppAvailabilityResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_app_availabilities is not None:
            _query["fields[appAvailabilities]"] = encode_param(
                fields_app_availabilities, False
            )
        if fields_territories is not None:
            _query["fields[territories]"] = encode_param(fields_territories, False)
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit_available_territories is not None:
            _query["limit[availableTerritories]"] = encode_param(
                limit_available_territories, False
            )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/appAvailabilities/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppAvailabilityResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)