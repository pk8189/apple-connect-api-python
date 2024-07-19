"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    encode_param,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    QueryParams,
    AsyncBaseClient,
)
import typing
import typing_extensions
from apple_python.types.v1.game_center_app_versions.app_store_version import models


class AppStoreVersionClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        id: str,
        fields_age_rating_declarations: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "ageRatingOverride",
                    "alcoholTobaccoOrDrugUseOrReferences",
                    "contests",
                    "gambling",
                    "gamblingAndContests",
                    "gamblingSimulated",
                    "horrorOrFearThemes",
                    "kidsAgeBand",
                    "matureOrSuggestiveThemes",
                    "medicalOrTreatmentInformation",
                    "profanityOrCrudeHumor",
                    "seventeenPlus",
                    "sexualContentGraphicAndNudity",
                    "sexualContentOrNudity",
                    "unrestrictedWebAccess",
                    "violenceCartoonOrFantasy",
                    "violenceRealistic",
                    "violenceRealisticProlongedGraphicOrSadistic",
                ]
            ]
        ] = None,
        fields_alternative_distribution_packages: typing.Optional[
            typing.List[typing_extensions.Literal["appStoreVersion", "versions"]]
        ] = None,
        fields_app_clip_default_experiences: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "action",
                    "appClip",
                    "appClipAppStoreReviewDetail",
                    "appClipDefaultExperienceLocalizations",
                    "appClipDefaultExperienceTemplate",
                    "releaseWithAppStoreVersion",
                ]
            ]
        ] = None,
        fields_app_store_review_details: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appStoreReviewAttachments",
                    "appStoreVersion",
                    "contactEmail",
                    "contactFirstName",
                    "contactLastName",
                    "contactPhone",
                    "demoAccountName",
                    "demoAccountPassword",
                    "demoAccountRequired",
                    "notes",
                ]
            ]
        ] = None,
        fields_app_store_version_experiments: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
                    "appStoreVersion",
                    "appStoreVersionExperimentTreatments",
                    "controlVersions",
                    "endDate",
                    "latestControlVersion",
                    "name",
                    "platform",
                    "reviewRequired",
                    "startDate",
                    "started",
                    "state",
                    "trafficProportion",
                ]
            ]
        ] = None,
        fields_app_store_version_localizations: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appPreviewSets",
                    "appScreenshotSets",
                    "appStoreVersion",
                    "description",
                    "keywords",
                    "locale",
                    "marketingUrl",
                    "promotionalText",
                    "supportUrl",
                    "whatsNew",
                ]
            ]
        ] = None,
        fields_app_store_version_phased_releases: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appStoreVersion",
                    "currentDayNumber",
                    "phasedReleaseState",
                    "startDate",
                    "totalPauseDuration",
                ]
            ]
        ] = None,
        fields_app_store_version_submissions: typing.Optional[
            typing.List[typing_extensions.Literal["appStoreVersion"]]
        ] = None,
        fields_app_store_versions: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "ageRatingDeclaration",
                    "alternativeDistributionPackage",
                    "app",
                    "appClipDefaultExperience",
                    "appStoreReviewDetail",
                    "appStoreState",
                    "appStoreVersionExperiments",
                    "appStoreVersionExperimentsV2",
                    "appStoreVersionLocalizations",
                    "appStoreVersionPhasedRelease",
                    "appStoreVersionSubmission",
                    "appVersionState",
                    "build",
                    "copyright",
                    "createdDate",
                    "customerReviews",
                    "downloadable",
                    "earliestReleaseDate",
                    "platform",
                    "releaseType",
                    "reviewType",
                    "routingAppCoverage",
                    "versionString",
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
        fields_routing_app_coverages: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appStoreVersion",
                    "assetDeliveryState",
                    "fileName",
                    "fileSize",
                    "sourceFileChecksum",
                    "uploadOperations",
                    "uploaded",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "ageRatingDeclaration",
                    "alternativeDistributionPackage",
                    "app",
                    "appClipDefaultExperience",
                    "appStoreReviewDetail",
                    "appStoreVersionExperiments",
                    "appStoreVersionExperimentsV2",
                    "appStoreVersionLocalizations",
                    "appStoreVersionPhasedRelease",
                    "appStoreVersionSubmission",
                    "build",
                    "routingAppCoverage",
                ]
            ]
        ] = None,
        limit_app_store_version_experiments_v2: typing.Optional[int] = None,
        limit_app_store_version_experiments: typing.Optional[int] = None,
        limit_app_store_version_localizations: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppStoreVersionResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_age_rating_declarations is not None:
            _query["fields[ageRatingDeclarations]"] = encode_param(
                fields_age_rating_declarations, False
            )
        if fields_alternative_distribution_packages is not None:
            _query["fields[alternativeDistributionPackages]"] = encode_param(
                fields_alternative_distribution_packages, False
            )
        if fields_app_clip_default_experiences is not None:
            _query["fields[appClipDefaultExperiences]"] = encode_param(
                fields_app_clip_default_experiences, False
            )
        if fields_app_store_review_details is not None:
            _query["fields[appStoreReviewDetails]"] = encode_param(
                fields_app_store_review_details, False
            )
        if fields_app_store_version_experiments is not None:
            _query["fields[appStoreVersionExperiments]"] = encode_param(
                fields_app_store_version_experiments, False
            )
        if fields_app_store_version_localizations is not None:
            _query["fields[appStoreVersionLocalizations]"] = encode_param(
                fields_app_store_version_localizations, False
            )
        if fields_app_store_version_phased_releases is not None:
            _query["fields[appStoreVersionPhasedReleases]"] = encode_param(
                fields_app_store_version_phased_releases, False
            )
        if fields_app_store_version_submissions is not None:
            _query["fields[appStoreVersionSubmissions]"] = encode_param(
                fields_app_store_version_submissions, False
            )
        if fields_app_store_versions is not None:
            _query["fields[appStoreVersions]"] = encode_param(
                fields_app_store_versions, False
            )
        if fields_apps is not None:
            _query["fields[apps]"] = encode_param(fields_apps, False)
        if fields_builds is not None:
            _query["fields[builds]"] = encode_param(fields_builds, False)
        if fields_routing_app_coverages is not None:
            _query["fields[routingAppCoverages]"] = encode_param(
                fields_routing_app_coverages, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit_app_store_version_experiments_v2 is not None:
            _query["limit[appStoreVersionExperimentsV2]"] = encode_param(
                limit_app_store_version_experiments_v2, False
            )
        if limit_app_store_version_experiments is not None:
            _query["limit[appStoreVersionExperiments]"] = encode_param(
                limit_app_store_version_experiments, False
            )
        if limit_app_store_version_localizations is not None:
            _query["limit[appStoreVersionLocalizations]"] = encode_param(
                limit_app_store_version_localizations, False
            )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/gameCenterAppVersions/{id}/appStoreVersion",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppStoreVersionResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncAppStoreVersionClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        id: str,
        fields_age_rating_declarations: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "ageRatingOverride",
                    "alcoholTobaccoOrDrugUseOrReferences",
                    "contests",
                    "gambling",
                    "gamblingAndContests",
                    "gamblingSimulated",
                    "horrorOrFearThemes",
                    "kidsAgeBand",
                    "matureOrSuggestiveThemes",
                    "medicalOrTreatmentInformation",
                    "profanityOrCrudeHumor",
                    "seventeenPlus",
                    "sexualContentGraphicAndNudity",
                    "sexualContentOrNudity",
                    "unrestrictedWebAccess",
                    "violenceCartoonOrFantasy",
                    "violenceRealistic",
                    "violenceRealisticProlongedGraphicOrSadistic",
                ]
            ]
        ] = None,
        fields_alternative_distribution_packages: typing.Optional[
            typing.List[typing_extensions.Literal["appStoreVersion", "versions"]]
        ] = None,
        fields_app_clip_default_experiences: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "action",
                    "appClip",
                    "appClipAppStoreReviewDetail",
                    "appClipDefaultExperienceLocalizations",
                    "appClipDefaultExperienceTemplate",
                    "releaseWithAppStoreVersion",
                ]
            ]
        ] = None,
        fields_app_store_review_details: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appStoreReviewAttachments",
                    "appStoreVersion",
                    "contactEmail",
                    "contactFirstName",
                    "contactLastName",
                    "contactPhone",
                    "demoAccountName",
                    "demoAccountPassword",
                    "demoAccountRequired",
                    "notes",
                ]
            ]
        ] = None,
        fields_app_store_version_experiments: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
                    "appStoreVersion",
                    "appStoreVersionExperimentTreatments",
                    "controlVersions",
                    "endDate",
                    "latestControlVersion",
                    "name",
                    "platform",
                    "reviewRequired",
                    "startDate",
                    "started",
                    "state",
                    "trafficProportion",
                ]
            ]
        ] = None,
        fields_app_store_version_localizations: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appPreviewSets",
                    "appScreenshotSets",
                    "appStoreVersion",
                    "description",
                    "keywords",
                    "locale",
                    "marketingUrl",
                    "promotionalText",
                    "supportUrl",
                    "whatsNew",
                ]
            ]
        ] = None,
        fields_app_store_version_phased_releases: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appStoreVersion",
                    "currentDayNumber",
                    "phasedReleaseState",
                    "startDate",
                    "totalPauseDuration",
                ]
            ]
        ] = None,
        fields_app_store_version_submissions: typing.Optional[
            typing.List[typing_extensions.Literal["appStoreVersion"]]
        ] = None,
        fields_app_store_versions: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "ageRatingDeclaration",
                    "alternativeDistributionPackage",
                    "app",
                    "appClipDefaultExperience",
                    "appStoreReviewDetail",
                    "appStoreState",
                    "appStoreVersionExperiments",
                    "appStoreVersionExperimentsV2",
                    "appStoreVersionLocalizations",
                    "appStoreVersionPhasedRelease",
                    "appStoreVersionSubmission",
                    "appVersionState",
                    "build",
                    "copyright",
                    "createdDate",
                    "customerReviews",
                    "downloadable",
                    "earliestReleaseDate",
                    "platform",
                    "releaseType",
                    "reviewType",
                    "routingAppCoverage",
                    "versionString",
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
        fields_routing_app_coverages: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appStoreVersion",
                    "assetDeliveryState",
                    "fileName",
                    "fileSize",
                    "sourceFileChecksum",
                    "uploadOperations",
                    "uploaded",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "ageRatingDeclaration",
                    "alternativeDistributionPackage",
                    "app",
                    "appClipDefaultExperience",
                    "appStoreReviewDetail",
                    "appStoreVersionExperiments",
                    "appStoreVersionExperimentsV2",
                    "appStoreVersionLocalizations",
                    "appStoreVersionPhasedRelease",
                    "appStoreVersionSubmission",
                    "build",
                    "routingAppCoverage",
                ]
            ]
        ] = None,
        limit_app_store_version_experiments_v2: typing.Optional[int] = None,
        limit_app_store_version_experiments: typing.Optional[int] = None,
        limit_app_store_version_localizations: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppStoreVersionResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_age_rating_declarations is not None:
            _query["fields[ageRatingDeclarations]"] = encode_param(
                fields_age_rating_declarations, False
            )
        if fields_alternative_distribution_packages is not None:
            _query["fields[alternativeDistributionPackages]"] = encode_param(
                fields_alternative_distribution_packages, False
            )
        if fields_app_clip_default_experiences is not None:
            _query["fields[appClipDefaultExperiences]"] = encode_param(
                fields_app_clip_default_experiences, False
            )
        if fields_app_store_review_details is not None:
            _query["fields[appStoreReviewDetails]"] = encode_param(
                fields_app_store_review_details, False
            )
        if fields_app_store_version_experiments is not None:
            _query["fields[appStoreVersionExperiments]"] = encode_param(
                fields_app_store_version_experiments, False
            )
        if fields_app_store_version_localizations is not None:
            _query["fields[appStoreVersionLocalizations]"] = encode_param(
                fields_app_store_version_localizations, False
            )
        if fields_app_store_version_phased_releases is not None:
            _query["fields[appStoreVersionPhasedReleases]"] = encode_param(
                fields_app_store_version_phased_releases, False
            )
        if fields_app_store_version_submissions is not None:
            _query["fields[appStoreVersionSubmissions]"] = encode_param(
                fields_app_store_version_submissions, False
            )
        if fields_app_store_versions is not None:
            _query["fields[appStoreVersions]"] = encode_param(
                fields_app_store_versions, False
            )
        if fields_apps is not None:
            _query["fields[apps]"] = encode_param(fields_apps, False)
        if fields_builds is not None:
            _query["fields[builds]"] = encode_param(fields_builds, False)
        if fields_routing_app_coverages is not None:
            _query["fields[routingAppCoverages]"] = encode_param(
                fields_routing_app_coverages, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit_app_store_version_experiments_v2 is not None:
            _query["limit[appStoreVersionExperimentsV2]"] = encode_param(
                limit_app_store_version_experiments_v2, False
            )
        if limit_app_store_version_experiments is not None:
            _query["limit[appStoreVersionExperiments]"] = encode_param(
                limit_app_store_version_experiments, False
            )
        if limit_app_store_version_localizations is not None:
            _query["limit[appStoreVersionLocalizations]"] = encode_param(
                limit_app_store_version_localizations, False
            )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/gameCenterAppVersions/{id}/appStoreVersion",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppStoreVersionResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
