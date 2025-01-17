"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    SyncBaseClient,
    encode_param,
    RequestOptions,
    default_request_options,
    AsyncBaseClient,
    QueryParams,
    to_encodable,
)
from apple_python.resources.v1.promoted_purchases.promotion_images import (
    PromotionImagesClient,
    AsyncPromotionImagesClient,
)
import typing
import typing_extensions
from apple_python.types.v1.promoted_purchases import models, params


class PromotedPurchasesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.promotion_images = PromotionImagesClient(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.PromotedPurchaseCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PromotedPurchaseResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerPromotedPurchaseCreateRequest
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/v1/promotedPurchases",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.PromotedPurchaseResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def patch(
        self,
        *,
        data: params.PromotedPurchaseUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PromotedPurchaseResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerPromotedPurchaseUpdateRequest
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="PATCH",
            path=f"/v1/promotedPurchases/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.PromotedPurchaseResponse,
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
        fields_promoted_purchases: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
                    "enabled",
                    "inAppPurchaseV2",
                    "promotionImages",
                    "state",
                    "subscription",
                    "visibleForAllUsers",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "inAppPurchaseV2", "promotionImages", "subscription"
                ]
            ]
        ] = None,
        limit_promotion_images: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PromotedPurchaseResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_promoted_purchase_images is not None:
            _query["fields[promotedPurchaseImages]"] = encode_param(
                fields_promoted_purchase_images, False
            )
        if fields_promoted_purchases is not None:
            _query["fields[promotedPurchases]"] = encode_param(
                fields_promoted_purchases, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit_promotion_images is not None:
            _query["limit[promotionImages]"] = encode_param(
                limit_promotion_images, False
            )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/promotedPurchases/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.PromotedPurchaseResponse,
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
            path=f"/v1/promotedPurchases/{id}",
            auth_names=["itc-bearer-token"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncPromotedPurchasesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.promotion_images = AsyncPromotionImagesClient(
            base_client=self._base_client
        )

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.PromotedPurchaseCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PromotedPurchaseResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerPromotedPurchaseCreateRequest
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/v1/promotedPurchases",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.PromotedPurchaseResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def patch(
        self,
        *,
        data: params.PromotedPurchaseUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PromotedPurchaseResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerPromotedPurchaseUpdateRequest
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="PATCH",
            path=f"/v1/promotedPurchases/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.PromotedPurchaseResponse,
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
        fields_promoted_purchases: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
                    "enabled",
                    "inAppPurchaseV2",
                    "promotionImages",
                    "state",
                    "subscription",
                    "visibleForAllUsers",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "inAppPurchaseV2", "promotionImages", "subscription"
                ]
            ]
        ] = None,
        limit_promotion_images: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PromotedPurchaseResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_promoted_purchase_images is not None:
            _query["fields[promotedPurchaseImages]"] = encode_param(
                fields_promoted_purchase_images, False
            )
        if fields_promoted_purchases is not None:
            _query["fields[promotedPurchases]"] = encode_param(
                fields_promoted_purchases, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit_promotion_images is not None:
            _query["limit[promotionImages]"] = encode_param(
                limit_promotion_images, False
            )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/promotedPurchases/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.PromotedPurchaseResponse,
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
            path=f"/v1/promotedPurchases/{id}",
            auth_names=["itc-bearer-token"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
