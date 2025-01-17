"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    default_request_options,
    RequestOptions,
    encode_param,
    AsyncBaseClient,
    QueryParams,
    SyncBaseClient,
)
import typing
import typing_extensions
from apple_python.types.v1.game_center_app_versions.compatibility_versions import models


class CompatibilityVersionsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        id: str,
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
        fields_game_center_app_versions: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appStoreVersion", "compatibilityVersions", "enabled"
                ]
            ]
        ] = None,
        filter_enabled: typing.Optional[typing.List[str]] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal["appStoreVersion", "compatibilityVersions"]
            ]
        ] = None,
        limit: typing.Optional[int] = None,
        limit_compatibility_versions: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterAppVersionsResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_app_store_versions is not None:
            _query["fields[appStoreVersions]"] = encode_param(
                fields_app_store_versions, False
            )
        if fields_game_center_app_versions is not None:
            _query["fields[gameCenterAppVersions]"] = encode_param(
                fields_game_center_app_versions, False
            )
        if filter_enabled is not None:
            _query["filter[enabled]"] = encode_param(filter_enabled, False)
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        if limit_compatibility_versions is not None:
            _query["limit[compatibilityVersions]"] = encode_param(
                limit_compatibility_versions, False
            )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/gameCenterAppVersions/{id}/compatibilityVersions",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.GameCenterAppVersionsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncCompatibilityVersionsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        id: str,
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
        fields_game_center_app_versions: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appStoreVersion", "compatibilityVersions", "enabled"
                ]
            ]
        ] = None,
        filter_enabled: typing.Optional[typing.List[str]] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal["appStoreVersion", "compatibilityVersions"]
            ]
        ] = None,
        limit: typing.Optional[int] = None,
        limit_compatibility_versions: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterAppVersionsResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_app_store_versions is not None:
            _query["fields[appStoreVersions]"] = encode_param(
                fields_app_store_versions, False
            )
        if fields_game_center_app_versions is not None:
            _query["fields[gameCenterAppVersions]"] = encode_param(
                fields_game_center_app_versions, False
            )
        if filter_enabled is not None:
            _query["filter[enabled]"] = encode_param(filter_enabled, False)
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        if limit_compatibility_versions is not None:
            _query["limit[compatibilityVersions]"] = encode_param(
                limit_compatibility_versions, False
            )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/gameCenterAppVersions/{id}/compatibilityVersions",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.GameCenterAppVersionsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
