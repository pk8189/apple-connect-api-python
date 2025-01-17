"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    AsyncBaseClient,
    default_request_options,
    encode_param,
    QueryParams,
    SyncBaseClient,
    RequestOptions,
)
import typing
import typing_extensions
from apple_python.types.v1.ci_build_actions.artifacts import models


class ArtifactsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        id: str,
        fields_ci_artifacts: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "downloadUrl", "fileName", "fileSize", "fileType"
                ]
            ]
        ] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CiArtifactsResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_ci_artifacts is not None:
            _query["fields[ciArtifacts]"] = encode_param(fields_ci_artifacts, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/ciBuildActions/{id}/artifacts",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.CiArtifactsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncArtifactsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        id: str,
        fields_ci_artifacts: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "downloadUrl", "fileName", "fileSize", "fileType"
                ]
            ]
        ] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CiArtifactsResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_ci_artifacts is not None:
            _query["fields[ciArtifacts]"] = encode_param(fields_ci_artifacts, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/ciBuildActions/{id}/artifacts",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.CiArtifactsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
