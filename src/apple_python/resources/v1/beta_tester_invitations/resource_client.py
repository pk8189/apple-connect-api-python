"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    default_request_options,
    RequestOptions,
    SyncBaseClient,
    to_encodable,
    AsyncBaseClient,
)
from apple_python.types.v1.beta_tester_invitations import models, params
import typing


class BetaTesterInvitationsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.BetaTesterInvitationCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BetaTesterInvitationResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerBetaTesterInvitationCreateRequest
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/v1/betaTesterInvitations",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.BetaTesterInvitationResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncBetaTesterInvitationsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.BetaTesterInvitationCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BetaTesterInvitationResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerBetaTesterInvitationCreateRequest
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/v1/betaTesterInvitations",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.BetaTesterInvitationResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
