import pytest

import autoconf as ac
from test_autoconf.mock import GeometryProfile


@pytest.fixture(
    name="geometry_profile_path"
)
def make_geometry_profile_path():
    return ["test_autoconf", "mock", "GeometryProfile"]


def test_path_for_class(geometry_profile_path):
    assert ac.path_for_class(
        GeometryProfile
    ) == geometry_profile_path


@pytest.mark.parametrize(
    "config_dict",
    [
        {
            "test_autoconf.mock.GeometryProfile": "test",
            "test_autoconf.mock.Other": "toast"
        },
        {
            "test_autoconf.mock": {"GeometryProfile": "test", "Other": "toast"},
        },
        {
            "test_autoconf": {"mock": {"GeometryProfile": "test", "Other": "toast"}}
        },
        {
            "test_autoconf": {"mock.GeometryProfile": "test", "mock.Other": "toast"}
        },
        {
            "*.GeometryProfile": "test", "*.Other": "toast"
        },
        {
            "*.mock.GeometryProfile": "test", "*.mock.Other": "toast"
        },
        {
            "*.mock": {"GeometryProfile": "test", "Other": "toast"}
        },
        {
            "test_autoconf": {"*.GeometryProfile": "test", "*.Other": "toast"}
        }
    ]
)
def test_config_for_path(
        geometry_profile_path,
        config_dict
):
    config = ac.JSONPriorConfig(
        config_dict
    )
    assert config(
        geometry_profile_path
    ) == "test"
    assert config(
        ["test_autoconf", "mock", "Other"]
    ) == "toast"
