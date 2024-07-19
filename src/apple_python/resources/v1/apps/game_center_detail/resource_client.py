"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    AsyncBaseClient,
    SyncBaseClient,
    QueryParams,
    encode_param,
    default_request_options,
    RequestOptions,
)
import typing
import typing_extensions
from apple_python.types.v1.apps.game_center_detail import models


class GameCenterDetailClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        id: str,
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
        fields_game_center_achievement_releases: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "gameCenterAchievement", "gameCenterDetail", "live"
                ]
            ]
        ] = None,
        fields_game_center_achievements: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "archived",
                    "gameCenterDetail",
                    "gameCenterGroup",
                    "groupAchievement",
                    "localizations",
                    "points",
                    "referenceName",
                    "releases",
                    "repeatable",
                    "showBeforeEarned",
                    "vendorIdentifier",
                ]
            ]
        ] = None,
        fields_game_center_app_versions: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appStoreVersion", "compatibilityVersions", "enabled"
                ]
            ]
        ] = None,
        fields_game_center_details: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "achievementReleases",
                    "app",
                    "arcadeEnabled",
                    "challengeEnabled",
                    "defaultGroupLeaderboard",
                    "defaultLeaderboard",
                    "gameCenterAchievements",
                    "gameCenterAppVersions",
                    "gameCenterGroup",
                    "gameCenterLeaderboardSets",
                    "gameCenterLeaderboards",
                    "leaderboardReleases",
                    "leaderboardSetReleases",
                ]
            ]
        ] = None,
        fields_game_center_groups: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "gameCenterAchievements",
                    "gameCenterDetails",
                    "gameCenterLeaderboardSets",
                    "gameCenterLeaderboards",
                    "referenceName",
                ]
            ]
        ] = None,
        fields_game_center_leaderboard_releases: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "gameCenterDetail", "gameCenterLeaderboard", "live"
                ]
            ]
        ] = None,
        fields_game_center_leaderboard_set_releases: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "gameCenterDetail", "gameCenterLeaderboardSet", "live"
                ]
            ]
        ] = None,
        fields_game_center_leaderboard_sets: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "gameCenterDetail",
                    "gameCenterGroup",
                    "gameCenterLeaderboards",
                    "groupLeaderboardSet",
                    "localizations",
                    "referenceName",
                    "releases",
                    "vendorIdentifier",
                ]
            ]
        ] = None,
        fields_game_center_leaderboards: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "archived",
                    "defaultFormatter",
                    "gameCenterDetail",
                    "gameCenterGroup",
                    "gameCenterLeaderboardSets",
                    "groupLeaderboard",
                    "localizations",
                    "recurrenceDuration",
                    "recurrenceRule",
                    "recurrenceStartDate",
                    "referenceName",
                    "releases",
                    "scoreRangeEnd",
                    "scoreRangeStart",
                    "scoreSortType",
                    "submissionType",
                    "vendorIdentifier",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "achievementReleases",
                    "app",
                    "defaultGroupLeaderboard",
                    "defaultLeaderboard",
                    "gameCenterAchievements",
                    "gameCenterAppVersions",
                    "gameCenterGroup",
                    "gameCenterLeaderboardSets",
                    "gameCenterLeaderboards",
                    "leaderboardReleases",
                    "leaderboardSetReleases",
                ]
            ]
        ] = None,
        limit_achievement_releases: typing.Optional[int] = None,
        limit_game_center_achievements: typing.Optional[int] = None,
        limit_game_center_app_versions: typing.Optional[int] = None,
        limit_game_center_leaderboard_sets: typing.Optional[int] = None,
        limit_game_center_leaderboards: typing.Optional[int] = None,
        limit_leaderboard_releases: typing.Optional[int] = None,
        limit_leaderboard_set_releases: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterDetailResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_apps is not None:
            _query["fields[apps]"] = encode_param(fields_apps, False)
        if fields_game_center_achievement_releases is not None:
            _query["fields[gameCenterAchievementReleases]"] = encode_param(
                fields_game_center_achievement_releases, False
            )
        if fields_game_center_achievements is not None:
            _query["fields[gameCenterAchievements]"] = encode_param(
                fields_game_center_achievements, False
            )
        if fields_game_center_app_versions is not None:
            _query["fields[gameCenterAppVersions]"] = encode_param(
                fields_game_center_app_versions, False
            )
        if fields_game_center_details is not None:
            _query["fields[gameCenterDetails]"] = encode_param(
                fields_game_center_details, False
            )
        if fields_game_center_groups is not None:
            _query["fields[gameCenterGroups]"] = encode_param(
                fields_game_center_groups, False
            )
        if fields_game_center_leaderboard_releases is not None:
            _query["fields[gameCenterLeaderboardReleases]"] = encode_param(
                fields_game_center_leaderboard_releases, False
            )
        if fields_game_center_leaderboard_set_releases is not None:
            _query["fields[gameCenterLeaderboardSetReleases]"] = encode_param(
                fields_game_center_leaderboard_set_releases, False
            )
        if fields_game_center_leaderboard_sets is not None:
            _query["fields[gameCenterLeaderboardSets]"] = encode_param(
                fields_game_center_leaderboard_sets, False
            )
        if fields_game_center_leaderboards is not None:
            _query["fields[gameCenterLeaderboards]"] = encode_param(
                fields_game_center_leaderboards, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit_achievement_releases is not None:
            _query["limit[achievementReleases]"] = encode_param(
                limit_achievement_releases, False
            )
        if limit_game_center_achievements is not None:
            _query["limit[gameCenterAchievements]"] = encode_param(
                limit_game_center_achievements, False
            )
        if limit_game_center_app_versions is not None:
            _query["limit[gameCenterAppVersions]"] = encode_param(
                limit_game_center_app_versions, False
            )
        if limit_game_center_leaderboard_sets is not None:
            _query["limit[gameCenterLeaderboardSets]"] = encode_param(
                limit_game_center_leaderboard_sets, False
            )
        if limit_game_center_leaderboards is not None:
            _query["limit[gameCenterLeaderboards]"] = encode_param(
                limit_game_center_leaderboards, False
            )
        if limit_leaderboard_releases is not None:
            _query["limit[leaderboardReleases]"] = encode_param(
                limit_leaderboard_releases, False
            )
        if limit_leaderboard_set_releases is not None:
            _query["limit[leaderboardSetReleases]"] = encode_param(
                limit_leaderboard_set_releases, False
            )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/apps/{id}/gameCenterDetail",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.GameCenterDetailResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncGameCenterDetailClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        id: str,
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
        fields_game_center_achievement_releases: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "gameCenterAchievement", "gameCenterDetail", "live"
                ]
            ]
        ] = None,
        fields_game_center_achievements: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "archived",
                    "gameCenterDetail",
                    "gameCenterGroup",
                    "groupAchievement",
                    "localizations",
                    "points",
                    "referenceName",
                    "releases",
                    "repeatable",
                    "showBeforeEarned",
                    "vendorIdentifier",
                ]
            ]
        ] = None,
        fields_game_center_app_versions: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appStoreVersion", "compatibilityVersions", "enabled"
                ]
            ]
        ] = None,
        fields_game_center_details: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "achievementReleases",
                    "app",
                    "arcadeEnabled",
                    "challengeEnabled",
                    "defaultGroupLeaderboard",
                    "defaultLeaderboard",
                    "gameCenterAchievements",
                    "gameCenterAppVersions",
                    "gameCenterGroup",
                    "gameCenterLeaderboardSets",
                    "gameCenterLeaderboards",
                    "leaderboardReleases",
                    "leaderboardSetReleases",
                ]
            ]
        ] = None,
        fields_game_center_groups: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "gameCenterAchievements",
                    "gameCenterDetails",
                    "gameCenterLeaderboardSets",
                    "gameCenterLeaderboards",
                    "referenceName",
                ]
            ]
        ] = None,
        fields_game_center_leaderboard_releases: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "gameCenterDetail", "gameCenterLeaderboard", "live"
                ]
            ]
        ] = None,
        fields_game_center_leaderboard_set_releases: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "gameCenterDetail", "gameCenterLeaderboardSet", "live"
                ]
            ]
        ] = None,
        fields_game_center_leaderboard_sets: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "gameCenterDetail",
                    "gameCenterGroup",
                    "gameCenterLeaderboards",
                    "groupLeaderboardSet",
                    "localizations",
                    "referenceName",
                    "releases",
                    "vendorIdentifier",
                ]
            ]
        ] = None,
        fields_game_center_leaderboards: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "archived",
                    "defaultFormatter",
                    "gameCenterDetail",
                    "gameCenterGroup",
                    "gameCenterLeaderboardSets",
                    "groupLeaderboard",
                    "localizations",
                    "recurrenceDuration",
                    "recurrenceRule",
                    "recurrenceStartDate",
                    "referenceName",
                    "releases",
                    "scoreRangeEnd",
                    "scoreRangeStart",
                    "scoreSortType",
                    "submissionType",
                    "vendorIdentifier",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "achievementReleases",
                    "app",
                    "defaultGroupLeaderboard",
                    "defaultLeaderboard",
                    "gameCenterAchievements",
                    "gameCenterAppVersions",
                    "gameCenterGroup",
                    "gameCenterLeaderboardSets",
                    "gameCenterLeaderboards",
                    "leaderboardReleases",
                    "leaderboardSetReleases",
                ]
            ]
        ] = None,
        limit_achievement_releases: typing.Optional[int] = None,
        limit_game_center_achievements: typing.Optional[int] = None,
        limit_game_center_app_versions: typing.Optional[int] = None,
        limit_game_center_leaderboard_sets: typing.Optional[int] = None,
        limit_game_center_leaderboards: typing.Optional[int] = None,
        limit_leaderboard_releases: typing.Optional[int] = None,
        limit_leaderboard_set_releases: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterDetailResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_apps is not None:
            _query["fields[apps]"] = encode_param(fields_apps, False)
        if fields_game_center_achievement_releases is not None:
            _query["fields[gameCenterAchievementReleases]"] = encode_param(
                fields_game_center_achievement_releases, False
            )
        if fields_game_center_achievements is not None:
            _query["fields[gameCenterAchievements]"] = encode_param(
                fields_game_center_achievements, False
            )
        if fields_game_center_app_versions is not None:
            _query["fields[gameCenterAppVersions]"] = encode_param(
                fields_game_center_app_versions, False
            )
        if fields_game_center_details is not None:
            _query["fields[gameCenterDetails]"] = encode_param(
                fields_game_center_details, False
            )
        if fields_game_center_groups is not None:
            _query["fields[gameCenterGroups]"] = encode_param(
                fields_game_center_groups, False
            )
        if fields_game_center_leaderboard_releases is not None:
            _query["fields[gameCenterLeaderboardReleases]"] = encode_param(
                fields_game_center_leaderboard_releases, False
            )
        if fields_game_center_leaderboard_set_releases is not None:
            _query["fields[gameCenterLeaderboardSetReleases]"] = encode_param(
                fields_game_center_leaderboard_set_releases, False
            )
        if fields_game_center_leaderboard_sets is not None:
            _query["fields[gameCenterLeaderboardSets]"] = encode_param(
                fields_game_center_leaderboard_sets, False
            )
        if fields_game_center_leaderboards is not None:
            _query["fields[gameCenterLeaderboards]"] = encode_param(
                fields_game_center_leaderboards, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit_achievement_releases is not None:
            _query["limit[achievementReleases]"] = encode_param(
                limit_achievement_releases, False
            )
        if limit_game_center_achievements is not None:
            _query["limit[gameCenterAchievements]"] = encode_param(
                limit_game_center_achievements, False
            )
        if limit_game_center_app_versions is not None:
            _query["limit[gameCenterAppVersions]"] = encode_param(
                limit_game_center_app_versions, False
            )
        if limit_game_center_leaderboard_sets is not None:
            _query["limit[gameCenterLeaderboardSets]"] = encode_param(
                limit_game_center_leaderboard_sets, False
            )
        if limit_game_center_leaderboards is not None:
            _query["limit[gameCenterLeaderboards]"] = encode_param(
                limit_game_center_leaderboards, False
            )
        if limit_leaderboard_releases is not None:
            _query["limit[leaderboardReleases]"] = encode_param(
                limit_leaderboard_releases, False
            )
        if limit_leaderboard_set_releases is not None:
            _query["limit[leaderboardSetReleases]"] = encode_param(
                limit_leaderboard_set_releases, False
            )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/apps/{id}/gameCenterDetail",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.GameCenterDetailResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)