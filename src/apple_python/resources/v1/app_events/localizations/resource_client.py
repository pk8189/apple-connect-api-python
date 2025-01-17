"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    default_request_options,
    AsyncBaseClient,
    SyncBaseClient,
    RequestOptions,
    encode_param,
    QueryParams,
)
import typing
import typing_extensions
from apple_python.types.v1.app_events.localizations import models


class LocalizationsClient:
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
        fields_app_event_screenshots: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appEventAssetType",
                    "appEventLocalization",
                    "assetDeliveryState",
                    "assetToken",
                    "fileName",
                    "fileSize",
                    "imageAsset",
                    "uploadOperations",
                    "uploaded",
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
        fields_app_events: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
                    "archivedTerritorySchedules",
                    "badge",
                    "deepLink",
                    "eventState",
                    "localizations",
                    "primaryLocale",
                    "priority",
                    "purchaseRequirement",
                    "purpose",
                    "referenceName",
                    "territorySchedules",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appEvent", "appEventScreenshots", "appEventVideoClips"
                ]
            ]
        ] = None,
        limit: typing.Optional[int] = None,
        limit_app_event_screenshots: typing.Optional[int] = None,
        limit_app_event_video_clips: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppEventLocalizationsResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_app_event_localizations is not None:
            _query["fields[appEventLocalizations]"] = encode_param(
                fields_app_event_localizations, False
            )
        if fields_app_event_screenshots is not None:
            _query["fields[appEventScreenshots]"] = encode_param(
                fields_app_event_screenshots, False
            )
        if fields_app_event_video_clips is not None:
            _query["fields[appEventVideoClips]"] = encode_param(
                fields_app_event_video_clips, False
            )
        if fields_app_events is not None:
            _query["fields[appEvents]"] = encode_param(fields_app_events, False)
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        if limit_app_event_screenshots is not None:
            _query["limit[appEventScreenshots]"] = encode_param(
                limit_app_event_screenshots, False
            )
        if limit_app_event_video_clips is not None:
            _query["limit[appEventVideoClips]"] = encode_param(
                limit_app_event_video_clips, False
            )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/appEvents/{id}/localizations",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppEventLocalizationsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncLocalizationsClient:
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
        fields_app_event_screenshots: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appEventAssetType",
                    "appEventLocalization",
                    "assetDeliveryState",
                    "assetToken",
                    "fileName",
                    "fileSize",
                    "imageAsset",
                    "uploadOperations",
                    "uploaded",
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
        fields_app_events: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
                    "archivedTerritorySchedules",
                    "badge",
                    "deepLink",
                    "eventState",
                    "localizations",
                    "primaryLocale",
                    "priority",
                    "purchaseRequirement",
                    "purpose",
                    "referenceName",
                    "territorySchedules",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appEvent", "appEventScreenshots", "appEventVideoClips"
                ]
            ]
        ] = None,
        limit: typing.Optional[int] = None,
        limit_app_event_screenshots: typing.Optional[int] = None,
        limit_app_event_video_clips: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppEventLocalizationsResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_app_event_localizations is not None:
            _query["fields[appEventLocalizations]"] = encode_param(
                fields_app_event_localizations, False
            )
        if fields_app_event_screenshots is not None:
            _query["fields[appEventScreenshots]"] = encode_param(
                fields_app_event_screenshots, False
            )
        if fields_app_event_video_clips is not None:
            _query["fields[appEventVideoClips]"] = encode_param(
                fields_app_event_video_clips, False
            )
        if fields_app_events is not None:
            _query["fields[appEvents]"] = encode_param(fields_app_events, False)
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        if limit_app_event_screenshots is not None:
            _query["limit[appEventScreenshots]"] = encode_param(
                limit_app_event_screenshots, False
            )
        if limit_app_event_video_clips is not None:
            _query["limit[appEventVideoClips]"] = encode_param(
                limit_app_event_video_clips, False
            )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/appEvents/{id}/localizations",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppEventLocalizationsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
