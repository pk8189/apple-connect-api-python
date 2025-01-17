"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    AsyncBaseClient,
    SyncBaseClient,
    encode_param,
    RequestOptions,
    default_request_options,
    QueryParams,
)
import typing
import typing_extensions
from apple_python.types.v1.ci_build_runs.actions import models


class ActionsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        id: str,
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
            typing.List[typing_extensions.Literal["buildRun"]]
        ] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CiBuildActionsResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_ci_build_actions is not None:
            _query["fields[ciBuildActions]"] = encode_param(
                fields_ci_build_actions, False
            )
        if fields_ci_build_runs is not None:
            _query["fields[ciBuildRuns]"] = encode_param(fields_ci_build_runs, False)
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/ciBuildRuns/{id}/actions",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.CiBuildActionsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncActionsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        id: str,
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
            typing.List[typing_extensions.Literal["buildRun"]]
        ] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CiBuildActionsResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_ci_build_actions is not None:
            _query["fields[ciBuildActions]"] = encode_param(
                fields_ci_build_actions, False
            )
        if fields_ci_build_runs is not None:
            _query["fields[ciBuildRuns]"] = encode_param(fields_ci_build_runs, False)
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/ciBuildRuns/{id}/actions",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.CiBuildActionsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
