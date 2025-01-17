"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    encode_param,
    RequestOptions,
    SyncBaseClient,
    AsyncBaseClient,
    QueryParams,
    default_request_options,
)
import typing
import typing_extensions
from apple_python.types.v1.apps.app_encryption_declarations import models


class AppEncryptionDeclarationsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        id: str,
        fields_app_encryption_declaration_documents: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appEncryptionDeclaration",
                    "assetDeliveryState",
                    "assetToken",
                    "downloadUrl",
                    "fileName",
                    "fileSize",
                    "sourceFileChecksum",
                    "uploadOperations",
                    "uploaded",
                ]
            ]
        ] = None,
        fields_app_encryption_declarations: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
                    "appDescription",
                    "appEncryptionDeclarationDocument",
                    "appEncryptionDeclarationState",
                    "availableOnFrenchStore",
                    "builds",
                    "codeValue",
                    "containsProprietaryCryptography",
                    "containsThirdPartyCryptography",
                    "createdDate",
                    "documentName",
                    "documentType",
                    "documentUrl",
                    "exempt",
                    "platform",
                    "uploadedDate",
                    "usesEncryption",
                ]
            ]
        ] = None,
        fields_apps: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "alternativeDistributionKey",
                    "analyticsReportRequests",
                    "appAvailability",
                    "appClips",
                    "appCustomProductPages",
                    "appEncryptionDeclarations",
                    "appEvents",
                    "appInfos",
                    "appPricePoints",
                    "appPriceSchedule",
                    "appStoreVersionExperimentsV2",
                    "appStoreVersions",
                    "betaAppLocalizations",
                    "betaAppReviewDetail",
                    "betaGroups",
                    "betaLicenseAgreement",
                    "betaTesters",
                    "builds",
                    "bundleId",
                    "ciProduct",
                    "contentRightsDeclaration",
                    "customerReviews",
                    "endUserLicenseAgreement",
                    "gameCenterDetail",
                    "gameCenterEnabledVersions",
                    "inAppPurchases",
                    "inAppPurchasesV2",
                    "isOrEverWasMadeForKids",
                    "marketplaceSearchDetail",
                    "name",
                    "perfPowerMetrics",
                    "preOrder",
                    "preReleaseVersions",
                    "primaryLocale",
                    "promotedPurchases",
                    "reviewSubmissions",
                    "sku",
                    "subscriptionGracePeriod",
                    "subscriptionGroups",
                    "subscriptionStatusUrl",
                    "subscriptionStatusUrlForSandbox",
                    "subscriptionStatusUrlVersion",
                    "subscriptionStatusUrlVersionForSandbox",
                ]
            ]
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
        filter_builds: typing.Optional[typing.List[str]] = None,
        filter_platform: typing.Optional[
            typing.List[
                typing_extensions.Literal["IOS", "MAC_OS", "TV_OS", "VISION_OS"]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app", "appEncryptionDeclarationDocument", "builds"
                ]
            ]
        ] = None,
        limit: typing.Optional[int] = None,
        limit_builds: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppEncryptionDeclarationsResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_app_encryption_declaration_documents is not None:
            _query["fields[appEncryptionDeclarationDocuments]"] = encode_param(
                fields_app_encryption_declaration_documents, False
            )
        if fields_app_encryption_declarations is not None:
            _query["fields[appEncryptionDeclarations]"] = encode_param(
                fields_app_encryption_declarations, False
            )
        if fields_apps is not None:
            _query["fields[apps]"] = encode_param(fields_apps, False)
        if fields_builds is not None:
            _query["fields[builds]"] = encode_param(fields_builds, False)
        if filter_builds is not None:
            _query["filter[builds]"] = encode_param(filter_builds, False)
        if filter_platform is not None:
            _query["filter[platform]"] = encode_param(filter_platform, False)
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        if limit_builds is not None:
            _query["limit[builds]"] = encode_param(limit_builds, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/apps/{id}/appEncryptionDeclarations",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppEncryptionDeclarationsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncAppEncryptionDeclarationsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        id: str,
        fields_app_encryption_declaration_documents: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appEncryptionDeclaration",
                    "assetDeliveryState",
                    "assetToken",
                    "downloadUrl",
                    "fileName",
                    "fileSize",
                    "sourceFileChecksum",
                    "uploadOperations",
                    "uploaded",
                ]
            ]
        ] = None,
        fields_app_encryption_declarations: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
                    "appDescription",
                    "appEncryptionDeclarationDocument",
                    "appEncryptionDeclarationState",
                    "availableOnFrenchStore",
                    "builds",
                    "codeValue",
                    "containsProprietaryCryptography",
                    "containsThirdPartyCryptography",
                    "createdDate",
                    "documentName",
                    "documentType",
                    "documentUrl",
                    "exempt",
                    "platform",
                    "uploadedDate",
                    "usesEncryption",
                ]
            ]
        ] = None,
        fields_apps: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "alternativeDistributionKey",
                    "analyticsReportRequests",
                    "appAvailability",
                    "appClips",
                    "appCustomProductPages",
                    "appEncryptionDeclarations",
                    "appEvents",
                    "appInfos",
                    "appPricePoints",
                    "appPriceSchedule",
                    "appStoreVersionExperimentsV2",
                    "appStoreVersions",
                    "betaAppLocalizations",
                    "betaAppReviewDetail",
                    "betaGroups",
                    "betaLicenseAgreement",
                    "betaTesters",
                    "builds",
                    "bundleId",
                    "ciProduct",
                    "contentRightsDeclaration",
                    "customerReviews",
                    "endUserLicenseAgreement",
                    "gameCenterDetail",
                    "gameCenterEnabledVersions",
                    "inAppPurchases",
                    "inAppPurchasesV2",
                    "isOrEverWasMadeForKids",
                    "marketplaceSearchDetail",
                    "name",
                    "perfPowerMetrics",
                    "preOrder",
                    "preReleaseVersions",
                    "primaryLocale",
                    "promotedPurchases",
                    "reviewSubmissions",
                    "sku",
                    "subscriptionGracePeriod",
                    "subscriptionGroups",
                    "subscriptionStatusUrl",
                    "subscriptionStatusUrlForSandbox",
                    "subscriptionStatusUrlVersion",
                    "subscriptionStatusUrlVersionForSandbox",
                ]
            ]
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
        filter_builds: typing.Optional[typing.List[str]] = None,
        filter_platform: typing.Optional[
            typing.List[
                typing_extensions.Literal["IOS", "MAC_OS", "TV_OS", "VISION_OS"]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app", "appEncryptionDeclarationDocument", "builds"
                ]
            ]
        ] = None,
        limit: typing.Optional[int] = None,
        limit_builds: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppEncryptionDeclarationsResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_app_encryption_declaration_documents is not None:
            _query["fields[appEncryptionDeclarationDocuments]"] = encode_param(
                fields_app_encryption_declaration_documents, False
            )
        if fields_app_encryption_declarations is not None:
            _query["fields[appEncryptionDeclarations]"] = encode_param(
                fields_app_encryption_declarations, False
            )
        if fields_apps is not None:
            _query["fields[apps]"] = encode_param(fields_apps, False)
        if fields_builds is not None:
            _query["fields[builds]"] = encode_param(fields_builds, False)
        if filter_builds is not None:
            _query["filter[builds]"] = encode_param(filter_builds, False)
        if filter_platform is not None:
            _query["filter[platform]"] = encode_param(filter_platform, False)
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        if limit_builds is not None:
            _query["limit[builds]"] = encode_param(limit_builds, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/apps/{id}/appEncryptionDeclarations",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppEncryptionDeclarationsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
