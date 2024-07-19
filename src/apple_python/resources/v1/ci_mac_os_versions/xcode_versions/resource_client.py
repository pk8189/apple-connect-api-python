"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    encode_param,
    AsyncBaseClient,
    SyncBaseClient,
    default_request_options,
    RequestOptions,
    QueryParams,
)
import typing
import typing_extensions
from apple_python.types.v1.ci_mac_os_versions.xcode_versions import models


class XcodeVersionsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        id: str,
        fields_ci_mac_os_versions: typing.Optional[
            typing.List[typing_extensions.Literal["name", "version", "xcodeVersions"]]
        ] = None,
        fields_ci_xcode_versions: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "macOsVersions", "name", "testDestinations", "version"
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[typing_extensions.Literal["macOsVersions"]]
        ] = None,
        limit: typing.Optional[int] = None,
        limit_mac_os_versions: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CiXcodeVersionsResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_ci_mac_os_versions is not None:
            _query["fields[ciMacOsVersions]"] = encode_param(
                fields_ci_mac_os_versions, False
            )
        if fields_ci_xcode_versions is not None:
            _query["fields[ciXcodeVersions]"] = encode_param(
                fields_ci_xcode_versions, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        if limit_mac_os_versions is not None:
            _query["limit[macOsVersions]"] = encode_param(limit_mac_os_versions, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/ciMacOsVersions/{id}/xcodeVersions",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.CiXcodeVersionsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncXcodeVersionsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        id: str,
        fields_ci_mac_os_versions: typing.Optional[
            typing.List[typing_extensions.Literal["name", "version", "xcodeVersions"]]
        ] = None,
        fields_ci_xcode_versions: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "macOsVersions", "name", "testDestinations", "version"
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[typing_extensions.Literal["macOsVersions"]]
        ] = None,
        limit: typing.Optional[int] = None,
        limit_mac_os_versions: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CiXcodeVersionsResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_ci_mac_os_versions is not None:
            _query["fields[ciMacOsVersions]"] = encode_param(
                fields_ci_mac_os_versions, False
            )
        if fields_ci_xcode_versions is not None:
            _query["fields[ciXcodeVersions]"] = encode_param(
                fields_ci_xcode_versions, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        if limit_mac_os_versions is not None:
            _query["limit[macOsVersions]"] = encode_param(limit_mac_os_versions, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/ciMacOsVersions/{id}/xcodeVersions",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.CiXcodeVersionsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)