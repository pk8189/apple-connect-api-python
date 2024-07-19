"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    to_encodable,
    AsyncBaseClient,
    QueryParams,
    SyncBaseClient,
    default_request_options,
    RequestOptions,
    encode_param,
)
import typing
import typing_extensions
from apple_python.types.v1.app_clip_advanced_experiences import params, models


class AppClipAdvancedExperiencesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.AppClipAdvancedExperienceCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppClipAdvancedExperienceResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerAppClipAdvancedExperienceCreateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/v1/appClipAdvancedExperiences",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.AppClipAdvancedExperienceResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def patch(
        self,
        *,
        data: params.AppClipAdvancedExperienceUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppClipAdvancedExperienceResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerAppClipAdvancedExperienceUpdateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="PATCH",
            path=f"/v1/appClipAdvancedExperiences/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.AppClipAdvancedExperienceResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def get(
        self,
        *,
        id: str,
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
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal["appClip", "headerImage", "localizations"]
            ]
        ] = None,
        limit_localizations: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppClipAdvancedExperienceResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_app_clip_advanced_experiences is not None:
            _query["fields[appClipAdvancedExperiences]"] = encode_param(
                fields_app_clip_advanced_experiences, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit_localizations is not None:
            _query["limit[localizations]"] = encode_param(limit_localizations, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/appClipAdvancedExperiences/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppClipAdvancedExperienceResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncAppClipAdvancedExperiencesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.AppClipAdvancedExperienceCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppClipAdvancedExperienceResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerAppClipAdvancedExperienceCreateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/v1/appClipAdvancedExperiences",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.AppClipAdvancedExperienceResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def patch(
        self,
        *,
        data: params.AppClipAdvancedExperienceUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppClipAdvancedExperienceResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerAppClipAdvancedExperienceUpdateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="PATCH",
            path=f"/v1/appClipAdvancedExperiences/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.AppClipAdvancedExperienceResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def get(
        self,
        *,
        id: str,
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
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal["appClip", "headerImage", "localizations"]
            ]
        ] = None,
        limit_localizations: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppClipAdvancedExperienceResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_app_clip_advanced_experiences is not None:
            _query["fields[appClipAdvancedExperiences]"] = encode_param(
                fields_app_clip_advanced_experiences, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit_localizations is not None:
            _query["limit[localizations]"] = encode_param(limit_localizations, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/appClipAdvancedExperiences/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppClipAdvancedExperienceResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
