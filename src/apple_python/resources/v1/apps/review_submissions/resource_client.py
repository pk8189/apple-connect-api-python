"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    QueryParams,
    encode_param,
    default_request_options,
    SyncBaseClient,
    AsyncBaseClient,
    RequestOptions,
)
import typing
import typing_extensions
from apple_python.types.v1.apps.review_submissions import models


class ReviewSubmissionsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        id: str,
        fields_actors: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "actorType",
                    "apiKeyId",
                    "userEmail",
                    "userFirstName",
                    "userLastName",
                ]
            ]
        ] = None,
        fields_app_store_versions: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "ageRatingDeclaration",
                    "alternativeDistributionPackage",
                    "app",
                    "appClipDefaultExperience",
                    "appStoreReviewDetail",
                    "appStoreState",
                    "appStoreVersionExperiments",
                    "appStoreVersionExperimentsV2",
                    "appStoreVersionLocalizations",
                    "appStoreVersionPhasedRelease",
                    "appStoreVersionSubmission",
                    "appVersionState",
                    "build",
                    "copyright",
                    "createdDate",
                    "customerReviews",
                    "downloadable",
                    "earliestReleaseDate",
                    "platform",
                    "releaseType",
                    "reviewType",
                    "routingAppCoverage",
                    "versionString",
                ]
            ]
        ] = None,
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
        fields_review_submission_items: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appCustomProductPageVersion",
                    "appEvent",
                    "appStoreVersion",
                    "appStoreVersionExperiment",
                    "appStoreVersionExperimentV2",
                    "removed",
                    "resolved",
                    "reviewSubmission",
                    "state",
                ]
            ]
        ] = None,
        fields_review_submissions: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
                    "appStoreVersionForReview",
                    "canceled",
                    "items",
                    "lastUpdatedByActor",
                    "platform",
                    "state",
                    "submitted",
                    "submittedByActor",
                    "submittedDate",
                ]
            ]
        ] = None,
        filter_platform: typing.Optional[
            typing.List[
                typing_extensions.Literal["IOS", "MAC_OS", "TV_OS", "VISION_OS"]
            ]
        ] = None,
        filter_state: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "READY_FOR_REVIEW",
                    "WAITING_FOR_REVIEW",
                    "IN_REVIEW",
                    "UNRESOLVED_ISSUES",
                    "CANCELING",
                    "COMPLETING",
                    "COMPLETE",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
                    "appStoreVersionForReview",
                    "items",
                    "lastUpdatedByActor",
                    "submittedByActor",
                ]
            ]
        ] = None,
        limit: typing.Optional[int] = None,
        limit_items: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReviewSubmissionsResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_actors is not None:
            _query["fields[actors]"] = encode_param(fields_actors, False)
        if fields_app_store_versions is not None:
            _query["fields[appStoreVersions]"] = encode_param(
                fields_app_store_versions, False
            )
        if fields_apps is not None:
            _query["fields[apps]"] = encode_param(fields_apps, False)
        if fields_review_submission_items is not None:
            _query["fields[reviewSubmissionItems]"] = encode_param(
                fields_review_submission_items, False
            )
        if fields_review_submissions is not None:
            _query["fields[reviewSubmissions]"] = encode_param(
                fields_review_submissions, False
            )
        if filter_platform is not None:
            _query["filter[platform]"] = encode_param(filter_platform, False)
        if filter_state is not None:
            _query["filter[state]"] = encode_param(filter_state, False)
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        if limit_items is not None:
            _query["limit[items]"] = encode_param(limit_items, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/apps/{id}/reviewSubmissions",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.ReviewSubmissionsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncReviewSubmissionsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        id: str,
        fields_actors: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "actorType",
                    "apiKeyId",
                    "userEmail",
                    "userFirstName",
                    "userLastName",
                ]
            ]
        ] = None,
        fields_app_store_versions: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "ageRatingDeclaration",
                    "alternativeDistributionPackage",
                    "app",
                    "appClipDefaultExperience",
                    "appStoreReviewDetail",
                    "appStoreState",
                    "appStoreVersionExperiments",
                    "appStoreVersionExperimentsV2",
                    "appStoreVersionLocalizations",
                    "appStoreVersionPhasedRelease",
                    "appStoreVersionSubmission",
                    "appVersionState",
                    "build",
                    "copyright",
                    "createdDate",
                    "customerReviews",
                    "downloadable",
                    "earliestReleaseDate",
                    "platform",
                    "releaseType",
                    "reviewType",
                    "routingAppCoverage",
                    "versionString",
                ]
            ]
        ] = None,
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
        fields_review_submission_items: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appCustomProductPageVersion",
                    "appEvent",
                    "appStoreVersion",
                    "appStoreVersionExperiment",
                    "appStoreVersionExperimentV2",
                    "removed",
                    "resolved",
                    "reviewSubmission",
                    "state",
                ]
            ]
        ] = None,
        fields_review_submissions: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
                    "appStoreVersionForReview",
                    "canceled",
                    "items",
                    "lastUpdatedByActor",
                    "platform",
                    "state",
                    "submitted",
                    "submittedByActor",
                    "submittedDate",
                ]
            ]
        ] = None,
        filter_platform: typing.Optional[
            typing.List[
                typing_extensions.Literal["IOS", "MAC_OS", "TV_OS", "VISION_OS"]
            ]
        ] = None,
        filter_state: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "READY_FOR_REVIEW",
                    "WAITING_FOR_REVIEW",
                    "IN_REVIEW",
                    "UNRESOLVED_ISSUES",
                    "CANCELING",
                    "COMPLETING",
                    "COMPLETE",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
                    "appStoreVersionForReview",
                    "items",
                    "lastUpdatedByActor",
                    "submittedByActor",
                ]
            ]
        ] = None,
        limit: typing.Optional[int] = None,
        limit_items: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReviewSubmissionsResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_actors is not None:
            _query["fields[actors]"] = encode_param(fields_actors, False)
        if fields_app_store_versions is not None:
            _query["fields[appStoreVersions]"] = encode_param(
                fields_app_store_versions, False
            )
        if fields_apps is not None:
            _query["fields[apps]"] = encode_param(fields_apps, False)
        if fields_review_submission_items is not None:
            _query["fields[reviewSubmissionItems]"] = encode_param(
                fields_review_submission_items, False
            )
        if fields_review_submissions is not None:
            _query["fields[reviewSubmissions]"] = encode_param(
                fields_review_submissions, False
            )
        if filter_platform is not None:
            _query["filter[platform]"] = encode_param(filter_platform, False)
        if filter_state is not None:
            _query["filter[state]"] = encode_param(filter_state, False)
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        if limit_items is not None:
            _query["limit[items]"] = encode_param(limit_items, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/apps/{id}/reviewSubmissions",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.ReviewSubmissionsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)