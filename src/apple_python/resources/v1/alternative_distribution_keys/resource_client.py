"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    encode_param,
    to_encodable,
    default_request_options,
    QueryParams,
)
import typing
import typing_extensions
from apple_python.types.v1.alternative_distribution_keys import params, models


class AlternativeDistributionKeysClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.AlternativeDistributionKeyCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AlternativeDistributionKeyResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerAlternativeDistributionKeyCreateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/v1/alternativeDistributionKeys",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.AlternativeDistributionKeyResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def get(
        self,
        *,
        id: str,
        fields_alternative_distribution_keys: typing.Optional[
            typing.List[typing_extensions.Literal["app", "publicKey"]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AlternativeDistributionKeyResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_alternative_distribution_keys is not None:
            _query["fields[alternativeDistributionKeys]"] = encode_param(
                fields_alternative_distribution_keys, False
            )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/alternativeDistributionKeys/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AlternativeDistributionKeyResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def list(
        self,
        *,
        exists_app: typing.Optional[bool] = None,
        fields_alternative_distribution_keys: typing.Optional[
            typing.List[typing_extensions.Literal["app", "publicKey"]]
        ] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AlternativeDistributionKeysResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if exists_app is not None:
            _query["exists[app]"] = encode_param(exists_app, False)
        if fields_alternative_distribution_keys is not None:
            _query["fields[alternativeDistributionKeys]"] = encode_param(
                fields_alternative_distribution_keys, False
            )
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path="/v1/alternativeDistributionKeys",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AlternativeDistributionKeysResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def delete(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="DELETE",
            path=f"/v1/alternativeDistributionKeys/{id}",
            auth_names=["itc-bearer-token"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncAlternativeDistributionKeysClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.AlternativeDistributionKeyCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AlternativeDistributionKeyResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerAlternativeDistributionKeyCreateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/v1/alternativeDistributionKeys",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.AlternativeDistributionKeyResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def get(
        self,
        *,
        id: str,
        fields_alternative_distribution_keys: typing.Optional[
            typing.List[typing_extensions.Literal["app", "publicKey"]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AlternativeDistributionKeyResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_alternative_distribution_keys is not None:
            _query["fields[alternativeDistributionKeys]"] = encode_param(
                fields_alternative_distribution_keys, False
            )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/alternativeDistributionKeys/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AlternativeDistributionKeyResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def list(
        self,
        *,
        exists_app: typing.Optional[bool] = None,
        fields_alternative_distribution_keys: typing.Optional[
            typing.List[typing_extensions.Literal["app", "publicKey"]]
        ] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AlternativeDistributionKeysResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if exists_app is not None:
            _query["exists[app]"] = encode_param(exists_app, False)
        if fields_alternative_distribution_keys is not None:
            _query["fields[alternativeDistributionKeys]"] = encode_param(
                fields_alternative_distribution_keys, False
            )
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path="/v1/alternativeDistributionKeys",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AlternativeDistributionKeysResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def delete(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="DELETE",
            path=f"/v1/alternativeDistributionKeys/{id}",
            auth_names=["itc-bearer-token"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)