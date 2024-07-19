"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    SyncBaseClient,
    default_request_options,
    QueryParams,
    AsyncBaseClient,
    RequestOptions,
    encode_param,
)
import typing
import typing_extensions
from apple_python.types.v2.app_availabilities.territory_availabilities import models


class TerritoryAvailabilitiesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        id: str,
        fields_territories: typing.Optional[
            typing.List[typing_extensions.Literal["currency"]]
        ] = None,
        fields_territory_availabilities: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "available",
                    "contentStatuses",
                    "preOrderEnabled",
                    "preOrderPublishDate",
                    "releaseDate",
                    "territory",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[typing_extensions.Literal["territory"]]
        ] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TerritoryAvailabilitiesResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_territories is not None:
            _query["fields[territories]"] = encode_param(fields_territories, False)
        if fields_territory_availabilities is not None:
            _query["fields[territoryAvailabilities]"] = encode_param(
                fields_territory_availabilities, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v2/appAvailabilities/{id}/territoryAvailabilities",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.TerritoryAvailabilitiesResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncTerritoryAvailabilitiesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        id: str,
        fields_territories: typing.Optional[
            typing.List[typing_extensions.Literal["currency"]]
        ] = None,
        fields_territory_availabilities: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "available",
                    "contentStatuses",
                    "preOrderEnabled",
                    "preOrderPublishDate",
                    "releaseDate",
                    "territory",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[typing_extensions.Literal["territory"]]
        ] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TerritoryAvailabilitiesResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_territories is not None:
            _query["fields[territories]"] = encode_param(fields_territories, False)
        if fields_territory_availabilities is not None:
            _query["fields[territoryAvailabilities]"] = encode_param(
                fields_territory_availabilities, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v2/appAvailabilities/{id}/territoryAvailabilities",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.TerritoryAvailabilitiesResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)