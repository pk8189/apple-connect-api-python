"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    RequestOptions,
    QueryParams,
    default_request_options,
    AsyncBaseClient,
    SyncBaseClient,
    encode_param,
)
import typing
import typing_extensions
from apple_python.types.v1.game_center_matchmaking_rule_sets.rules import models


class RulesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        id: str,
        fields_game_center_matchmaking_rules: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "description",
                    "expression",
                    "referenceName",
                    "ruleSet",
                    "type",
                    "weight",
                ]
            ]
        ] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterMatchmakingRulesResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_game_center_matchmaking_rules is not None:
            _query["fields[gameCenterMatchmakingRules]"] = encode_param(
                fields_game_center_matchmaking_rules, False
            )
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/gameCenterMatchmakingRuleSets/{id}/rules",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.GameCenterMatchmakingRulesResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncRulesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        id: str,
        fields_game_center_matchmaking_rules: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "description",
                    "expression",
                    "referenceName",
                    "ruleSet",
                    "type",
                    "weight",
                ]
            ]
        ] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterMatchmakingRulesResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_game_center_matchmaking_rules is not None:
            _query["fields[gameCenterMatchmakingRules]"] = encode_param(
                fields_game_center_matchmaking_rules, False
            )
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/gameCenterMatchmakingRuleSets/{id}/rules",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.GameCenterMatchmakingRulesResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)