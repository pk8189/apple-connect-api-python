"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    default_request_options,
    SyncBaseClient,
    encode_param,
    QueryParams,
    RequestOptions,
    AsyncBaseClient,
)
import typing
import typing_extensions
from apple_python.types.v1.beta_app_review_details.app import models


class AppClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        id: str,
        fields_apps: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "alternativeDistributionKey",
                    "analyticsReportRequests",
                    "appAvailability",
                    "appClips",
                    "appCustomProductPages",
                    "appEncryptionDeclarations",
                    "appEvents",
                    "appInfos",
                    "appPricePoints",
                    "appPriceSchedule",
                    "appStoreVersionExperimentsV2",
                    "appStoreVersions",
                    "betaAppLocalizations",
                    "betaAppReviewDetail",
                    "betaGroups",
                    "betaLicenseAgreement",
                    "betaTesters",
                    "builds",
                    "bundleId",
                    "ciProduct",
                    "contentRightsDeclaration",
                    "customerReviews",
                    "endUserLicenseAgreement",
                    "gameCenterDetail",
                    "gameCenterEnabledVersions",
                    "inAppPurchases",
                    "inAppPurchasesV2",
                    "isOrEverWasMadeForKids",
                    "marketplaceSearchDetail",
                    "name",
                    "perfPowerMetrics",
                    "preOrder",
                    "preReleaseVersions",
                    "primaryLocale",
                    "promotedPurchases",
                    "reviewSubmissions",
                    "sku",
                    "subscriptionGracePeriod",
                    "subscriptionGroups",
                    "subscriptionStatusUrl",
                    "subscriptionStatusUrlForSandbox",
                    "subscriptionStatusUrlVersion",
                    "subscriptionStatusUrlVersionForSandbox",
                ]
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppWithoutIncludesResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_apps is not None:
            _query["fields[apps]"] = encode_param(fields_apps, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/betaAppReviewDetails/{id}/app",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppWithoutIncludesResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncAppClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        id: str,
        fields_apps: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "alternativeDistributionKey",
                    "analyticsReportRequests",
                    "appAvailability",
                    "appClips",
                    "appCustomProductPages",
                    "appEncryptionDeclarations",
                    "appEvents",
                    "appInfos",
                    "appPricePoints",
                    "appPriceSchedule",
                    "appStoreVersionExperimentsV2",
                    "appStoreVersions",
                    "betaAppLocalizations",
                    "betaAppReviewDetail",
                    "betaGroups",
                    "betaLicenseAgreement",
                    "betaTesters",
                    "builds",
                    "bundleId",
                    "ciProduct",
                    "contentRightsDeclaration",
                    "customerReviews",
                    "endUserLicenseAgreement",
                    "gameCenterDetail",
                    "gameCenterEnabledVersions",
                    "inAppPurchases",
                    "inAppPurchasesV2",
                    "isOrEverWasMadeForKids",
                    "marketplaceSearchDetail",
                    "name",
                    "perfPowerMetrics",
                    "preOrder",
                    "preReleaseVersions",
                    "primaryLocale",
                    "promotedPurchases",
                    "reviewSubmissions",
                    "sku",
                    "subscriptionGracePeriod",
                    "subscriptionGroups",
                    "subscriptionStatusUrl",
                    "subscriptionStatusUrlForSandbox",
                    "subscriptionStatusUrlVersion",
                    "subscriptionStatusUrlVersionForSandbox",
                ]
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppWithoutIncludesResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_apps is not None:
            _query["fields[apps]"] = encode_param(fields_apps, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/betaAppReviewDetails/{id}/app",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppWithoutIncludesResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
