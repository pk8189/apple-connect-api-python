"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    default_request_options,
    SyncBaseClient,
    encode_param,
    AsyncBaseClient,
    RequestOptions,
    to_encodable,
    QueryParams,
)
import typing
import typing_extensions
from apple_python.types.v1.customer_review_responses import models, params


class CustomerReviewResponsesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.CustomerReviewResponseV1CreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CustomerReviewResponseV1Response:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerCustomerReviewResponseV1CreateRequest
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/v1/customerReviewResponses",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.CustomerReviewResponseV1Response,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def get(
        self,
        *,
        id: str,
        fields_customer_review_responses: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "lastModifiedDate", "responseBody", "review", "state"
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[typing_extensions.Literal["review"]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CustomerReviewResponseV1Response:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_customer_review_responses is not None:
            _query["fields[customerReviewResponses]"] = encode_param(
                fields_customer_review_responses, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/customerReviewResponses/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.CustomerReviewResponseV1Response,
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
            path=f"/v1/customerReviewResponses/{id}",
            auth_names=["itc-bearer-token"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncCustomerReviewResponsesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.CustomerReviewResponseV1CreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CustomerReviewResponseV1Response:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerCustomerReviewResponseV1CreateRequest
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/v1/customerReviewResponses",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.CustomerReviewResponseV1Response,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def get(
        self,
        *,
        id: str,
        fields_customer_review_responses: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "lastModifiedDate", "responseBody", "review", "state"
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[typing_extensions.Literal["review"]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CustomerReviewResponseV1Response:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_customer_review_responses is not None:
            _query["fields[customerReviewResponses]"] = encode_param(
                fields_customer_review_responses, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/customerReviewResponses/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.CustomerReviewResponseV1Response,
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
            path=f"/v1/customerReviewResponses/{id}",
            auth_names=["itc-bearer-token"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
