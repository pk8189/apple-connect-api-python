"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    SyncBaseClient,
    encode_param,
    RequestOptions,
    QueryParams,
    default_request_options,
    AsyncBaseClient,
)
import typing
import typing_extensions
from apple_python.types.v1.scm_repositories.pull_requests import models


class PullRequestsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        id: str,
        fields_scm_pull_requests: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "destinationBranchName",
                    "destinationRepositoryName",
                    "destinationRepositoryOwner",
                    "isClosed",
                    "isCrossRepository",
                    "number",
                    "repository",
                    "sourceBranchName",
                    "sourceRepositoryName",
                    "sourceRepositoryOwner",
                    "title",
                    "webUrl",
                ]
            ]
        ] = None,
        fields_scm_repositories: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "defaultBranch",
                    "gitReferences",
                    "httpCloneUrl",
                    "lastAccessedDate",
                    "ownerName",
                    "pullRequests",
                    "repositoryName",
                    "scmProvider",
                    "sshCloneUrl",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[typing_extensions.Literal["repository"]]
        ] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ScmPullRequestsResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_scm_pull_requests is not None:
            _query["fields[scmPullRequests]"] = encode_param(
                fields_scm_pull_requests, False
            )
        if fields_scm_repositories is not None:
            _query["fields[scmRepositories]"] = encode_param(
                fields_scm_repositories, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/scmRepositories/{id}/pullRequests",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.ScmPullRequestsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncPullRequestsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        id: str,
        fields_scm_pull_requests: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "destinationBranchName",
                    "destinationRepositoryName",
                    "destinationRepositoryOwner",
                    "isClosed",
                    "isCrossRepository",
                    "number",
                    "repository",
                    "sourceBranchName",
                    "sourceRepositoryName",
                    "sourceRepositoryOwner",
                    "title",
                    "webUrl",
                ]
            ]
        ] = None,
        fields_scm_repositories: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "defaultBranch",
                    "gitReferences",
                    "httpCloneUrl",
                    "lastAccessedDate",
                    "ownerName",
                    "pullRequests",
                    "repositoryName",
                    "scmProvider",
                    "sshCloneUrl",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[typing_extensions.Literal["repository"]]
        ] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ScmPullRequestsResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_scm_pull_requests is not None:
            _query["fields[scmPullRequests]"] = encode_param(
                fields_scm_pull_requests, False
            )
        if fields_scm_repositories is not None:
            _query["fields[scmRepositories]"] = encode_param(
                fields_scm_repositories, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/scmRepositories/{id}/pullRequests",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.ScmPullRequestsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)