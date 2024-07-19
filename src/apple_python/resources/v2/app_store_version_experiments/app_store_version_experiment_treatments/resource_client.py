"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    AsyncBaseClient,
    RequestOptions,
    QueryParams,
    SyncBaseClient,
    default_request_options,
    encode_param,
)
import typing
import typing_extensions
from apple_python.types.v2.app_store_version_experiments.app_store_version_experiment_treatments import (
    models,
)


class AppStoreVersionExperimentTreatmentsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
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
        fields_app_store_version_experiments: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
                    "appStoreVersion",
                    "appStoreVersionExperimentTreatments",
                    "controlVersions",
                    "endDate",
                    "latestControlVersion",
                    "name",
                    "platform",
                    "reviewRequired",
                    "startDate",
                    "started",
                    "state",
                    "trafficProportion",
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
        limit: typing.Optional[int] = None,
        limit_app_store_version_experiment_treatment_localizations: typing.Optional[
            int
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppStoreVersionExperimentTreatmentsResponse:
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
        if fields_app_store_version_experiments is not None:
            _query["fields[appStoreVersionExperiments]"] = encode_param(
                fields_app_store_version_experiments, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
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
            path=f"/v2/appStoreVersionExperiments/{id}/appStoreVersionExperimentTreatments",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppStoreVersionExperimentTreatmentsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncAppStoreVersionExperimentTreatmentsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
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
        fields_app_store_version_experiments: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
                    "appStoreVersion",
                    "appStoreVersionExperimentTreatments",
                    "controlVersions",
                    "endDate",
                    "latestControlVersion",
                    "name",
                    "platform",
                    "reviewRequired",
                    "startDate",
                    "started",
                    "state",
                    "trafficProportion",
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
        limit: typing.Optional[int] = None,
        limit_app_store_version_experiment_treatment_localizations: typing.Optional[
            int
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppStoreVersionExperimentTreatmentsResponse:
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
        if fields_app_store_version_experiments is not None:
            _query["fields[appStoreVersionExperiments]"] = encode_param(
                fields_app_store_version_experiments, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
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
            path=f"/v2/appStoreVersionExperiments/{id}/appStoreVersionExperimentTreatments",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppStoreVersionExperimentTreatmentsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
