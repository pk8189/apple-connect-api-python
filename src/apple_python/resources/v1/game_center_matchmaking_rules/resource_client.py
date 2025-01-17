"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    SyncBaseClient,
    default_request_options,
    AsyncBaseClient,
    RequestOptions,
    to_encodable,
)
from apple_python.resources.v1.game_center_matchmaking_rules.metrics import (
    AsyncMetricsClient,
    MetricsClient,
)
import typing
from apple_python.types.v1.game_center_matchmaking_rules import models, params


class GameCenterMatchmakingRulesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.metrics = MetricsClient(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.GameCenterMatchmakingRuleCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterMatchmakingRuleResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerGameCenterMatchmakingRuleCreateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/v1/gameCenterMatchmakingRules",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.GameCenterMatchmakingRuleResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def patch(
        self,
        *,
        data: params.GameCenterMatchmakingRuleUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterMatchmakingRuleResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerGameCenterMatchmakingRuleUpdateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="PATCH",
            path=f"/v1/gameCenterMatchmakingRules/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.GameCenterMatchmakingRuleResponse,
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
            path=f"/v1/gameCenterMatchmakingRules/{id}",
            auth_names=["itc-bearer-token"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncGameCenterMatchmakingRulesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.metrics = AsyncMetricsClient(base_client=self._base_client)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.GameCenterMatchmakingRuleCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterMatchmakingRuleResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerGameCenterMatchmakingRuleCreateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/v1/gameCenterMatchmakingRules",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.GameCenterMatchmakingRuleResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def patch(
        self,
        *,
        data: params.GameCenterMatchmakingRuleUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterMatchmakingRuleResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerGameCenterMatchmakingRuleUpdateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="PATCH",
            path=f"/v1/gameCenterMatchmakingRules/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.GameCenterMatchmakingRuleResponse,
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
            path=f"/v1/gameCenterMatchmakingRules/{id}",
            auth_names=["itc-bearer-token"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
