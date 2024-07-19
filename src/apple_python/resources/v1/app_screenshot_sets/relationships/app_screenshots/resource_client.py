"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    QueryParams,
    default_request_options,
    to_encodable,
    RequestOptions,
    SyncBaseClient,
    encode_param,
    AsyncBaseClient,
)
import typing
from apple_python.types.v1.app_screenshot_sets.relationships.app_screenshots import (
    params,
    models,
)


class AppScreenshotsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def patch(
        self,
        *,
        data: params.AppScreenshotSetAppScreenshotsLinkagesRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerAppScreenshotSetAppScreenshotsLinkagesRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="PATCH",
            path=f"/v1/appScreenshotSets/{id}/relationships/appScreenshots",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def list(
        self,
        *,
        id: str,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppScreenshotSetAppScreenshotsLinkagesResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/appScreenshotSets/{id}/relationships/appScreenshots",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppScreenshotSetAppScreenshotsLinkagesResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncAppScreenshotsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def patch(
        self,
        *,
        data: params.AppScreenshotSetAppScreenshotsLinkagesRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerAppScreenshotSetAppScreenshotsLinkagesRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="PATCH",
            path=f"/v1/appScreenshotSets/{id}/relationships/appScreenshots",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def list(
        self,
        *,
        id: str,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppScreenshotSetAppScreenshotsLinkagesResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/appScreenshotSets/{id}/relationships/appScreenshots",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppScreenshotSetAppScreenshotsLinkagesResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
