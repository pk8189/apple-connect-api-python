"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    SyncBaseClient,
    AsyncBaseClient,
    encode_param,
    default_request_options,
    QueryParams,
    RequestOptions,
)
import typing
import typing_extensions
from apple_python.types.v1.app_store_versions.app_clip_default_experience import models


class AppClipDefaultExperienceClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        id: str,
        fields_app_clip_app_store_review_details: typing.Optional[
            typing.List[
                typing_extensions.Literal["appClipDefaultExperience", "invocationUrls"]
            ]
        ] = None,
        fields_app_clip_default_experience_localizations: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appClipDefaultExperience",
                    "appClipHeaderImage",
                    "locale",
                    "subtitle",
                ]
            ]
        ] = None,
        fields_app_clip_default_experiences: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "action",
                    "appClip",
                    "appClipAppStoreReviewDetail",
                    "appClipDefaultExperienceLocalizations",
                    "appClipDefaultExperienceTemplate",
                    "releaseWithAppStoreVersion",
                ]
            ]
        ] = None,
        fields_app_clips: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
                    "appClipAdvancedExperiences",
                    "appClipDefaultExperiences",
                    "bundleId",
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
                    "appClip",
                    "appClipAppStoreReviewDetail",
                    "appClipDefaultExperienceLocalizations",
                    "releaseWithAppStoreVersion",
                ]
            ]
        ] = None,
        limit_app_clip_default_experience_localizations: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppClipDefaultExperienceResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_app_clip_app_store_review_details is not None:
            _query["fields[appClipAppStoreReviewDetails]"] = encode_param(
                fields_app_clip_app_store_review_details, False
            )
        if fields_app_clip_default_experience_localizations is not None:
            _query["fields[appClipDefaultExperienceLocalizations]"] = encode_param(
                fields_app_clip_default_experience_localizations, False
            )
        if fields_app_clip_default_experiences is not None:
            _query["fields[appClipDefaultExperiences]"] = encode_param(
                fields_app_clip_default_experiences, False
            )
        if fields_app_clips is not None:
            _query["fields[appClips]"] = encode_param(fields_app_clips, False)
        if fields_app_store_versions is not None:
            _query["fields[appStoreVersions]"] = encode_param(
                fields_app_store_versions, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit_app_clip_default_experience_localizations is not None:
            _query["limit[appClipDefaultExperienceLocalizations]"] = encode_param(
                limit_app_clip_default_experience_localizations, False
            )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/appStoreVersions/{id}/appClipDefaultExperience",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppClipDefaultExperienceResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncAppClipDefaultExperienceClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        id: str,
        fields_app_clip_app_store_review_details: typing.Optional[
            typing.List[
                typing_extensions.Literal["appClipDefaultExperience", "invocationUrls"]
            ]
        ] = None,
        fields_app_clip_default_experience_localizations: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appClipDefaultExperience",
                    "appClipHeaderImage",
                    "locale",
                    "subtitle",
                ]
            ]
        ] = None,
        fields_app_clip_default_experiences: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "action",
                    "appClip",
                    "appClipAppStoreReviewDetail",
                    "appClipDefaultExperienceLocalizations",
                    "appClipDefaultExperienceTemplate",
                    "releaseWithAppStoreVersion",
                ]
            ]
        ] = None,
        fields_app_clips: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
                    "appClipAdvancedExperiences",
                    "appClipDefaultExperiences",
                    "bundleId",
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
                    "appClip",
                    "appClipAppStoreReviewDetail",
                    "appClipDefaultExperienceLocalizations",
                    "releaseWithAppStoreVersion",
                ]
            ]
        ] = None,
        limit_app_clip_default_experience_localizations: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppClipDefaultExperienceResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_app_clip_app_store_review_details is not None:
            _query["fields[appClipAppStoreReviewDetails]"] = encode_param(
                fields_app_clip_app_store_review_details, False
            )
        if fields_app_clip_default_experience_localizations is not None:
            _query["fields[appClipDefaultExperienceLocalizations]"] = encode_param(
                fields_app_clip_default_experience_localizations, False
            )
        if fields_app_clip_default_experiences is not None:
            _query["fields[appClipDefaultExperiences]"] = encode_param(
                fields_app_clip_default_experiences, False
            )
        if fields_app_clips is not None:
            _query["fields[appClips]"] = encode_param(fields_app_clips, False)
        if fields_app_store_versions is not None:
            _query["fields[appStoreVersions]"] = encode_param(
                fields_app_store_versions, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit_app_clip_default_experience_localizations is not None:
            _query["limit[appClipDefaultExperienceLocalizations]"] = encode_param(
                limit_app_clip_default_experience_localizations, False
            )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/appStoreVersions/{id}/appClipDefaultExperience",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppClipDefaultExperienceResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
