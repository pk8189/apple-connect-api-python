"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    SyncBaseClient,
    default_request_options,
    QueryParams,
    encode_param,
    AsyncBaseClient,
    to_encodable,
    RequestOptions,
)
import typing
import typing_extensions
from apple_python.types.v1.promoted_purchase_images import models, params


class PromotedPurchaseImagesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.PromotedPurchaseImageCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PromotedPurchaseImageResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerPromotedPurchaseImageCreateRequest
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/v1/promotedPurchaseImages",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.PromotedPurchaseImageResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def patch(
        self,
        *,
        data: params.PromotedPurchaseImageUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PromotedPurchaseImageResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerPromotedPurchaseImageUpdateRequest
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="PATCH",
            path=f"/v1/promotedPurchaseImages/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.PromotedPurchaseImageResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def get(
        self,
        *,
        id: str,
        fields_promoted_purchase_images: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "assetToken",
                    "assetType",
                    "fileName",
                    "fileSize",
                    "imageAsset",
                    "promotedPurchase",
                    "sourceFileChecksum",
                    "state",
                    "uploadOperations",
                    "uploaded",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[typing_extensions.Literal["promotedPurchase"]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PromotedPurchaseImageResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_promoted_purchase_images is not None:
            _query["fields[promotedPurchaseImages]"] = encode_param(
                fields_promoted_purchase_images, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/promotedPurchaseImages/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.PromotedPurchaseImageResponse,
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
            path=f"/v1/promotedPurchaseImages/{id}",
            auth_names=["itc-bearer-token"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncPromotedPurchaseImagesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.PromotedPurchaseImageCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PromotedPurchaseImageResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerPromotedPurchaseImageCreateRequest
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/v1/promotedPurchaseImages",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.PromotedPurchaseImageResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def patch(
        self,
        *,
        data: params.PromotedPurchaseImageUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PromotedPurchaseImageResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerPromotedPurchaseImageUpdateRequest
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="PATCH",
            path=f"/v1/promotedPurchaseImages/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.PromotedPurchaseImageResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def get(
        self,
        *,
        id: str,
        fields_promoted_purchase_images: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "assetToken",
                    "assetType",
                    "fileName",
                    "fileSize",
                    "imageAsset",
                    "promotedPurchase",
                    "sourceFileChecksum",
                    "state",
                    "uploadOperations",
                    "uploaded",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[typing_extensions.Literal["promotedPurchase"]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PromotedPurchaseImageResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_promoted_purchase_images is not None:
            _query["fields[promotedPurchaseImages]"] = encode_param(
                fields_promoted_purchase_images, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/promotedPurchaseImages/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.PromotedPurchaseImageResponse,
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
            path=f"/v1/promotedPurchaseImages/{id}",
            auth_names=["itc-bearer-token"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
