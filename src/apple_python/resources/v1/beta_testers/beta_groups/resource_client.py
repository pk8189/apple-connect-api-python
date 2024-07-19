"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    encode_param,
    QueryParams,
    default_request_options,
    SyncBaseClient,
    AsyncBaseClient,
    RequestOptions,
)
import typing
import typing_extensions
from apple_python.types.v1.beta_testers.beta_groups import models


class BetaGroupsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        id: str,
        fields_beta_groups: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
                    "betaTesters",
                    "builds",
                    "createdDate",
                    "feedbackEnabled",
                    "hasAccessToAllBuilds",
                    "iosBuildsAvailableForAppleSiliconMac",
                    "isInternalGroup",
                    "name",
                    "publicLink",
                    "publicLinkEnabled",
                    "publicLinkId",
                    "publicLinkLimit",
                    "publicLinkLimitEnabled",
                ]
            ]
        ] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BetaGroupsWithoutIncludesResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_beta_groups is not None:
            _query["fields[betaGroups]"] = encode_param(fields_beta_groups, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/betaTesters/{id}/betaGroups",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.BetaGroupsWithoutIncludesResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncBetaGroupsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        id: str,
        fields_beta_groups: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
                    "betaTesters",
                    "builds",
                    "createdDate",
                    "feedbackEnabled",
                    "hasAccessToAllBuilds",
                    "iosBuildsAvailableForAppleSiliconMac",
                    "isInternalGroup",
                    "name",
                    "publicLink",
                    "publicLinkEnabled",
                    "publicLinkId",
                    "publicLinkLimit",
                    "publicLinkLimitEnabled",
                ]
            ]
        ] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BetaGroupsWithoutIncludesResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_beta_groups is not None:
            _query["fields[betaGroups]"] = encode_param(fields_beta_groups, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/betaTesters/{id}/betaGroups",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.BetaGroupsWithoutIncludesResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
