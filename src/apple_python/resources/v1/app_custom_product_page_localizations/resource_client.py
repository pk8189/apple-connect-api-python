"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    AsyncBaseClient,
    RequestOptions,
    to_encodable,
    SyncBaseClient,
    default_request_options,
    QueryParams,
    encode_param,
)
from apple_python.resources.v1.app_custom_product_page_localizations.app_preview_sets import (
    AppPreviewSetsClient,
    AsyncAppPreviewSetsClient,
)
from apple_python.resources.v1.app_custom_product_page_localizations.app_screenshot_sets import (
    AppScreenshotSetsClient,
    AsyncAppScreenshotSetsClient,
)
import typing
import typing_extensions
from apple_python.types.v1.app_custom_product_page_localizations import params, models


class AppCustomProductPageLocalizationsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.app_preview_sets = AppPreviewSetsClient(base_client=self._base_client)
        self.app_screenshot_sets = AppScreenshotSetsClient(
            base_client=self._base_client
        )

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.AppCustomProductPageLocalizationCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppCustomProductPageLocalizationResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerAppCustomProductPageLocalizationCreateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/v1/appCustomProductPageLocalizations",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.AppCustomProductPageLocalizationResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def patch(
        self,
        *,
        data: params.AppCustomProductPageLocalizationUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppCustomProductPageLocalizationResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerAppCustomProductPageLocalizationUpdateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="PATCH",
            path=f"/v1/appCustomProductPageLocalizations/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.AppCustomProductPageLocalizationResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def get(
        self,
        *,
        id: str,
        fields_app_custom_product_page_localizations: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appCustomProductPageVersion",
                    "appPreviewSets",
                    "appScreenshotSets",
                    "locale",
                    "promotionalText",
                ]
            ]
        ] = None,
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
        fields_app_screenshot_sets: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appCustomProductPageLocalization",
                    "appScreenshots",
                    "appStoreVersionExperimentTreatmentLocalization",
                    "appStoreVersionLocalization",
                    "screenshotDisplayType",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appCustomProductPageVersion", "appPreviewSets", "appScreenshotSets"
                ]
            ]
        ] = None,
        limit_app_preview_sets: typing.Optional[int] = None,
        limit_app_screenshot_sets: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppCustomProductPageLocalizationResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_app_custom_product_page_localizations is not None:
            _query["fields[appCustomProductPageLocalizations]"] = encode_param(
                fields_app_custom_product_page_localizations, False
            )
        if fields_app_preview_sets is not None:
            _query["fields[appPreviewSets]"] = encode_param(
                fields_app_preview_sets, False
            )
        if fields_app_screenshot_sets is not None:
            _query["fields[appScreenshotSets]"] = encode_param(
                fields_app_screenshot_sets, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit_app_preview_sets is not None:
            _query["limit[appPreviewSets]"] = encode_param(
                limit_app_preview_sets, False
            )
        if limit_app_screenshot_sets is not None:
            _query["limit[appScreenshotSets]"] = encode_param(
                limit_app_screenshot_sets, False
            )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/appCustomProductPageLocalizations/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppCustomProductPageLocalizationResponse,
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
            path=f"/v1/appCustomProductPageLocalizations/{id}",
            auth_names=["itc-bearer-token"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncAppCustomProductPageLocalizationsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.app_preview_sets = AsyncAppPreviewSetsClient(base_client=self._base_client)
        self.app_screenshot_sets = AsyncAppScreenshotSetsClient(
            base_client=self._base_client
        )

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.AppCustomProductPageLocalizationCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppCustomProductPageLocalizationResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerAppCustomProductPageLocalizationCreateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/v1/appCustomProductPageLocalizations",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.AppCustomProductPageLocalizationResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def patch(
        self,
        *,
        data: params.AppCustomProductPageLocalizationUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppCustomProductPageLocalizationResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerAppCustomProductPageLocalizationUpdateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="PATCH",
            path=f"/v1/appCustomProductPageLocalizations/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.AppCustomProductPageLocalizationResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def get(
        self,
        *,
        id: str,
        fields_app_custom_product_page_localizations: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appCustomProductPageVersion",
                    "appPreviewSets",
                    "appScreenshotSets",
                    "locale",
                    "promotionalText",
                ]
            ]
        ] = None,
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
        fields_app_screenshot_sets: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appCustomProductPageLocalization",
                    "appScreenshots",
                    "appStoreVersionExperimentTreatmentLocalization",
                    "appStoreVersionLocalization",
                    "screenshotDisplayType",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appCustomProductPageVersion", "appPreviewSets", "appScreenshotSets"
                ]
            ]
        ] = None,
        limit_app_preview_sets: typing.Optional[int] = None,
        limit_app_screenshot_sets: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppCustomProductPageLocalizationResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_app_custom_product_page_localizations is not None:
            _query["fields[appCustomProductPageLocalizations]"] = encode_param(
                fields_app_custom_product_page_localizations, False
            )
        if fields_app_preview_sets is not None:
            _query["fields[appPreviewSets]"] = encode_param(
                fields_app_preview_sets, False
            )
        if fields_app_screenshot_sets is not None:
            _query["fields[appScreenshotSets]"] = encode_param(
                fields_app_screenshot_sets, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit_app_preview_sets is not None:
            _query["limit[appPreviewSets]"] = encode_param(
                limit_app_preview_sets, False
            )
        if limit_app_screenshot_sets is not None:
            _query["limit[appScreenshotSets]"] = encode_param(
                limit_app_screenshot_sets, False
            )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/appCustomProductPageLocalizations/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppCustomProductPageLocalizationResponse,
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
            path=f"/v1/appCustomProductPageLocalizations/{id}",
            auth_names=["itc-bearer-token"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
