"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    encode_param,
    default_request_options,
    QueryParams,
    RequestOptions,
    AsyncBaseClient,
    SyncBaseClient,
)
import typing
import typing_extensions
from apple_python.types.v1.game_center_leaderboards.releases import models


class ReleasesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        id: str,
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
        fields_game_center_leaderboard_releases: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "gameCenterDetail", "gameCenterLeaderboard", "live"
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
        filter_game_center_detail: typing.Optional[typing.List[str]] = None,
        filter_live: typing.Optional[typing.List[str]] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal["gameCenterDetail", "gameCenterLeaderboard"]
            ]
        ] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterLeaderboardReleasesResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_game_center_details is not None:
            _query["fields[gameCenterDetails]"] = encode_param(
                fields_game_center_details, False
            )
        if fields_game_center_leaderboard_releases is not None:
            _query["fields[gameCenterLeaderboardReleases]"] = encode_param(
                fields_game_center_leaderboard_releases, False
            )
        if fields_game_center_leaderboards is not None:
            _query["fields[gameCenterLeaderboards]"] = encode_param(
                fields_game_center_leaderboards, False
            )
        if filter_game_center_detail is not None:
            _query["filter[gameCenterDetail]"] = encode_param(
                filter_game_center_detail, False
            )
        if filter_live is not None:
            _query["filter[live]"] = encode_param(filter_live, False)
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/gameCenterLeaderboards/{id}/releases",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.GameCenterLeaderboardReleasesResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncReleasesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        id: str,
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
        fields_game_center_leaderboard_releases: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "gameCenterDetail", "gameCenterLeaderboard", "live"
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
        filter_game_center_detail: typing.Optional[typing.List[str]] = None,
        filter_live: typing.Optional[typing.List[str]] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal["gameCenterDetail", "gameCenterLeaderboard"]
            ]
        ] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterLeaderboardReleasesResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_game_center_details is not None:
            _query["fields[gameCenterDetails]"] = encode_param(
                fields_game_center_details, False
            )
        if fields_game_center_leaderboard_releases is not None:
            _query["fields[gameCenterLeaderboardReleases]"] = encode_param(
                fields_game_center_leaderboard_releases, False
            )
        if fields_game_center_leaderboards is not None:
            _query["fields[gameCenterLeaderboards]"] = encode_param(
                fields_game_center_leaderboards, False
            )
        if filter_game_center_detail is not None:
            _query["filter[gameCenterDetail]"] = encode_param(
                filter_game_center_detail, False
            )
        if filter_live is not None:
            _query["filter[live]"] = encode_param(filter_live, False)
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/gameCenterLeaderboards/{id}/releases",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.GameCenterLeaderboardReleasesResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
