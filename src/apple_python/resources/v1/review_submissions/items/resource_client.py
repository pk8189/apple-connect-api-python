"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    default_request_options,
    encode_param,
    RequestOptions,
    QueryParams,
    SyncBaseClient,
    AsyncBaseClient,
)
import typing
import typing_extensions
from apple_python.types.v1.review_submissions.items import models


class ItemsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        id: str,
        fields_app_custom_product_page_versions: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appCustomProductPage",
                    "appCustomProductPageLocalizations",
                    "deepLink",
                    "state",
                    "version",
                ]
            ]
        ] = None,
        fields_app_events: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
                    "archivedTerritorySchedules",
                    "badge",
                    "deepLink",
                    "eventState",
                    "localizations",
                    "primaryLocale",
                    "priority",
                    "purchaseRequirement",
                    "purpose",
                    "referenceName",
                    "territorySchedules",
                ]
            ]
        ] = None,
        fields_app_store_version_experiments: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
                    "appStoreVersion",
                    "appStoreVersionExperimentTreatments",
                    "controlVersions",
                    "endDate",
                    "latestControlVersion",
                    "name",
                    "platform",
                    "reviewRequired",
                    "startDate",
                    "started",
                    "state",
                    "trafficProportion",
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
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appCustomProductPageVersion",
                    "appEvent",
                    "appStoreVersion",
                    "appStoreVersionExperiment",
                    "appStoreVersionExperimentV2",
                ]
            ]
        ] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReviewSubmissionItemsResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_app_custom_product_page_versions is not None:
            _query["fields[appCustomProductPageVersions]"] = encode_param(
                fields_app_custom_product_page_versions, False
            )
        if fields_app_events is not None:
            _query["fields[appEvents]"] = encode_param(fields_app_events, False)
        if fields_app_store_version_experiments is not None:
            _query["fields[appStoreVersionExperiments]"] = encode_param(
                fields_app_store_version_experiments, False
            )
        if fields_app_store_versions is not None:
            _query["fields[appStoreVersions]"] = encode_param(
                fields_app_store_versions, False
            )
        if fields_review_submission_items is not None:
            _query["fields[reviewSubmissionItems]"] = encode_param(
                fields_review_submission_items, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/reviewSubmissions/{id}/items",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.ReviewSubmissionItemsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncItemsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        id: str,
        fields_app_custom_product_page_versions: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appCustomProductPage",
                    "appCustomProductPageLocalizations",
                    "deepLink",
                    "state",
                    "version",
                ]
            ]
        ] = None,
        fields_app_events: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
                    "archivedTerritorySchedules",
                    "badge",
                    "deepLink",
                    "eventState",
                    "localizations",
                    "primaryLocale",
                    "priority",
                    "purchaseRequirement",
                    "purpose",
                    "referenceName",
                    "territorySchedules",
                ]
            ]
        ] = None,
        fields_app_store_version_experiments: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
                    "appStoreVersion",
                    "appStoreVersionExperimentTreatments",
                    "controlVersions",
                    "endDate",
                    "latestControlVersion",
                    "name",
                    "platform",
                    "reviewRequired",
                    "startDate",
                    "started",
                    "state",
                    "trafficProportion",
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
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appCustomProductPageVersion",
                    "appEvent",
                    "appStoreVersion",
                    "appStoreVersionExperiment",
                    "appStoreVersionExperimentV2",
                ]
            ]
        ] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReviewSubmissionItemsResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_app_custom_product_page_versions is not None:
            _query["fields[appCustomProductPageVersions]"] = encode_param(
                fields_app_custom_product_page_versions, False
            )
        if fields_app_events is not None:
            _query["fields[appEvents]"] = encode_param(fields_app_events, False)
        if fields_app_store_version_experiments is not None:
            _query["fields[appStoreVersionExperiments]"] = encode_param(
                fields_app_store_version_experiments, False
            )
        if fields_app_store_versions is not None:
            _query["fields[appStoreVersions]"] = encode_param(
                fields_app_store_versions, False
            )
        if fields_review_submission_items is not None:
            _query["fields[reviewSubmissionItems]"] = encode_param(
                fields_review_submission_items, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/reviewSubmissions/{id}/items",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.ReviewSubmissionItemsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)