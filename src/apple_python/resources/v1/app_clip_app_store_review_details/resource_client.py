"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    QueryParams,
    default_request_options,
    to_encodable,
    RequestOptions,
    AsyncBaseClient,
    SyncBaseClient,
    encode_param,
)
import typing
import typing_extensions
from apple_python.types.v1.app_clip_app_store_review_details import params, models


class AppClipAppStoreReviewDetailsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.AppClipAppStoreReviewDetailCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppClipAppStoreReviewDetailResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerAppClipAppStoreReviewDetailCreateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/v1/appClipAppStoreReviewDetails",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.AppClipAppStoreReviewDetailResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def patch(
        self,
        *,
        data: params.AppClipAppStoreReviewDetailUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppClipAppStoreReviewDetailResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerAppClipAppStoreReviewDetailUpdateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="PATCH",
            path=f"/v1/appClipAppStoreReviewDetails/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.AppClipAppStoreReviewDetailResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def get(
        self,
        *,
        id: str,
        fields_app_clip_app_store_review_details: typing.Optional[
            typing.List[
                typing_extensions.Literal["appClipDefaultExperience", "invocationUrls"]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[typing_extensions.Literal["appClipDefaultExperience"]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppClipAppStoreReviewDetailResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_app_clip_app_store_review_details is not None:
            _query["fields[appClipAppStoreReviewDetails]"] = encode_param(
                fields_app_clip_app_store_review_details, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/appClipAppStoreReviewDetails/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppClipAppStoreReviewDetailResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncAppClipAppStoreReviewDetailsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.AppClipAppStoreReviewDetailCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppClipAppStoreReviewDetailResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerAppClipAppStoreReviewDetailCreateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/v1/appClipAppStoreReviewDetails",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.AppClipAppStoreReviewDetailResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def patch(
        self,
        *,
        data: params.AppClipAppStoreReviewDetailUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppClipAppStoreReviewDetailResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerAppClipAppStoreReviewDetailUpdateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="PATCH",
            path=f"/v1/appClipAppStoreReviewDetails/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.AppClipAppStoreReviewDetailResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def get(
        self,
        *,
        id: str,
        fields_app_clip_app_store_review_details: typing.Optional[
            typing.List[
                typing_extensions.Literal["appClipDefaultExperience", "invocationUrls"]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[typing_extensions.Literal["appClipDefaultExperience"]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppClipAppStoreReviewDetailResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_app_clip_app_store_review_details is not None:
            _query["fields[appClipAppStoreReviewDetails]"] = encode_param(
                fields_app_clip_app_store_review_details, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/appClipAppStoreReviewDetails/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppClipAppStoreReviewDetailResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
