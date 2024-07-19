"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    default_request_options,
    QueryParams,
    encode_param,
    RequestOptions,
    SyncBaseClient,
    to_encodable,
    AsyncBaseClient,
)
import typing
import typing_extensions
from apple_python.types.v1.app_encryption_declaration_documents import models, params


class AppEncryptionDeclarationDocumentsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.AppEncryptionDeclarationDocumentCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppEncryptionDeclarationDocumentResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerAppEncryptionDeclarationDocumentCreateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/v1/appEncryptionDeclarationDocuments",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.AppEncryptionDeclarationDocumentResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def patch(
        self,
        *,
        data: params.AppEncryptionDeclarationDocumentUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppEncryptionDeclarationDocumentResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerAppEncryptionDeclarationDocumentUpdateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="PATCH",
            path=f"/v1/appEncryptionDeclarationDocuments/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.AppEncryptionDeclarationDocumentResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def get(
        self,
        *,
        id: str,
        fields_app_encryption_declaration_documents: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appEncryptionDeclaration",
                    "assetDeliveryState",
                    "assetToken",
                    "downloadUrl",
                    "fileName",
                    "fileSize",
                    "sourceFileChecksum",
                    "uploadOperations",
                    "uploaded",
                ]
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppEncryptionDeclarationDocumentResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_app_encryption_declaration_documents is not None:
            _query["fields[appEncryptionDeclarationDocuments]"] = encode_param(
                fields_app_encryption_declaration_documents, False
            )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/appEncryptionDeclarationDocuments/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppEncryptionDeclarationDocumentResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncAppEncryptionDeclarationDocumentsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.AppEncryptionDeclarationDocumentCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppEncryptionDeclarationDocumentResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerAppEncryptionDeclarationDocumentCreateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/v1/appEncryptionDeclarationDocuments",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.AppEncryptionDeclarationDocumentResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def patch(
        self,
        *,
        data: params.AppEncryptionDeclarationDocumentUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppEncryptionDeclarationDocumentResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerAppEncryptionDeclarationDocumentUpdateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="PATCH",
            path=f"/v1/appEncryptionDeclarationDocuments/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.AppEncryptionDeclarationDocumentResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def get(
        self,
        *,
        id: str,
        fields_app_encryption_declaration_documents: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "appEncryptionDeclaration",
                    "assetDeliveryState",
                    "assetToken",
                    "downloadUrl",
                    "fileName",
                    "fileSize",
                    "sourceFileChecksum",
                    "uploadOperations",
                    "uploaded",
                ]
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppEncryptionDeclarationDocumentResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_app_encryption_declaration_documents is not None:
            _query["fields[appEncryptionDeclarationDocuments]"] = encode_param(
                fields_app_encryption_declaration_documents, False
            )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/appEncryptionDeclarationDocuments/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.AppEncryptionDeclarationDocumentResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
