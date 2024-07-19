"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    AsyncBaseClient,
    SyncBaseClient,
    default_request_options,
    QueryParams,
    to_encodable,
    encode_param,
    RequestOptions,
)
from apple_python.resources.v2.app_store_version_experiments.app_store_version_experiment_treatments import (
    AsyncAppStoreVersionExperimentTreatmentsClient,
    AppStoreVersionExperimentTreatmentsClient,
)
import typing
import typing_extensions
from apple_python.types.v2.app_store_version_experiments import models, params


class AppStoreVersionExperimentsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.app_store_version_experiment_treatments = (
            AppStoreVersionExperimentTreatmentsClient(base_client=self._base_client)
        )

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.AppStoreVersionExperimentV2CreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppStoreVersionExperimentV2Response:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerAppStoreVersionExperimentV2CreateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/v2/appStoreVersionExperiments",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.AppStoreVersionExperimentV2Response,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def patch(
        self,
        *,
        data: params.AppStoreVersionExperimentV2UpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppStoreVersionExperimentV2Response:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerAppStoreVersionExperimentV2UpdateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="PATCH",
            path=f"/v2/appStoreVersionExperiments/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.AppStoreVersionExperimentV2Response,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def get(
        self,
        *,
        id: str,
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
                    "app",
                    "appStoreVersionExperimentTreatments",
                    "controlVersions",
                    "latestControlVersion",
                ]
            ]
        ] = None,
        limit_app_store_version_experiment_treatments: typing.Optional[int] = None,
        limit_control_versions: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppStoreVersionExperimentV2Response:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
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
        if limit_app_store_version_experiment_treatments is not None:
            _query["limit[appStoreVersionExperimentTreatments]"] = encode_param(
                limit_app_store_version_experiment_treatments, False
            )
        if limit_control_versions is not None:
            _query["limit[controlVersions]"] = encode_param(
                limit_control_versions, False
            )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v2/appStoreVersionExperiments/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppStoreVersionExperimentV2Response,
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
            path=f"/v2/appStoreVersionExperiments/{id}",
            auth_names=["itc-bearer-token"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncAppStoreVersionExperimentsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.app_store_version_experiment_treatments = (
            AsyncAppStoreVersionExperimentTreatmentsClient(
                base_client=self._base_client
            )
        )

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.AppStoreVersionExperimentV2CreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppStoreVersionExperimentV2Response:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerAppStoreVersionExperimentV2CreateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/v2/appStoreVersionExperiments",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.AppStoreVersionExperimentV2Response,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def patch(
        self,
        *,
        data: params.AppStoreVersionExperimentV2UpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppStoreVersionExperimentV2Response:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerAppStoreVersionExperimentV2UpdateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="PATCH",
            path=f"/v2/appStoreVersionExperiments/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.AppStoreVersionExperimentV2Response,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def get(
        self,
        *,
        id: str,
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
                    "app",
                    "appStoreVersionExperimentTreatments",
                    "controlVersions",
                    "latestControlVersion",
                ]
            ]
        ] = None,
        limit_app_store_version_experiment_treatments: typing.Optional[int] = None,
        limit_control_versions: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppStoreVersionExperimentV2Response:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
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
        if limit_app_store_version_experiment_treatments is not None:
            _query["limit[appStoreVersionExperimentTreatments]"] = encode_param(
                limit_app_store_version_experiment_treatments, False
            )
        if limit_control_versions is not None:
            _query["limit[controlVersions]"] = encode_param(
                limit_control_versions, False
            )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v2/appStoreVersionExperiments/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppStoreVersionExperimentV2Response,
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
            path=f"/v2/appStoreVersionExperiments/{id}",
            auth_names=["itc-bearer-token"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)