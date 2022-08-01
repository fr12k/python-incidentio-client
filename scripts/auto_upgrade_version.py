import textwrap
from pathlib import Path
from typing import Any, Dict, Mapping

import click
import toml
from pkg_resources import parse_version
from toml import TomlEncoder  # type:ignore
from pkg_resources.extern.packaging.version import Version  # type:ignore

CHANGELOG_TEMPLATE = textwrap.dedent(
    """
    # v{version}

    - {message}
"""
).strip()


class AutoUpdateChangelogException(Exception):
    pass


class VersionKeyNotFoundError(Exception):
    pass


def load_pyproject(pyproject_path: Path) -> Dict[str, Any]:
    with pyproject_path.open() as f:
        content = toml.load(f)

    return content


def get_version_number(content: dict) -> Version:
    try:
        version_str = content["tool"]["poetry"]["version"]
    except KeyError:
        raise VersionKeyNotFoundError("Key `version` in `[tool.poetry]` section not found")

    version = parse_version(str(version_str))

    return version


def increase_major_version(version: Version) -> Version:
    if version.major == 0:
        major = 0
        minor = version.minor + 1
    else:
        major = 0
        minor = version.minor + 1

    version_str = f"{major}.{minor}.0"
    version = Version(version_str)

    return version


def update_version_in_pyproject(content: Dict[str, Any], version: Version) -> Dict[str, any]:
    content["tool"]["poetry"]["version"] = str(version)

    return content


def save_pyproject(pyproject_path: Path, content: Mapping[str, Any]) -> None:
    encoder = TomlEncoder(preserve=True)

    with pyproject_path.open("w") as f:
        toml.dump(content, f, encoder=encoder)


@click.command()
@click.argument(
    "pyproject_path",
    type=click.Path(file_okay=True, dir_okay=False, resolve_path=True, path_type=Path),
)
def main(pyproject_path: Path) -> None:
    """
    Updates the pyproject.toml by increasing the version number
    """
    # Get version from pyproject.toml
    content = load_pyproject(pyproject_path)
    version = get_version_number(content)

    # Increase version number
    version = increase_major_version(version)
    content = update_version_in_pyproject(content, version)

    # Update pyproject
    save_pyproject(pyproject_path, content)


if __name__ == "__main__":
    main()
