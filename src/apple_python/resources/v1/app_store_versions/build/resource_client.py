"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    QueryParams,
    AsyncBaseClient,
    SyncBaseClient,
    encode_param,
    RequestOptions,
    default_request_options,
)
import typing
import typing_extensions
from apple_python.types.v1.app_store_versions.build import models


class BuildClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        id: str,
        fields_builds: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
                    "appEncryptionDeclaration",
                    "appStoreVersion",
                    "betaAppReviewSubmission",
                    "betaBuildLocalizations",
                    "betaGroups",
                    "buildAudienceType",
                    "buildBetaDetail",
                    "buildBundles",
                    "computedMinMacOsVersion",
                    "diagnosticSignatures",
                    "expirationDate",
                    "expired",
                    "iconAssetToken",
                    "icons",
                    "individualTesters",
                    "lsMinimumSystemVersion",
                    "minOsVersion",
                    "perfPowerMetrics",
                    "preReleaseVersion",
                    "processingState",
                    "uploadedDate",
                    "usesNonExemptEncryption",
                    "version",
                ]
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BuildWithoutIncludesResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_builds is not None:
            _query["fields[builds]"] = encode_param(fields_builds, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/appStoreVersions/{id}/build",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.BuildWithoutIncludesResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncBuildClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        id: str,
        fields_builds: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
                    "appEncryptionDeclaration",
                    "appStoreVersion",
                    "betaAppReviewSubmission",
                    "betaBuildLocalizations",
                    "betaGroups",
                    "buildAudienceType",
                    "buildBetaDetail",
                    "buildBundles",
                    "computedMinMacOsVersion",
                    "diagnosticSignatures",
                    "expirationDate",
                    "expired",
                    "iconAssetToken",
                    "icons",
                    "individualTesters",
                    "lsMinimumSystemVersion",
                    "minOsVersion",
                    "perfPowerMetrics",
                    "preReleaseVersion",
                    "processingState",
                    "uploadedDate",
                    "usesNonExemptEncryption",
                    "version",
                ]
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BuildWithoutIncludesResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_builds is not None:
            _query["fields[builds]"] = encode_param(fields_builds, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/appStoreVersions/{id}/build",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.BuildWithoutIncludesResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
