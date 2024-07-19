"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    default_request_options,
    RequestOptions,
    encode_param,
    AsyncBaseClient,
    QueryParams,
    SyncBaseClient,
)
import typing
import typing_extensions
from apple_python.types.v1.app_infos.primary_subcategory_one import models


class PrimarySubcategoryOneClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        id: str,
        fields_app_categories: typing.Optional[
            typing.List[
                typing_extensions.Literal["parent", "platforms", "subcategories"]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[typing_extensions.Literal["parent", "subcategories"]]
        ] = None,
        limit_subcategories: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppCategoryResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_app_categories is not None:
            _query["fields[appCategories]"] = encode_param(fields_app_categories, False)
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit_subcategories is not None:
            _query["limit[subcategories]"] = encode_param(limit_subcategories, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/appInfos/{id}/primarySubcategoryOne",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppCategoryResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncPrimarySubcategoryOneClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        id: str,
        fields_app_categories: typing.Optional[
            typing.List[
                typing_extensions.Literal["parent", "platforms", "subcategories"]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[typing_extensions.Literal["parent", "subcategories"]]
        ] = None,
        limit_subcategories: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppCategoryResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_app_categories is not None:
            _query["fields[appCategories]"] = encode_param(fields_app_categories, False)
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit_subcategories is not None:
            _query["limit[subcategories]"] = encode_param(limit_subcategories, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/appInfos/{id}/primarySubcategoryOne",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppCategoryResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
