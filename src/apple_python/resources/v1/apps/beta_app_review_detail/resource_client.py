"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    default_request_options,
    RequestOptions,
    SyncBaseClient,
    encode_param,
    QueryParams,
    AsyncBaseClient,
)
import typing
import typing_extensions
from apple_python.types.v1.apps.beta_app_review_detail import models


class BetaAppReviewDetailClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        id: str,
        fields_beta_app_review_details: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
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
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BetaAppReviewDetailWithoutIncludesResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_beta_app_review_details is not None:
            _query["fields[betaAppReviewDetails]"] = encode_param(
                fields_beta_app_review_details, False
            )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/apps/{id}/betaAppReviewDetail",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.BetaAppReviewDetailWithoutIncludesResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncBetaAppReviewDetailClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        id: str,
        fields_beta_app_review_details: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
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
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BetaAppReviewDetailWithoutIncludesResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_beta_app_review_details is not None:
            _query["fields[betaAppReviewDetails]"] = encode_param(
                fields_beta_app_review_details, False
            )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/apps/{id}/betaAppReviewDetail",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.BetaAppReviewDetailWithoutIncludesResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
