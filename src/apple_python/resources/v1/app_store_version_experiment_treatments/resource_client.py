"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    SyncBaseClient,
    encode_param,
    to_encodable,
    default_request_options,
    AsyncBaseClient,
    RequestOptions,
    QueryParams,
)
from apple_python.resources.v1.app_store_version_experiment_treatments.app_store_version_experiment_treatment_localizations import (
    AppStoreVersionExperimentTreatmentLocalizationsClient,
    AsyncAppStoreVersionExperimentTreatmentLocalizationsClient,
)
import typing
import typing_extensions
from apple_python.types.v1.app_store_version_experiment_treatments import models, params


class AppStoreVersionExperimentTreatmentsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.app_store_version_experiment_treatment_localizations = (
            AppStoreVersionExperimentTreatmentLocalizationsClient(
                base_client=self._base_client
            )
        )

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.AppStoreVersionExperimentTreatmentCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppStoreVersionExperimentTreatmentResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerAppStoreVersionExperimentTreatmentCreateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/v1/appStoreVersionExperimentTreatments",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.AppStoreVersionExperimentTreatmentResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def patch(
        self,
        *,
        data: params.AppStoreVersionExperimentTreatmentUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppStoreVersionExperimentTreatmentResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerAppStoreVersionExperimentTreatmentUpdateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="PATCH",
            path=f"/v1/appStoreVersionExperimentTreatments/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.AppStoreVersionExperimentTreatmentResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def get(
        self,
        *,
        id: str,
        fields_app_store_version_experiment_treatment_localizations: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appPreviewSets",
                    "appScreenshotSets",
                    "appStoreVersionExperimentTreatment",
                    "locale",
                ]
            ]
        ] = None,
        fields_app_store_version_experiment_treatments: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appIcon",
                    "appIconName",
                    "appStoreVersionExperiment",
                    "appStoreVersionExperimentTreatmentLocalizations",
                    "appStoreVersionExperimentV2",
                    "name",
                    "promotedDate",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appStoreVersionExperiment",
                    "appStoreVersionExperimentTreatmentLocalizations",
                    "appStoreVersionExperimentV2",
                ]
            ]
        ] = None,
        limit_app_store_version_experiment_treatment_localizations: typing.Optional[
            int
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppStoreVersionExperimentTreatmentResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_app_store_version_experiment_treatment_localizations is not None:
            _query["fields[appStoreVersionExperimentTreatmentLocalizations]"] = (
                encode_param(
                    fields_app_store_version_experiment_treatment_localizations, False
                )
            )
        if fields_app_store_version_experiment_treatments is not None:
            _query["fields[appStoreVersionExperimentTreatments]"] = encode_param(
                fields_app_store_version_experiment_treatments, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit_app_store_version_experiment_treatment_localizations is not None:
            _query["limit[appStoreVersionExperimentTreatmentLocalizations]"] = (
                encode_param(
                    limit_app_store_version_experiment_treatment_localizations, False
                )
            )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/appStoreVersionExperimentTreatments/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppStoreVersionExperimentTreatmentResponse,
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
            path=f"/v1/appStoreVersionExperimentTreatments/{id}",
            auth_names=["itc-bearer-token"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncAppStoreVersionExperimentTreatmentsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.app_store_version_experiment_treatment_localizations = (
            AsyncAppStoreVersionExperimentTreatmentLocalizationsClient(
                base_client=self._base_client
            )
        )

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.AppStoreVersionExperimentTreatmentCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppStoreVersionExperimentTreatmentResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerAppStoreVersionExperimentTreatmentCreateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/v1/appStoreVersionExperimentTreatments",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.AppStoreVersionExperimentTreatmentResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def patch(
        self,
        *,
        data: params.AppStoreVersionExperimentTreatmentUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppStoreVersionExperimentTreatmentResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerAppStoreVersionExperimentTreatmentUpdateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="PATCH",
            path=f"/v1/appStoreVersionExperimentTreatments/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.AppStoreVersionExperimentTreatmentResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def get(
        self,
        *,
        id: str,
        fields_app_store_version_experiment_treatment_localizations: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appPreviewSets",
                    "appScreenshotSets",
                    "appStoreVersionExperimentTreatment",
                    "locale",
                ]
            ]
        ] = None,
        fields_app_store_version_experiment_treatments: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appIcon",
                    "appIconName",
                    "appStoreVersionExperiment",
                    "appStoreVersionExperimentTreatmentLocalizations",
                    "appStoreVersionExperimentV2",
                    "name",
                    "promotedDate",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appStoreVersionExperiment",
                    "appStoreVersionExperimentTreatmentLocalizations",
                    "appStoreVersionExperimentV2",
                ]
            ]
        ] = None,
        limit_app_store_version_experiment_treatment_localizations: typing.Optional[
            int
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppStoreVersionExperimentTreatmentResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_app_store_version_experiment_treatment_localizations is not None:
            _query["fields[appStoreVersionExperimentTreatmentLocalizations]"] = (
                encode_param(
                    fields_app_store_version_experiment_treatment_localizations, False
                )
            )
        if fields_app_store_version_experiment_treatments is not None:
            _query["fields[appStoreVersionExperimentTreatments]"] = encode_param(
                fields_app_store_version_experiment_treatments, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit_app_store_version_experiment_treatment_localizations is not None:
            _query["limit[appStoreVersionExperimentTreatmentLocalizations]"] = (
                encode_param(
                    limit_app_store_version_experiment_treatment_localizations, False
                )
            )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/appStoreVersionExperimentTreatments/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppStoreVersionExperimentTreatmentResponse,
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
            path=f"/v1/appStoreVersionExperimentTreatments/{id}",
            auth_names=["itc-bearer-token"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
