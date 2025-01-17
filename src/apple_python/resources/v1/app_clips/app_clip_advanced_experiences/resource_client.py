"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    encode_param,
    RequestOptions,
    QueryParams,
    default_request_options,
    SyncBaseClient,
    AsyncBaseClient,
)
import typing
import typing_extensions
from apple_python.types.v1.app_clips.app_clip_advanced_experiences import models


class AppClipAdvancedExperiencesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        id: str,
        fields_app_clip_advanced_experience_images: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "assetDeliveryState",
                    "fileName",
                    "fileSize",
                    "imageAsset",
                    "sourceFileChecksum",
                    "uploadOperations",
                    "uploaded",
                ]
            ]
        ] = None,
        fields_app_clip_advanced_experience_localizations: typing.Optional[
            typing.List[typing_extensions.Literal["language", "subtitle", "title"]]
        ] = None,
        fields_app_clip_advanced_experiences: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "action",
                    "appClip",
                    "businessCategory",
                    "defaultLanguage",
                    "headerImage",
                    "isPoweredBy",
                    "link",
                    "localizations",
                    "place",
                    "placeStatus",
                    "removed",
                    "status",
                    "version",
                ]
            ]
        ] = None,
        fields_app_clips: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
                    "appClipAdvancedExperiences",
                    "appClipDefaultExperiences",
                    "bundleId",
                ]
            ]
        ] = None,
        filter_action: typing.Optional[
            typing.List[typing_extensions.Literal["OPEN", "VIEW", "PLAY"]]
        ] = None,
        filter_place_status: typing.Optional[
            typing.List[typing_extensions.Literal["PENDING", "MATCHED", "NO_MATCH"]]
        ] = None,
        filter_status: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "RECEIVED", "DEACTIVATED", "APP_TRANSFER_IN_PROGRESS"
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal["appClip", "headerImage", "localizations"]
            ]
        ] = None,
        limit: typing.Optional[int] = None,
        limit_localizations: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppClipAdvancedExperiencesResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_app_clip_advanced_experience_images is not None:
            _query["fields[appClipAdvancedExperienceImages]"] = encode_param(
                fields_app_clip_advanced_experience_images, False
            )
        if fields_app_clip_advanced_experience_localizations is not None:
            _query["fields[appClipAdvancedExperienceLocalizations]"] = encode_param(
                fields_app_clip_advanced_experience_localizations, False
            )
        if fields_app_clip_advanced_experiences is not None:
            _query["fields[appClipAdvancedExperiences]"] = encode_param(
                fields_app_clip_advanced_experiences, False
            )
        if fields_app_clips is not None:
            _query["fields[appClips]"] = encode_param(fields_app_clips, False)
        if filter_action is not None:
            _query["filter[action]"] = encode_param(filter_action, False)
        if filter_place_status is not None:
            _query["filter[placeStatus]"] = encode_param(filter_place_status, False)
        if filter_status is not None:
            _query["filter[status]"] = encode_param(filter_status, False)
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        if limit_localizations is not None:
            _query["limit[localizations]"] = encode_param(limit_localizations, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/appClips/{id}/appClipAdvancedExperiences",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppClipAdvancedExperiencesResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncAppClipAdvancedExperiencesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        id: str,
        fields_app_clip_advanced_experience_images: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "assetDeliveryState",
                    "fileName",
                    "fileSize",
                    "imageAsset",
                    "sourceFileChecksum",
                    "uploadOperations",
                    "uploaded",
                ]
            ]
        ] = None,
        fields_app_clip_advanced_experience_localizations: typing.Optional[
            typing.List[typing_extensions.Literal["language", "subtitle", "title"]]
        ] = None,
        fields_app_clip_advanced_experiences: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "action",
                    "appClip",
                    "businessCategory",
                    "defaultLanguage",
                    "headerImage",
                    "isPoweredBy",
                    "link",
                    "localizations",
                    "place",
                    "placeStatus",
                    "removed",
                    "status",
                    "version",
                ]
            ]
        ] = None,
        fields_app_clips: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
                    "appClipAdvancedExperiences",
                    "appClipDefaultExperiences",
                    "bundleId",
                ]
            ]
        ] = None,
        filter_action: typing.Optional[
            typing.List[typing_extensions.Literal["OPEN", "VIEW", "PLAY"]]
        ] = None,
        filter_place_status: typing.Optional[
            typing.List[typing_extensions.Literal["PENDING", "MATCHED", "NO_MATCH"]]
        ] = None,
        filter_status: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "RECEIVED", "DEACTIVATED", "APP_TRANSFER_IN_PROGRESS"
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal["appClip", "headerImage", "localizations"]
            ]
        ] = None,
        limit: typing.Optional[int] = None,
        limit_localizations: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppClipAdvancedExperiencesResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_app_clip_advanced_experience_images is not None:
            _query["fields[appClipAdvancedExperienceImages]"] = encode_param(
                fields_app_clip_advanced_experience_images, False
            )
        if fields_app_clip_advanced_experience_localizations is not None:
            _query["fields[appClipAdvancedExperienceLocalizations]"] = encode_param(
                fields_app_clip_advanced_experience_localizations, False
            )
        if fields_app_clip_advanced_experiences is not None:
            _query["fields[appClipAdvancedExperiences]"] = encode_param(
                fields_app_clip_advanced_experiences, False
            )
        if fields_app_clips is not None:
            _query["fields[appClips]"] = encode_param(fields_app_clips, False)
        if filter_action is not None:
            _query["filter[action]"] = encode_param(filter_action, False)
        if filter_place_status is not None:
            _query["filter[placeStatus]"] = encode_param(filter_place_status, False)
        if filter_status is not None:
            _query["filter[status]"] = encode_param(filter_status, False)
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        if limit_localizations is not None:
            _query["limit[localizations]"] = encode_param(limit_localizations, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/appClips/{id}/appClipAdvancedExperiences",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppClipAdvancedExperiencesResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
