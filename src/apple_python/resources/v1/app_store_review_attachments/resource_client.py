"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    SyncBaseClient,
    RequestOptions,
    default_request_options,
    encode_param,
    QueryParams,
    to_encodable,
    AsyncBaseClient,
)
import typing
import typing_extensions
from apple_python.types.v1.app_store_review_attachments import params, models


class AppStoreReviewAttachmentsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.AppStoreReviewAttachmentCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppStoreReviewAttachmentResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerAppStoreReviewAttachmentCreateRequest
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/v1/appStoreReviewAttachments",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.AppStoreReviewAttachmentResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def patch(
        self,
        *,
        data: params.AppStoreReviewAttachmentUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppStoreReviewAttachmentResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerAppStoreReviewAttachmentUpdateRequest
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="PATCH",
            path=f"/v1/appStoreReviewAttachments/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.AppStoreReviewAttachmentResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def get(
        self,
        *,
        id: str,
        fields_app_store_review_attachments: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appStoreReviewDetail",
                    "assetDeliveryState",
                    "fileName",
                    "fileSize",
                    "sourceFileChecksum",
                    "uploadOperations",
                    "uploaded",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[typing_extensions.Literal["appStoreReviewDetail"]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppStoreReviewAttachmentResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_app_store_review_attachments is not None:
            _query["fields[appStoreReviewAttachments]"] = encode_param(
                fields_app_store_review_attachments, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/appStoreReviewAttachments/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppStoreReviewAttachmentResponse,
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
            path=f"/v1/appStoreReviewAttachments/{id}",
            auth_names=["itc-bearer-token"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncAppStoreReviewAttachmentsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.AppStoreReviewAttachmentCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppStoreReviewAttachmentResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerAppStoreReviewAttachmentCreateRequest
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/v1/appStoreReviewAttachments",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.AppStoreReviewAttachmentResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def patch(
        self,
        *,
        data: params.AppStoreReviewAttachmentUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppStoreReviewAttachmentResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerAppStoreReviewAttachmentUpdateRequest
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="PATCH",
            path=f"/v1/appStoreReviewAttachments/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.AppStoreReviewAttachmentResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def get(
        self,
        *,
        id: str,
        fields_app_store_review_attachments: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appStoreReviewDetail",
                    "assetDeliveryState",
                    "fileName",
                    "fileSize",
                    "sourceFileChecksum",
                    "uploadOperations",
                    "uploaded",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[typing_extensions.Literal["appStoreReviewDetail"]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppStoreReviewAttachmentResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_app_store_review_attachments is not None:
            _query["fields[appStoreReviewAttachments]"] = encode_param(
                fields_app_store_review_attachments, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/appStoreReviewAttachments/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppStoreReviewAttachmentResponse,
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
            path=f"/v1/appStoreReviewAttachments/{id}",
            auth_names=["itc-bearer-token"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
