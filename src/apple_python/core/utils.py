import typing


def remove_none_from_dict(
    original: typing.Dict[str, typing.Optional[typing.Any]],
) -> typing.Dict[str, typing.Any]:
    new: typing.Dict[str, typing.Any] = {}
    for key, value in original.items():
        if value is not None:
            new[key] = value
    return new
