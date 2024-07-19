"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    AsyncBaseClient,
    SyncBaseClient,
    to_encodable,
    QueryParams,
    default_request_options,
    RequestOptions,
    encode_param,
)
from apple_python.resources.v1.ci_build_runs.actions import (
    ActionsClient,
    AsyncActionsClient,
)
from apple_python.resources.v1.ci_build_runs.builds import (
    BuildsClient,
    AsyncBuildsClient,
)
import typing
import typing_extensions
from apple_python.types.v1.ci_build_runs import params, models


class CiBuildRunsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.actions = ActionsClient(base_client=self._base_client)
        self.builds = BuildsClient(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.CiBuildRunCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CiBuildRunResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerCiBuildRunCreateRequest
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/v1/ciBuildRuns",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.CiBuildRunResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def get(
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
        fields_ci_build_actions: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "actionType",
                    "artifacts",
                    "buildRun",
                    "completionStatus",
                    "executionProgress",
                    "finishedDate",
                    "isRequiredToPass",
                    "issueCounts",
                    "issues",
                    "name",
                    "startedDate",
                    "testResults",
                ]
            ]
        ] = None,
        fields_ci_build_runs: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "actions",
                    "buildRun",
                    "builds",
                    "cancelReason",
                    "clean",
                    "completionStatus",
                    "createdDate",
                    "destinationBranch",
                    "destinationCommit",
                    "executionProgress",
                    "finishedDate",
                    "isPullRequestBuild",
                    "issueCounts",
                    "number",
                    "product",
                    "pullRequest",
                    "sourceBranchOrTag",
                    "sourceCommit",
                    "startReason",
                    "startedDate",
                    "workflow",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "builds",
                    "destinationBranch",
                    "product",
                    "pullRequest",
                    "sourceBranchOrTag",
                    "workflow",
                ]
            ]
        ] = None,
        limit_builds: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CiBuildRunResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_builds is not None:
            _query["fields[builds]"] = encode_param(fields_builds, False)
        if fields_ci_build_actions is not None:
            _query["fields[ciBuildActions]"] = encode_param(
                fields_ci_build_actions, False
            )
        if fields_ci_build_runs is not None:
            _query["fields[ciBuildRuns]"] = encode_param(fields_ci_build_runs, False)
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit_builds is not None:
            _query["limit[builds]"] = encode_param(limit_builds, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/ciBuildRuns/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.CiBuildRunResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncCiBuildRunsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.actions = AsyncActionsClient(base_client=self._base_client)
        self.builds = AsyncBuildsClient(base_client=self._base_client)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.CiBuildRunCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CiBuildRunResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerCiBuildRunCreateRequest
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/v1/ciBuildRuns",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.CiBuildRunResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def get(
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
        fields_ci_build_actions: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "actionType",
                    "artifacts",
                    "buildRun",
                    "completionStatus",
                    "executionProgress",
                    "finishedDate",
                    "isRequiredToPass",
                    "issueCounts",
                    "issues",
                    "name",
                    "startedDate",
                    "testResults",
                ]
            ]
        ] = None,
        fields_ci_build_runs: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "actions",
                    "buildRun",
                    "builds",
                    "cancelReason",
                    "clean",
                    "completionStatus",
                    "createdDate",
                    "destinationBranch",
                    "destinationCommit",
                    "executionProgress",
                    "finishedDate",
                    "isPullRequestBuild",
                    "issueCounts",
                    "number",
                    "product",
                    "pullRequest",
                    "sourceBranchOrTag",
                    "sourceCommit",
                    "startReason",
                    "startedDate",
                    "workflow",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "builds",
                    "destinationBranch",
                    "product",
                    "pullRequest",
                    "sourceBranchOrTag",
                    "workflow",
                ]
            ]
        ] = None,
        limit_builds: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CiBuildRunResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_builds is not None:
            _query["fields[builds]"] = encode_param(fields_builds, False)
        if fields_ci_build_actions is not None:
            _query["fields[ciBuildActions]"] = encode_param(
                fields_ci_build_actions, False
            )
        if fields_ci_build_runs is not None:
            _query["fields[ciBuildRuns]"] = encode_param(fields_ci_build_runs, False)
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit_builds is not None:
            _query["limit[builds]"] = encode_param(limit_builds, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/ciBuildRuns/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.CiBuildRunResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
