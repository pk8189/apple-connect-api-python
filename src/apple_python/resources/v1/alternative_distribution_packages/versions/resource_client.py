"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    QueryParams,
    encode_param,
    default_request_options,
    SyncBaseClient,
    AsyncBaseClient,
    RequestOptions,
)
import typing
import typing_extensions
from apple_python.types.v1.alternative_distribution_packages.versions import models


class VersionsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        id: str,
        fields_alternative_distribution_package_deltas: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "alternativeDistributionKeyBlob",
                    "fileChecksum",
                    "url",
                    "urlExpirationDate",
                ]
            ]
        ] = None,
        fields_alternative_distribution_package_variants: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "alternativeDistributionKeyBlob",
                    "fileChecksum",
                    "url",
                    "urlExpirationDate",
                ]
            ]
        ] = None,
        fields_alternative_distribution_package_versions: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "alternativeDistributionPackage",
                    "deltas",
                    "fileChecksum",
                    "state",
                    "url",
                    "urlExpirationDate",
                    "variants",
                    "version",
                ]
            ]
        ] = None,
        fields_alternative_distribution_packages: typing.Optional[
            typing.List[typing_extensions.Literal["appStoreVersion", "versions"]]
        ] = None,
        filter_state: typing.Optional[
            typing.List[typing_extensions.Literal["COMPLETED", "REPLACED"]]
        ] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "alternativeDistributionPackage", "deltas", "variants"
                ]
            ]
        ] = None,
        limit: typing.Optional[int] = None,
        limit_deltas: typing.Optional[int] = None,
        limit_variants: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AlternativeDistributionPackageVersionsResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_alternative_distribution_package_deltas is not None:
            _query["fields[alternativeDistributionPackageDeltas]"] = encode_param(
                fields_alternative_distribution_package_deltas, False
            )
        if fields_alternative_distribution_package_variants is not None:
            _query["fields[alternativeDistributionPackageVariants]"] = encode_param(
                fields_alternative_distribution_package_variants, False
            )
        if fields_alternative_distribution_package_versions is not None:
            _query["fields[alternativeDistributionPackageVersions]"] = encode_param(
                fields_alternative_distribution_package_versions, False
            )
        if fields_alternative_distribution_packages is not None:
            _query["fields[alternativeDistributionPackages]"] = encode_param(
                fields_alternative_distribution_packages, False
            )
        if filter_state is not None:
            _query["filter[state]"] = encode_param(filter_state, False)
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        if limit_deltas is not None:
            _query["limit[deltas]"] = encode_param(limit_deltas, False)
        if limit_variants is not None:
            _query["limit[variants]"] = encode_param(limit_variants, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/alternativeDistributionPackages/{id}/versions",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AlternativeDistributionPackageVersionsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncVersionsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        id: str,
        fields_alternative_distribution_package_deltas: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "alternativeDistributionKeyBlob",
                    "fileChecksum",
                    "url",
                    "urlExpirationDate",
                ]
            ]
        ] = None,
        fields_alternative_distribution_package_variants: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "alternativeDistributionKeyBlob",
                    "fileChecksum",
                    "url",
                    "urlExpirationDate",
                ]
            ]
        ] = None,
        fields_alternative_distribution_package_versions: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "alternativeDistributionPackage",
                    "deltas",
                    "fileChecksum",
                    "state",
                    "url",
                    "urlExpirationDate",
                    "variants",
                    "version",
                ]
            ]
        ] = None,
        fields_alternative_distribution_packages: typing.Optional[
            typing.List[typing_extensions.Literal["appStoreVersion", "versions"]]
        ] = None,
        filter_state: typing.Optional[
            typing.List[typing_extensions.Literal["COMPLETED", "REPLACED"]]
        ] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "alternativeDistributionPackage", "deltas", "variants"
                ]
            ]
        ] = None,
        limit: typing.Optional[int] = None,
        limit_deltas: typing.Optional[int] = None,
        limit_variants: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AlternativeDistributionPackageVersionsResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_alternative_distribution_package_deltas is not None:
            _query["fields[alternativeDistributionPackageDeltas]"] = encode_param(
                fields_alternative_distribution_package_deltas, False
            )
        if fields_alternative_distribution_package_variants is not None:
            _query["fields[alternativeDistributionPackageVariants]"] = encode_param(
                fields_alternative_distribution_package_variants, False
            )
        if fields_alternative_distribution_package_versions is not None:
            _query["fields[alternativeDistributionPackageVersions]"] = encode_param(
                fields_alternative_distribution_package_versions, False
            )
        if fields_alternative_distribution_packages is not None:
            _query["fields[alternativeDistributionPackages]"] = encode_param(
                fields_alternative_distribution_packages, False
            )
        if filter_state is not None:
            _query["filter[state]"] = encode_param(filter_state, False)
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        if limit_deltas is not None:
            _query["limit[deltas]"] = encode_param(limit_deltas, False)
        if limit_variants is not None:
            _query["limit[variants]"] = encode_param(limit_variants, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/alternativeDistributionPackages/{id}/versions",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AlternativeDistributionPackageVersionsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)