"""File Generated by Sideko (sideko.dev)"""

import io
import typing
import typing_extensions
from pydantic import (
    BaseModel as _PydanticBaseModel,
    Field as _PydanticField,
    ConfigDict as _PydanticConfigDict,
)

ModelFiles = typing.List[
    typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]
]


class CiTestResultAttributesDestinationTestResultsItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    device_name: typing.Optional[str] = _PydanticField(alias="deviceName", default=None)
    duration: typing.Optional[float] = _PydanticField(alias="duration", default=None)
    os_version: typing.Optional[str] = _PydanticField(alias="osVersion", default=None)
    status: typing.Optional[
        typing_extensions.Literal[
            "SUCCESS", "FAILURE", "MIXED", "SKIPPED", "EXPECTED_FAILURE"
        ]
    ] = _PydanticField(alias="status", default=None)
    uuid_field: typing.Optional[str] = _PydanticField(alias="uuid", default=None)


class FileLocation(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    line_number: typing.Optional[int] = _PydanticField(alias="lineNumber", default=None)
    path: typing.Optional[str] = _PydanticField(alias="path", default=None)


class ResourceLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class DocumentLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    self: str = _PydanticField(alias="self")


class CiTestResultAttributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    class_name: typing.Optional[str] = _PydanticField(alias="className", default=None)
    destination_test_results: typing.Optional[
        typing.List[CiTestResultAttributesDestinationTestResultsItem]
    ] = _PydanticField(alias="destinationTestResults", default=None)
    file_source: typing.Optional[FileLocation] = _PydanticField(
        alias="fileSource", default=None
    )
    message: typing.Optional[str] = _PydanticField(alias="message", default=None)
    name: typing.Optional[str] = _PydanticField(alias="name", default=None)
    status: typing.Optional[
        typing_extensions.Literal[
            "SUCCESS", "FAILURE", "MIXED", "SKIPPED", "EXPECTED_FAILURE"
        ]
    ] = _PydanticField(alias="status", default=None)


class CiTestResult(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[CiTestResultAttributes] = _PydanticField(
        alias="attributes", default=None
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    type: typing_extensions.Literal["ciTestResults"] = _PydanticField(alias="type")


class CiTestResultResponse(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: CiTestResult = _PydanticField(alias="data")
    links: DocumentLinks = _PydanticField(alias="links")