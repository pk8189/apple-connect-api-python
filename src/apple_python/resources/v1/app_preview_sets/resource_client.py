"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    to_encodable,
    AsyncBaseClient,
    default_request_options,
    SyncBaseClient,
    RequestOptions,
    encode_param,
    QueryParams,
)
from apple_python.resources.v1.app_preview_sets.app_previews import (
    AppPreviewsClient,
    AsyncAppPreviewsClient,
)
from apple_python.resources.v1.app_preview_sets.relationships import (
    RelationshipsClient,
    AsyncRelationshipsClient,
)
import typing
import typing_extensions
from apple_python.types.v1.app_preview_sets import models, params


class AppPreviewSetsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.app_previews = AppPreviewsClient(base_client=self._base_client)
        self.relationships = RelationshipsClient(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.AppPreviewSetCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppPreviewSetResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerAppPreviewSetCreateRequest
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/v1/appPreviewSets",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.AppPreviewSetResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def get(
        self,
        *,
        id: str,
        fields_app_preview_sets: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appCustomProductPageLocalization",
                    "appPreviews",
                    "appStoreVersionExperimentTreatmentLocalization",
                    "appStoreVersionLocalization",
                    "previewType",
                ]
            ]
        ] = None,
        fields_app_previews: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appPreviewSet",
                    "assetDeliveryState",
                    "fileName",
                    "fileSize",
                    "mimeType",
                    "previewFrameTimeCode",
                    "previewImage",
                    "sourceFileChecksum",
                    "uploadOperations",
                    "uploaded",
                    "videoUrl",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appCustomProductPageLocalization",
                    "appPreviews",
                    "appStoreVersionExperimentTreatmentLocalization",
                    "appStoreVersionLocalization",
                ]
            ]
        ] = None,
        limit_app_previews: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppPreviewSetResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_app_preview_sets is not None:
            _query["fields[appPreviewSets]"] = encode_param(
                fields_app_preview_sets, False
            )
        if fields_app_previews is not None:
            _query["fields[appPreviews]"] = encode_param(fields_app_previews, False)
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit_app_previews is not None:
            _query["limit[appPreviews]"] = encode_param(limit_app_previews, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/appPreviewSets/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppPreviewSetResponse,
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
            path=f"/v1/appPreviewSets/{id}",
            auth_names=["itc-bearer-token"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncAppPreviewSetsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.app_previews = AsyncAppPreviewsClient(base_client=self._base_client)
        self.relationships = AsyncRelationshipsClient(base_client=self._base_client)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.AppPreviewSetCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppPreviewSetResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerAppPreviewSetCreateRequest
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/v1/appPreviewSets",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.AppPreviewSetResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def get(
        self,
        *,
        id: str,
        fields_app_preview_sets: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appCustomProductPageLocalization",
                    "appPreviews",
                    "appStoreVersionExperimentTreatmentLocalization",
                    "appStoreVersionLocalization",
                    "previewType",
                ]
            ]
        ] = None,
        fields_app_previews: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appPreviewSet",
                    "assetDeliveryState",
                    "fileName",
                    "fileSize",
                    "mimeType",
                    "previewFrameTimeCode",
                    "previewImage",
                    "sourceFileChecksum",
                    "uploadOperations",
                    "uploaded",
                    "videoUrl",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appCustomProductPageLocalization",
                    "appPreviews",
                    "appStoreVersionExperimentTreatmentLocalization",
                    "appStoreVersionLocalization",
                ]
            ]
        ] = None,
        limit_app_previews: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppPreviewSetResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_app_preview_sets is not None:
            _query["fields[appPreviewSets]"] = encode_param(
                fields_app_preview_sets, False
            )
        if fields_app_previews is not None:
            _query["fields[appPreviews]"] = encode_param(fields_app_previews, False)
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit_app_previews is not None:
            _query["limit[appPreviews]"] = encode_param(limit_app_previews, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/appPreviewSets/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppPreviewSetResponse,
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
            path=f"/v1/appPreviewSets/{id}",
            auth_names=["itc-bearer-token"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
