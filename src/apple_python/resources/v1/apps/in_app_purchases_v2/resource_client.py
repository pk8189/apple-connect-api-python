"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    AsyncBaseClient,
    default_request_options,
    encode_param,
    QueryParams,
    SyncBaseClient,
    RequestOptions,
)
import typing
import typing_extensions
from apple_python.types.v1.apps.in_app_purchases_v2 import models


class InAppPurchasesV2Client:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        id: str,
        fields_in_app_purchase_app_store_review_screenshots: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "assetDeliveryState",
                    "assetToken",
                    "assetType",
                    "fileName",
                    "fileSize",
                    "imageAsset",
                    "inAppPurchaseV2",
                    "sourceFileChecksum",
                    "uploadOperations",
                    "uploaded",
                ]
            ]
        ] = None,
        fields_in_app_purchase_availabilities: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "availableInNewTerritories", "availableTerritories", "inAppPurchase"
                ]
            ]
        ] = None,
        fields_in_app_purchase_contents: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "fileName", "fileSize", "inAppPurchaseV2", "lastModifiedDate", "url"
                ]
            ]
        ] = None,
        fields_in_app_purchase_localizations: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "description", "inAppPurchaseV2", "locale", "name", "state"
                ]
            ]
        ] = None,
        fields_in_app_purchase_price_schedules: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "automaticPrices", "baseTerritory", "inAppPurchase", "manualPrices"
                ]
            ]
        ] = None,
        fields_in_app_purchases: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
                    "appStoreReviewScreenshot",
                    "content",
                    "contentHosting",
                    "familySharable",
                    "iapPriceSchedule",
                    "inAppPurchaseAvailability",
                    "inAppPurchaseLocalizations",
                    "inAppPurchaseType",
                    "name",
                    "productId",
                    "promotedPurchase",
                    "reviewNote",
                    "state",
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
        filter_in_app_purchase_type: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "CONSUMABLE", "NON_CONSUMABLE", "NON_RENEWING_SUBSCRIPTION"
                ]
            ]
        ] = None,
        filter_name: typing.Optional[typing.List[str]] = None,
        filter_product_id: typing.Optional[typing.List[str]] = None,
        filter_state: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "MISSING_METADATA",
                    "WAITING_FOR_UPLOAD",
                    "PROCESSING_CONTENT",
                    "READY_TO_SUBMIT",
                    "WAITING_FOR_REVIEW",
                    "IN_REVIEW",
                    "DEVELOPER_ACTION_NEEDED",
                    "PENDING_BINARY_APPROVAL",
                    "APPROVED",
                    "DEVELOPER_REMOVED_FROM_SALE",
                    "REMOVED_FROM_SALE",
                    "REJECTED",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appStoreReviewScreenshot",
                    "content",
                    "iapPriceSchedule",
                    "inAppPurchaseAvailability",
                    "inAppPurchaseLocalizations",
                    "promotedPurchase",
                ]
            ]
        ] = None,
        limit: typing.Optional[int] = None,
        limit_in_app_purchase_localizations: typing.Optional[int] = None,
        sort: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "inAppPurchaseType", "-inAppPurchaseType", "name", "-name"
                ]
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.InAppPurchasesV2Response:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_in_app_purchase_app_store_review_screenshots is not None:
            _query["fields[inAppPurchaseAppStoreReviewScreenshots]"] = encode_param(
                fields_in_app_purchase_app_store_review_screenshots, False
            )
        if fields_in_app_purchase_availabilities is not None:
            _query["fields[inAppPurchaseAvailabilities]"] = encode_param(
                fields_in_app_purchase_availabilities, False
            )
        if fields_in_app_purchase_contents is not None:
            _query["fields[inAppPurchaseContents]"] = encode_param(
                fields_in_app_purchase_contents, False
            )
        if fields_in_app_purchase_localizations is not None:
            _query["fields[inAppPurchaseLocalizations]"] = encode_param(
                fields_in_app_purchase_localizations, False
            )
        if fields_in_app_purchase_price_schedules is not None:
            _query["fields[inAppPurchasePriceSchedules]"] = encode_param(
                fields_in_app_purchase_price_schedules, False
            )
        if fields_in_app_purchases is not None:
            _query["fields[inAppPurchases]"] = encode_param(
                fields_in_app_purchases, False
            )
        if fields_promoted_purchases is not None:
            _query["fields[promotedPurchases]"] = encode_param(
                fields_promoted_purchases, False
            )
        if filter_in_app_purchase_type is not None:
            _query["filter[inAppPurchaseType]"] = encode_param(
                filter_in_app_purchase_type, False
            )
        if filter_name is not None:
            _query["filter[name]"] = encode_param(filter_name, False)
        if filter_product_id is not None:
            _query["filter[productId]"] = encode_param(filter_product_id, False)
        if filter_state is not None:
            _query["filter[state]"] = encode_param(filter_state, False)
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        if limit_in_app_purchase_localizations is not None:
            _query["limit[inAppPurchaseLocalizations]"] = encode_param(
                limit_in_app_purchase_localizations, False
            )
        if sort is not None:
            _query["sort"] = encode_param(sort, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/apps/{id}/inAppPurchasesV2",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.InAppPurchasesV2Response,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncInAppPurchasesV2Client:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        id: str,
        fields_in_app_purchase_app_store_review_screenshots: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "assetDeliveryState",
                    "assetToken",
                    "assetType",
                    "fileName",
                    "fileSize",
                    "imageAsset",
                    "inAppPurchaseV2",
                    "sourceFileChecksum",
                    "uploadOperations",
                    "uploaded",
                ]
            ]
        ] = None,
        fields_in_app_purchase_availabilities: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "availableInNewTerritories", "availableTerritories", "inAppPurchase"
                ]
            ]
        ] = None,
        fields_in_app_purchase_contents: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "fileName", "fileSize", "inAppPurchaseV2", "lastModifiedDate", "url"
                ]
            ]
        ] = None,
        fields_in_app_purchase_localizations: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "description", "inAppPurchaseV2", "locale", "name", "state"
                ]
            ]
        ] = None,
        fields_in_app_purchase_price_schedules: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "automaticPrices", "baseTerritory", "inAppPurchase", "manualPrices"
                ]
            ]
        ] = None,
        fields_in_app_purchases: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
                    "appStoreReviewScreenshot",
                    "content",
                    "contentHosting",
                    "familySharable",
                    "iapPriceSchedule",
                    "inAppPurchaseAvailability",
                    "inAppPurchaseLocalizations",
                    "inAppPurchaseType",
                    "name",
                    "productId",
                    "promotedPurchase",
                    "reviewNote",
                    "state",
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
        filter_in_app_purchase_type: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "CONSUMABLE", "NON_CONSUMABLE", "NON_RENEWING_SUBSCRIPTION"
                ]
            ]
        ] = None,
        filter_name: typing.Optional[typing.List[str]] = None,
        filter_product_id: typing.Optional[typing.List[str]] = None,
        filter_state: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "MISSING_METADATA",
                    "WAITING_FOR_UPLOAD",
                    "PROCESSING_CONTENT",
                    "READY_TO_SUBMIT",
                    "WAITING_FOR_REVIEW",
                    "IN_REVIEW",
                    "DEVELOPER_ACTION_NEEDED",
                    "PENDING_BINARY_APPROVAL",
                    "APPROVED",
                    "DEVELOPER_REMOVED_FROM_SALE",
                    "REMOVED_FROM_SALE",
                    "REJECTED",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appStoreReviewScreenshot",
                    "content",
                    "iapPriceSchedule",
                    "inAppPurchaseAvailability",
                    "inAppPurchaseLocalizations",
                    "promotedPurchase",
                ]
            ]
        ] = None,
        limit: typing.Optional[int] = None,
        limit_in_app_purchase_localizations: typing.Optional[int] = None,
        sort: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "inAppPurchaseType", "-inAppPurchaseType", "name", "-name"
                ]
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.InAppPurchasesV2Response:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_in_app_purchase_app_store_review_screenshots is not None:
            _query["fields[inAppPurchaseAppStoreReviewScreenshots]"] = encode_param(
                fields_in_app_purchase_app_store_review_screenshots, False
            )
        if fields_in_app_purchase_availabilities is not None:
            _query["fields[inAppPurchaseAvailabilities]"] = encode_param(
                fields_in_app_purchase_availabilities, False
            )
        if fields_in_app_purchase_contents is not None:
            _query["fields[inAppPurchaseContents]"] = encode_param(
                fields_in_app_purchase_contents, False
            )
        if fields_in_app_purchase_localizations is not None:
            _query["fields[inAppPurchaseLocalizations]"] = encode_param(
                fields_in_app_purchase_localizations, False
            )
        if fields_in_app_purchase_price_schedules is not None:
            _query["fields[inAppPurchasePriceSchedules]"] = encode_param(
                fields_in_app_purchase_price_schedules, False
            )
        if fields_in_app_purchases is not None:
            _query["fields[inAppPurchases]"] = encode_param(
                fields_in_app_purchases, False
            )
        if fields_promoted_purchases is not None:
            _query["fields[promotedPurchases]"] = encode_param(
                fields_promoted_purchases, False
            )
        if filter_in_app_purchase_type is not None:
            _query["filter[inAppPurchaseType]"] = encode_param(
                filter_in_app_purchase_type, False
            )
        if filter_name is not None:
            _query["filter[name]"] = encode_param(filter_name, False)
        if filter_product_id is not None:
            _query["filter[productId]"] = encode_param(filter_product_id, False)
        if filter_state is not None:
            _query["filter[state]"] = encode_param(filter_state, False)
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        if limit_in_app_purchase_localizations is not None:
            _query["limit[inAppPurchaseLocalizations]"] = encode_param(
                limit_in_app_purchase_localizations, False
            )
        if sort is not None:
            _query["sort"] = encode_param(sort, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/apps/{id}/inAppPurchasesV2",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.InAppPurchasesV2Response,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)