"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    encode_param,
    default_request_options,
    SyncBaseClient,
    RequestOptions,
    AsyncBaseClient,
    QueryParams,
)
import typing
import typing_extensions
from apple_python.types.v1.app_event_localizations.app_event_video_clips import models


class AppEventVideoClipsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        id: str,
        fields_app_event_localizations: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appEvent",
                    "appEventScreenshots",
                    "appEventVideoClips",
                    "locale",
                    "longDescription",
                    "name",
                    "shortDescription",
                ]
            ]
        ] = None,
        fields_app_event_video_clips: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appEventAssetType",
                    "appEventLocalization",
                    "assetDeliveryState",
                    "fileName",
                    "fileSize",
                    "previewFrameTimeCode",
                    "previewImage",
                    "uploadOperations",
                    "uploaded",
                    "videoUrl",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[typing_extensions.Literal["appEventLocalization"]]
        ] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppEventVideoClipsResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_app_event_localizations is not None:
            _query["fields[appEventLocalizations]"] = encode_param(
                fields_app_event_localizations, False
            )
        if fields_app_event_video_clips is not None:
            _query["fields[appEventVideoClips]"] = encode_param(
                fields_app_event_video_clips, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/appEventLocalizations/{id}/appEventVideoClips",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppEventVideoClipsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncAppEventVideoClipsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        id: str,
        fields_app_event_localizations: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appEvent",
                    "appEventScreenshots",
                    "appEventVideoClips",
                    "locale",
                    "longDescription",
                    "name",
                    "shortDescription",
                ]
            ]
        ] = None,
        fields_app_event_video_clips: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appEventAssetType",
                    "appEventLocalization",
                    "assetDeliveryState",
                    "fileName",
                    "fileSize",
                    "previewFrameTimeCode",
                    "previewImage",
                    "uploadOperations",
                    "uploaded",
                    "videoUrl",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[typing_extensions.Literal["appEventLocalization"]]
        ] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppEventVideoClipsResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_app_event_localizations is not None:
            _query["fields[appEventLocalizations]"] = encode_param(
                fields_app_event_localizations, False
            )
        if fields_app_event_video_clips is not None:
            _query["fields[appEventVideoClips]"] = encode_param(
                fields_app_event_video_clips, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/appEventLocalizations/{id}/appEventVideoClips",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppEventVideoClipsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
