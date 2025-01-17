"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    AsyncBaseClient,
    default_request_options,
    RequestOptions,
    QueryParams,
    SyncBaseClient,
    encode_param,
)
import typing
import typing_extensions
from apple_python.types.v1.ci_issues import models


class CiIssuesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def get(
        self,
        *,
        id: str,
        fields_ci_issues: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "category", "fileSource", "issueType", "message"
                ]
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CiIssueResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_ci_issues is not None:
            _query["fields[ciIssues]"] = encode_param(fields_ci_issues, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/ciIssues/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.CiIssueResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncCiIssuesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def get(
        self,
        *,
        id: str,
        fields_ci_issues: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "category", "fileSource", "issueType", "message"
                ]
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CiIssueResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_ci_issues is not None:
            _query["fields[ciIssues]"] = encode_param(fields_ci_issues, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/ciIssues/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.CiIssueResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
