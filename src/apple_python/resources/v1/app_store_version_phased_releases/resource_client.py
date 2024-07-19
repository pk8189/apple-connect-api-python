"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    AsyncBaseClient,
    SyncBaseClient,
    to_encodable,
    default_request_options,
    RequestOptions,
)
import typing
from apple_python.types.v1.app_store_version_phased_releases import params, models


class AppStoreVersionPhasedReleasesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.AppStoreVersionPhasedReleaseCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppStoreVersionPhasedReleaseResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerAppStoreVersionPhasedReleaseCreateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/v1/appStoreVersionPhasedReleases",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.AppStoreVersionPhasedReleaseResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def patch(
        self,
        *,
        data: params.AppStoreVersionPhasedReleaseUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppStoreVersionPhasedReleaseResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerAppStoreVersionPhasedReleaseUpdateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="PATCH",
            path=f"/v1/appStoreVersionPhasedReleases/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.AppStoreVersionPhasedReleaseResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def delete(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="DELETE",
            path=f"/v1/appStoreVersionPhasedReleases/{id}",
            auth_names=["itc-bearer-token"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncAppStoreVersionPhasedReleasesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.AppStoreVersionPhasedReleaseCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppStoreVersionPhasedReleaseResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerAppStoreVersionPhasedReleaseCreateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/v1/appStoreVersionPhasedReleases",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.AppStoreVersionPhasedReleaseResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def patch(
        self,
        *,
        data: params.AppStoreVersionPhasedReleaseUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppStoreVersionPhasedReleaseResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerAppStoreVersionPhasedReleaseUpdateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="PATCH",
            path=f"/v1/appStoreVersionPhasedReleases/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.AppStoreVersionPhasedReleaseResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def delete(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="DELETE",
            path=f"/v1/appStoreVersionPhasedReleases/{id}",
            auth_names=["itc-bearer-token"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
