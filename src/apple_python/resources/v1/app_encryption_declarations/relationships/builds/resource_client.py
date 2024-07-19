"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    SyncBaseClient,
    AsyncBaseClient,
    to_encodable,
    default_request_options,
    RequestOptions,
)
from apple_python.types.v1.app_encryption_declarations.relationships.builds import (
    params,
)
import typing


class BuildsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.AppEncryptionDeclarationBuildsLinkagesRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerAppEncryptionDeclarationBuildsLinkagesRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path=f"/v1/appEncryptionDeclarations/{id}/relationships/builds",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncBuildsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.AppEncryptionDeclarationBuildsLinkagesRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerAppEncryptionDeclarationBuildsLinkagesRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path=f"/v1/appEncryptionDeclarations/{id}/relationships/builds",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
