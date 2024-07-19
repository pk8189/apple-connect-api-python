"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    RequestOptions,
    to_encodable,
    SyncBaseClient,
    AsyncBaseClient,
    default_request_options,
)
from apple_python.types.v1.in_app_purchase_submissions import params, models
import typing


class InAppPurchaseSubmissionsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.InAppPurchaseSubmissionCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.InAppPurchaseSubmissionResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerInAppPurchaseSubmissionCreateRequest
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/v1/inAppPurchaseSubmissions",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.InAppPurchaseSubmissionResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncInAppPurchaseSubmissionsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.InAppPurchaseSubmissionCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.InAppPurchaseSubmissionResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerInAppPurchaseSubmissionCreateRequest
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/v1/inAppPurchaseSubmissions",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.InAppPurchaseSubmissionResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)