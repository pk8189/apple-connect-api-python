"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    QueryParams,
    AsyncBaseClient,
    default_request_options,
    encode_param,
    RequestOptions,
    SyncBaseClient,
)
import typing
import typing_extensions
from apple_python.types.v1.app_store_versions.app_store_review_detail import models


class AppStoreReviewDetailClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
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
        if fields_app_store_versions is not None:
            _query["fields[appStoreVersions]"] = encode_param(
                fields_app_store_versions, False
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
            path=f"/v1/appStoreVersions/{id}/appStoreReviewDetail",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppStoreReviewDetailResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncAppStoreReviewDetailClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
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
        if fields_app_store_versions is not None:
            _query["fields[appStoreVersions]"] = encode_param(
                fields_app_store_versions, False
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
            path=f"/v1/appStoreVersions/{id}/appStoreReviewDetail",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppStoreReviewDetailResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)