"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    QueryParams,
    AsyncBaseClient,
    encode_param,
    RequestOptions,
    default_request_options,
    SyncBaseClient,
)
import typing
import typing_extensions
from apple_python.types.v1.profiles.certificates import models


class CertificatesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        id: str,
        fields_certificates: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "certificateContent",
                    "certificateType",
                    "csrContent",
                    "displayName",
                    "expirationDate",
                    "name",
                    "platform",
                    "serialNumber",
                ]
            ]
        ] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CertificatesWithoutIncludesResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_certificates is not None:
            _query["fields[certificates]"] = encode_param(fields_certificates, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/profiles/{id}/certificates",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.CertificatesWithoutIncludesResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncCertificatesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        id: str,
        fields_certificates: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "certificateContent",
                    "certificateType",
                    "csrContent",
                    "displayName",
                    "expirationDate",
                    "name",
                    "platform",
                    "serialNumber",
                ]
            ]
        ] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CertificatesWithoutIncludesResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_certificates is not None:
            _query["fields[certificates]"] = encode_param(fields_certificates, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/profiles/{id}/certificates",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.CertificatesWithoutIncludesResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
