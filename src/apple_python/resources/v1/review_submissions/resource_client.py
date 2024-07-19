"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    QueryParams,
    AsyncBaseClient,
    default_request_options,
    SyncBaseClient,
    to_encodable,
    encode_param,
    RequestOptions,
)
from apple_python.resources.v1.review_submissions.items import (
    ItemsClient,
    AsyncItemsClient,
)
import typing
import typing_extensions
from apple_python.types.v1.review_submissions import models, params


class ReviewSubmissionsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.items = ItemsClient(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.ReviewSubmissionCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReviewSubmissionResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerReviewSubmissionCreateRequest
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/v1/reviewSubmissions",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.ReviewSubmissionResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def patch(
        self,
        *,
        data: params.ReviewSubmissionUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReviewSubmissionResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerReviewSubmissionUpdateRequest
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="PATCH",
            path=f"/v1/reviewSubmissions/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.ReviewSubmissionResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def get(
        self,
        *,
        id: str,
        fields_review_submission_items: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appCustomProductPageVersion",
                    "appEvent",
                    "appStoreVersion",
                    "appStoreVersionExperiment",
                    "appStoreVersionExperimentV2",
                    "removed",
                    "resolved",
                    "reviewSubmission",
                    "state",
                ]
            ]
        ] = None,
        fields_review_submissions: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
                    "appStoreVersionForReview",
                    "canceled",
                    "items",
                    "lastUpdatedByActor",
                    "platform",
                    "state",
                    "submitted",
                    "submittedByActor",
                    "submittedDate",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
                    "appStoreVersionForReview",
                    "items",
                    "lastUpdatedByActor",
                    "submittedByActor",
                ]
            ]
        ] = None,
        limit_items: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReviewSubmissionResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_review_submission_items is not None:
            _query["fields[reviewSubmissionItems]"] = encode_param(
                fields_review_submission_items, False
            )
        if fields_review_submissions is not None:
            _query["fields[reviewSubmissions]"] = encode_param(
                fields_review_submissions, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit_items is not None:
            _query["limit[items]"] = encode_param(limit_items, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/reviewSubmissions/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.ReviewSubmissionResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def list(
        self,
        *,
        filter_app: typing.List[str],
        fields_review_submission_items: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appCustomProductPageVersion",
                    "appEvent",
                    "appStoreVersion",
                    "appStoreVersionExperiment",
                    "appStoreVersionExperimentV2",
                    "removed",
                    "resolved",
                    "reviewSubmission",
                    "state",
                ]
            ]
        ] = None,
        fields_review_submissions: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
                    "appStoreVersionForReview",
                    "canceled",
                    "items",
                    "lastUpdatedByActor",
                    "platform",
                    "state",
                    "submitted",
                    "submittedByActor",
                    "submittedDate",
                ]
            ]
        ] = None,
        filter_platform: typing.Optional[
            typing.List[
                typing_extensions.Literal["IOS", "MAC_OS", "TV_OS", "VISION_OS"]
            ]
        ] = None,
        filter_state: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "READY_FOR_REVIEW",
                    "WAITING_FOR_REVIEW",
                    "IN_REVIEW",
                    "UNRESOLVED_ISSUES",
                    "CANCELING",
                    "COMPLETING",
                    "COMPLETE",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
                    "appStoreVersionForReview",
                    "items",
                    "lastUpdatedByActor",
                    "submittedByActor",
                ]
            ]
        ] = None,
        limit: typing.Optional[int] = None,
        limit_items: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReviewSubmissionsResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        _query["filter[app]"] = encode_param(filter_app, False)
        if fields_review_submission_items is not None:
            _query["fields[reviewSubmissionItems]"] = encode_param(
                fields_review_submission_items, False
            )
        if fields_review_submissions is not None:
            _query["fields[reviewSubmissions]"] = encode_param(
                fields_review_submissions, False
            )
        if filter_platform is not None:
            _query["filter[platform]"] = encode_param(filter_platform, False)
        if filter_state is not None:
            _query["filter[state]"] = encode_param(filter_state, False)
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        if limit_items is not None:
            _query["limit[items]"] = encode_param(limit_items, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path="/v1/reviewSubmissions",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.ReviewSubmissionsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncReviewSubmissionsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.items = AsyncItemsClient(base_client=self._base_client)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.ReviewSubmissionCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReviewSubmissionResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerReviewSubmissionCreateRequest
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/v1/reviewSubmissions",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.ReviewSubmissionResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def patch(
        self,
        *,
        data: params.ReviewSubmissionUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReviewSubmissionResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerReviewSubmissionUpdateRequest
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="PATCH",
            path=f"/v1/reviewSubmissions/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.ReviewSubmissionResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def get(
        self,
        *,
        id: str,
        fields_review_submission_items: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appCustomProductPageVersion",
                    "appEvent",
                    "appStoreVersion",
                    "appStoreVersionExperiment",
                    "appStoreVersionExperimentV2",
                    "removed",
                    "resolved",
                    "reviewSubmission",
                    "state",
                ]
            ]
        ] = None,
        fields_review_submissions: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
                    "appStoreVersionForReview",
                    "canceled",
                    "items",
                    "lastUpdatedByActor",
                    "platform",
                    "state",
                    "submitted",
                    "submittedByActor",
                    "submittedDate",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
                    "appStoreVersionForReview",
                    "items",
                    "lastUpdatedByActor",
                    "submittedByActor",
                ]
            ]
        ] = None,
        limit_items: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReviewSubmissionResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_review_submission_items is not None:
            _query["fields[reviewSubmissionItems]"] = encode_param(
                fields_review_submission_items, False
            )
        if fields_review_submissions is not None:
            _query["fields[reviewSubmissions]"] = encode_param(
                fields_review_submissions, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit_items is not None:
            _query["limit[items]"] = encode_param(limit_items, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/reviewSubmissions/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.ReviewSubmissionResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def list(
        self,
        *,
        filter_app: typing.List[str],
        fields_review_submission_items: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appCustomProductPageVersion",
                    "appEvent",
                    "appStoreVersion",
                    "appStoreVersionExperiment",
                    "appStoreVersionExperimentV2",
                    "removed",
                    "resolved",
                    "reviewSubmission",
                    "state",
                ]
            ]
        ] = None,
        fields_review_submissions: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
                    "appStoreVersionForReview",
                    "canceled",
                    "items",
                    "lastUpdatedByActor",
                    "platform",
                    "state",
                    "submitted",
                    "submittedByActor",
                    "submittedDate",
                ]
            ]
        ] = None,
        filter_platform: typing.Optional[
            typing.List[
                typing_extensions.Literal["IOS", "MAC_OS", "TV_OS", "VISION_OS"]
            ]
        ] = None,
        filter_state: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "READY_FOR_REVIEW",
                    "WAITING_FOR_REVIEW",
                    "IN_REVIEW",
                    "UNRESOLVED_ISSUES",
                    "CANCELING",
                    "COMPLETING",
                    "COMPLETE",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
                    "appStoreVersionForReview",
                    "items",
                    "lastUpdatedByActor",
                    "submittedByActor",
                ]
            ]
        ] = None,
        limit: typing.Optional[int] = None,
        limit_items: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReviewSubmissionsResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        _query["filter[app]"] = encode_param(filter_app, False)
        if fields_review_submission_items is not None:
            _query["fields[reviewSubmissionItems]"] = encode_param(
                fields_review_submission_items, False
            )
        if fields_review_submissions is not None:
            _query["fields[reviewSubmissions]"] = encode_param(
                fields_review_submissions, False
            )
        if filter_platform is not None:
            _query["filter[platform]"] = encode_param(filter_platform, False)
        if filter_state is not None:
            _query["filter[state]"] = encode_param(filter_state, False)
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        if limit_items is not None:
            _query["limit[items]"] = encode_param(limit_items, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path="/v1/reviewSubmissions",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.ReviewSubmissionsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
