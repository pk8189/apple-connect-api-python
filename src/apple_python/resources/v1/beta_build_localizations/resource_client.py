"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    AsyncBaseClient,
    default_request_options,
    to_encodable,
    RequestOptions,
    QueryParams,
    SyncBaseClient,
    encode_param,
)
from apple_python.resources.v1.beta_build_localizations.build import (
    AsyncBuildClient,
    BuildClient,
)
import typing
import typing_extensions
from apple_python.types.v1.beta_build_localizations import params, models


class BetaBuildLocalizationsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.build = BuildClient(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.BetaBuildLocalizationCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BetaBuildLocalizationResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerBetaBuildLocalizationCreateRequest
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/v1/betaBuildLocalizations",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.BetaBuildLocalizationResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def patch(
        self,
        *,
        data: params.BetaBuildLocalizationUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BetaBuildLocalizationResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerBetaBuildLocalizationUpdateRequest
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="PATCH",
            path=f"/v1/betaBuildLocalizations/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.BetaBuildLocalizationResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def get(
        self,
        *,
        id: str,
        fields_beta_build_localizations: typing.Optional[
            typing.List[typing_extensions.Literal["build", "locale", "whatsNew"]]
        ] = None,
        fields_builds: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
                    "appEncryptionDeclaration",
                    "appStoreVersion",
                    "betaAppReviewSubmission",
                    "betaBuildLocalizations",
                    "betaGroups",
                    "buildAudienceType",
                    "buildBetaDetail",
                    "buildBundles",
                    "computedMinMacOsVersion",
                    "diagnosticSignatures",
                    "expirationDate",
                    "expired",
                    "iconAssetToken",
                    "icons",
                    "individualTesters",
                    "lsMinimumSystemVersion",
                    "minOsVersion",
                    "perfPowerMetrics",
                    "preReleaseVersion",
                    "processingState",
                    "uploadedDate",
                    "usesNonExemptEncryption",
                    "version",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[typing_extensions.Literal["build"]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BetaBuildLocalizationResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_beta_build_localizations is not None:
            _query["fields[betaBuildLocalizations]"] = encode_param(
                fields_beta_build_localizations, False
            )
        if fields_builds is not None:
            _query["fields[builds]"] = encode_param(fields_builds, False)
        if include is not None:
            _query["include"] = encode_param(include, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/betaBuildLocalizations/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.BetaBuildLocalizationResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def list(
        self,
        *,
        fields_beta_build_localizations: typing.Optional[
            typing.List[typing_extensions.Literal["build", "locale", "whatsNew"]]
        ] = None,
        fields_builds: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
                    "appEncryptionDeclaration",
                    "appStoreVersion",
                    "betaAppReviewSubmission",
                    "betaBuildLocalizations",
                    "betaGroups",
                    "buildAudienceType",
                    "buildBetaDetail",
                    "buildBundles",
                    "computedMinMacOsVersion",
                    "diagnosticSignatures",
                    "expirationDate",
                    "expired",
                    "iconAssetToken",
                    "icons",
                    "individualTesters",
                    "lsMinimumSystemVersion",
                    "minOsVersion",
                    "perfPowerMetrics",
                    "preReleaseVersion",
                    "processingState",
                    "uploadedDate",
                    "usesNonExemptEncryption",
                    "version",
                ]
            ]
        ] = None,
        filter_build: typing.Optional[typing.List[str]] = None,
        filter_locale: typing.Optional[typing.List[str]] = None,
        include: typing.Optional[
            typing.List[typing_extensions.Literal["build"]]
        ] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BetaBuildLocalizationsResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_beta_build_localizations is not None:
            _query["fields[betaBuildLocalizations]"] = encode_param(
                fields_beta_build_localizations, False
            )
        if fields_builds is not None:
            _query["fields[builds]"] = encode_param(fields_builds, False)
        if filter_build is not None:
            _query["filter[build]"] = encode_param(filter_build, False)
        if filter_locale is not None:
            _query["filter[locale]"] = encode_param(filter_locale, False)
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path="/v1/betaBuildLocalizations",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.BetaBuildLocalizationsResponse,
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
            path=f"/v1/betaBuildLocalizations/{id}",
            auth_names=["itc-bearer-token"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncBetaBuildLocalizationsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.build = AsyncBuildClient(base_client=self._base_client)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.BetaBuildLocalizationCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BetaBuildLocalizationResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerBetaBuildLocalizationCreateRequest
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/v1/betaBuildLocalizations",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.BetaBuildLocalizationResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def patch(
        self,
        *,
        data: params.BetaBuildLocalizationUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BetaBuildLocalizationResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerBetaBuildLocalizationUpdateRequest
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="PATCH",
            path=f"/v1/betaBuildLocalizations/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.BetaBuildLocalizationResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def get(
        self,
        *,
        id: str,
        fields_beta_build_localizations: typing.Optional[
            typing.List[typing_extensions.Literal["build", "locale", "whatsNew"]]
        ] = None,
        fields_builds: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
                    "appEncryptionDeclaration",
                    "appStoreVersion",
                    "betaAppReviewSubmission",
                    "betaBuildLocalizations",
                    "betaGroups",
                    "buildAudienceType",
                    "buildBetaDetail",
                    "buildBundles",
                    "computedMinMacOsVersion",
                    "diagnosticSignatures",
                    "expirationDate",
                    "expired",
                    "iconAssetToken",
                    "icons",
                    "individualTesters",
                    "lsMinimumSystemVersion",
                    "minOsVersion",
                    "perfPowerMetrics",
                    "preReleaseVersion",
                    "processingState",
                    "uploadedDate",
                    "usesNonExemptEncryption",
                    "version",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[typing_extensions.Literal["build"]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BetaBuildLocalizationResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_beta_build_localizations is not None:
            _query["fields[betaBuildLocalizations]"] = encode_param(
                fields_beta_build_localizations, False
            )
        if fields_builds is not None:
            _query["fields[builds]"] = encode_param(fields_builds, False)
        if include is not None:
            _query["include"] = encode_param(include, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/betaBuildLocalizations/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.BetaBuildLocalizationResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def list(
        self,
        *,
        fields_beta_build_localizations: typing.Optional[
            typing.List[typing_extensions.Literal["build", "locale", "whatsNew"]]
        ] = None,
        fields_builds: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
                    "appEncryptionDeclaration",
                    "appStoreVersion",
                    "betaAppReviewSubmission",
                    "betaBuildLocalizations",
                    "betaGroups",
                    "buildAudienceType",
                    "buildBetaDetail",
                    "buildBundles",
                    "computedMinMacOsVersion",
                    "diagnosticSignatures",
                    "expirationDate",
                    "expired",
                    "iconAssetToken",
                    "icons",
                    "individualTesters",
                    "lsMinimumSystemVersion",
                    "minOsVersion",
                    "perfPowerMetrics",
                    "preReleaseVersion",
                    "processingState",
                    "uploadedDate",
                    "usesNonExemptEncryption",
                    "version",
                ]
            ]
        ] = None,
        filter_build: typing.Optional[typing.List[str]] = None,
        filter_locale: typing.Optional[typing.List[str]] = None,
        include: typing.Optional[
            typing.List[typing_extensions.Literal["build"]]
        ] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BetaBuildLocalizationsResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_beta_build_localizations is not None:
            _query["fields[betaBuildLocalizations]"] = encode_param(
                fields_beta_build_localizations, False
            )
        if fields_builds is not None:
            _query["fields[builds]"] = encode_param(fields_builds, False)
        if filter_build is not None:
            _query["filter[build]"] = encode_param(filter_build, False)
        if filter_locale is not None:
            _query["filter[locale]"] = encode_param(filter_locale, False)
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path="/v1/betaBuildLocalizations",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.BetaBuildLocalizationsResponse,
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
            path=f"/v1/betaBuildLocalizations/{id}",
            auth_names=["itc-bearer-token"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
