"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    AsyncBaseClient,
    default_request_options,
    SyncBaseClient,
    QueryParams,
    encode_param,
    RequestOptions,
)
import typing
import typing_extensions
from apple_python.types.v1.app_store_versions.app_store_version_submission import models


class AppStoreVersionSubmissionClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        id: str,
        fields_app_store_version_submissions: typing.Optional[
            typing.List[typing_extensions.Literal["appStoreVersion"]]
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
            typing.List[typing_extensions.Literal["appStoreVersion"]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppStoreVersionSubmissionResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_app_store_version_submissions is not None:
            _query["fields[appStoreVersionSubmissions]"] = encode_param(
                fields_app_store_version_submissions, False
            )
        if fields_app_store_versions is not None:
            _query["fields[appStoreVersions]"] = encode_param(
                fields_app_store_versions, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/appStoreVersions/{id}/appStoreVersionSubmission",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppStoreVersionSubmissionResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncAppStoreVersionSubmissionClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        id: str,
        fields_app_store_version_submissions: typing.Optional[
            typing.List[typing_extensions.Literal["appStoreVersion"]]
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
            typing.List[typing_extensions.Literal["appStoreVersion"]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppStoreVersionSubmissionResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_app_store_version_submissions is not None:
            _query["fields[appStoreVersionSubmissions]"] = encode_param(
                fields_app_store_version_submissions, False
            )
        if fields_app_store_versions is not None:
            _query["fields[appStoreVersions]"] = encode_param(
                fields_app_store_versions, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/appStoreVersions/{id}/appStoreVersionSubmission",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppStoreVersionSubmissionResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
