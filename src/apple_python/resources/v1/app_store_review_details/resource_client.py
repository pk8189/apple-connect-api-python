"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    QueryParams,
    encode_param,
    to_encodable,
    AsyncBaseClient,
    SyncBaseClient,
    RequestOptions,
    default_request_options,
)
from apple_python.resources.v1.app_store_review_details.app_store_review_attachments import (
    AsyncAppStoreReviewAttachmentsClient,
    AppStoreReviewAttachmentsClient,
)
import typing
import typing_extensions
from apple_python.types.v1.app_store_review_details import models, params


class AppStoreReviewDetailsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.app_store_review_attachments = AppStoreReviewAttachmentsClient(
            base_client=self._base_client
        )

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.AppStoreReviewDetailCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppStoreReviewDetailResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerAppStoreReviewDetailCreateRequest
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/v1/appStoreReviewDetails",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.AppStoreReviewDetailResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def patch(
        self,
        *,
        data: params.AppStoreReviewDetailUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppStoreReviewDetailResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerAppStoreReviewDetailUpdateRequest
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="PATCH",
            path=f"/v1/appStoreReviewDetails/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.AppStoreReviewDetailResponse,
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
        fields_app_store_review_details: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appStoreReviewAttachments",
                    "appStoreVersion",
                    "contactEmail",
                    "contactFirstName",
                    "contactLastName",
                    "contactPhone",
                    "demoAccountName",
                    "demoAccountPassword",
                    "demoAccountRequired",
                    "notes",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appStoreReviewAttachments", "appStoreVersion"
                ]
            ]
        ] = None,
        limit_app_store_review_attachments: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppStoreReviewDetailResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_app_store_review_attachments is not None:
            _query["fields[appStoreReviewAttachments]"] = encode_param(
                fields_app_store_review_attachments, False
            )
        if fields_app_store_review_details is not None:
            _query["fields[appStoreReviewDetails]"] = encode_param(
                fields_app_store_review_details, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit_app_store_review_attachments is not None:
            _query["limit[appStoreReviewAttachments]"] = encode_param(
                limit_app_store_review_attachments, False
            )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/appStoreReviewDetails/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppStoreReviewDetailResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncAppStoreReviewDetailsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.app_store_review_attachments = AsyncAppStoreReviewAttachmentsClient(
            base_client=self._base_client
        )

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.AppStoreReviewDetailCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppStoreReviewDetailResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerAppStoreReviewDetailCreateRequest
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/v1/appStoreReviewDetails",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.AppStoreReviewDetailResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def patch(
        self,
        *,
        data: params.AppStoreReviewDetailUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppStoreReviewDetailResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerAppStoreReviewDetailUpdateRequest
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="PATCH",
            path=f"/v1/appStoreReviewDetails/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.AppStoreReviewDetailResponse,
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
        fields_app_store_review_details: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appStoreReviewAttachments",
                    "appStoreVersion",
                    "contactEmail",
                    "contactFirstName",
                    "contactLastName",
                    "contactPhone",
                    "demoAccountName",
                    "demoAccountPassword",
                    "demoAccountRequired",
                    "notes",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appStoreReviewAttachments", "appStoreVersion"
                ]
            ]
        ] = None,
        limit_app_store_review_attachments: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppStoreReviewDetailResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_app_store_review_attachments is not None:
            _query["fields[appStoreReviewAttachments]"] = encode_param(
                fields_app_store_review_attachments, False
            )
        if fields_app_store_review_details is not None:
            _query["fields[appStoreReviewDetails]"] = encode_param(
                fields_app_store_review_details, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit_app_store_review_attachments is not None:
            _query["limit[appStoreReviewAttachments]"] = encode_param(
                limit_app_store_review_attachments, False
            )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/appStoreReviewDetails/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppStoreReviewDetailResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)