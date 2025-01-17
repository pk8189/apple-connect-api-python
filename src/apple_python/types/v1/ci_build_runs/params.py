"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class CiBuildRunCreateRequestDataAttributes(typing_extensions.TypedDict):
    """
    No description specified
    """

    clean: typing_extensions.NotRequired[bool]


class _SerializerCiBuildRunCreateRequestDataAttributes(pydantic.BaseModel):
    """
    Serializer for CiBuildRunCreateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    clean: typing.Optional[bool] = pydantic.Field(alias="clean", default=None)


class CiBuildRunCreateRequestDataRelationshipsBuildRunData(typing_extensions.TypedDict):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["ciBuildRuns"]]


class _SerializerCiBuildRunCreateRequestDataRelationshipsBuildRunData(
    pydantic.BaseModel
):
    """
    Serializer for CiBuildRunCreateRequestDataRelationshipsBuildRunData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["ciBuildRuns"] = pydantic.Field(alias="type")


class CiBuildRunCreateRequestDataRelationshipsPullRequestData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["scmPullRequests"]]


class _SerializerCiBuildRunCreateRequestDataRelationshipsPullRequestData(
    pydantic.BaseModel
):
    """
    Serializer for CiBuildRunCreateRequestDataRelationshipsPullRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["scmPullRequests"] = pydantic.Field(alias="type")


class CiBuildRunCreateRequestDataRelationshipsSourceBranchOrTagData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["scmGitReferences"]]


class _SerializerCiBuildRunCreateRequestDataRelationshipsSourceBranchOrTagData(
    pydantic.BaseModel
):
    """
    Serializer for CiBuildRunCreateRequestDataRelationshipsSourceBranchOrTagData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["scmGitReferences"] = pydantic.Field(alias="type")


class CiBuildRunCreateRequestDataRelationshipsWorkflowData(typing_extensions.TypedDict):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["ciWorkflows"]]


class _SerializerCiBuildRunCreateRequestDataRelationshipsWorkflowData(
    pydantic.BaseModel
):
    """
    Serializer for CiBuildRunCreateRequestDataRelationshipsWorkflowData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["ciWorkflows"] = pydantic.Field(alias="type")


class CiBuildRunCreateRequestDataRelationshipsBuildRun(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.NotRequired[
        CiBuildRunCreateRequestDataRelationshipsBuildRunData
    ]


class _SerializerCiBuildRunCreateRequestDataRelationshipsBuildRun(pydantic.BaseModel):
    """
    Serializer for CiBuildRunCreateRequestDataRelationshipsBuildRun handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: typing.Optional[
        _SerializerCiBuildRunCreateRequestDataRelationshipsBuildRunData
    ] = pydantic.Field(alias="data", default=None)


class CiBuildRunCreateRequestDataRelationshipsPullRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.NotRequired[
        CiBuildRunCreateRequestDataRelationshipsPullRequestData
    ]


class _SerializerCiBuildRunCreateRequestDataRelationshipsPullRequest(
    pydantic.BaseModel
):
    """
    Serializer for CiBuildRunCreateRequestDataRelationshipsPullRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: typing.Optional[
        _SerializerCiBuildRunCreateRequestDataRelationshipsPullRequestData
    ] = pydantic.Field(alias="data", default=None)


class CiBuildRunCreateRequestDataRelationshipsSourceBranchOrTag(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.NotRequired[
        CiBuildRunCreateRequestDataRelationshipsSourceBranchOrTagData
    ]


class _SerializerCiBuildRunCreateRequestDataRelationshipsSourceBranchOrTag(
    pydantic.BaseModel
):
    """
    Serializer for CiBuildRunCreateRequestDataRelationshipsSourceBranchOrTag handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: typing.Optional[
        _SerializerCiBuildRunCreateRequestDataRelationshipsSourceBranchOrTagData
    ] = pydantic.Field(alias="data", default=None)


class CiBuildRunCreateRequestDataRelationshipsWorkflow(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.NotRequired[
        CiBuildRunCreateRequestDataRelationshipsWorkflowData
    ]


class _SerializerCiBuildRunCreateRequestDataRelationshipsWorkflow(pydantic.BaseModel):
    """
    Serializer for CiBuildRunCreateRequestDataRelationshipsWorkflow handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: typing.Optional[
        _SerializerCiBuildRunCreateRequestDataRelationshipsWorkflowData
    ] = pydantic.Field(alias="data", default=None)


class CiBuildRunCreateRequestDataRelationships(typing_extensions.TypedDict):
    """
    No description specified
    """

    build_run: typing_extensions.NotRequired[
        CiBuildRunCreateRequestDataRelationshipsBuildRun
    ]
    pull_request: typing_extensions.NotRequired[
        CiBuildRunCreateRequestDataRelationshipsPullRequest
    ]
    source_branch_or_tag: typing_extensions.NotRequired[
        CiBuildRunCreateRequestDataRelationshipsSourceBranchOrTag
    ]
    workflow: typing_extensions.NotRequired[
        CiBuildRunCreateRequestDataRelationshipsWorkflow
    ]


class _SerializerCiBuildRunCreateRequestDataRelationships(pydantic.BaseModel):
    """
    Serializer for CiBuildRunCreateRequestDataRelationships handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    build_run: typing.Optional[
        _SerializerCiBuildRunCreateRequestDataRelationshipsBuildRun
    ] = pydantic.Field(alias="buildRun", default=None)
    pull_request: typing.Optional[
        _SerializerCiBuildRunCreateRequestDataRelationshipsPullRequest
    ] = pydantic.Field(alias="pullRequest", default=None)
    source_branch_or_tag: typing.Optional[
        _SerializerCiBuildRunCreateRequestDataRelationshipsSourceBranchOrTag
    ] = pydantic.Field(alias="sourceBranchOrTag", default=None)
    workflow: typing.Optional[
        _SerializerCiBuildRunCreateRequestDataRelationshipsWorkflow
    ] = pydantic.Field(alias="workflow", default=None)


class CiBuildRunCreateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.NotRequired[CiBuildRunCreateRequestDataAttributes]
    relationships: typing_extensions.NotRequired[
        CiBuildRunCreateRequestDataRelationships
    ]
    type: typing_extensions.Required[typing_extensions.Literal["ciBuildRuns"]]


class _SerializerCiBuildRunCreateRequestData(pydantic.BaseModel):
    """
    Serializer for CiBuildRunCreateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: typing.Optional[_SerializerCiBuildRunCreateRequestDataAttributes] = (
        pydantic.Field(alias="attributes", default=None)
    )
    relationships: typing.Optional[
        _SerializerCiBuildRunCreateRequestDataRelationships
    ] = pydantic.Field(alias="relationships", default=None)
    type: typing_extensions.Literal["ciBuildRuns"] = pydantic.Field(alias="type")


class CiBuildRunCreateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[CiBuildRunCreateRequestData]


class _SerializerCiBuildRunCreateRequest(pydantic.BaseModel):
    """
    Serializer for CiBuildRunCreateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerCiBuildRunCreateRequestData = pydantic.Field(alias="data")
