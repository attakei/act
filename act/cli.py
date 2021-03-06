# -*- coding:utf-8 -*-
from pathlib import Path
import logging
import subprocess
import click


Logger = logging.getLogger(__name__)

ROOT = Path(__file__).resolve().parents[1]  # type: Path


@click.group()
def act():
    pass


@act.command()
def upgrade():
    """Upgrade act
    """
    repo_dir = Path(__file__).parent.parent
    # Run git pull
    from git import Repo
    repo = Repo(str(repo_dir))
    repo.git.pull()
    # TODO: Not use subprocess (use Python lib)
    commands = [
        'pip install -e .',
    ]
    for command in commands:
        proc = subprocess.Popen(
            command.split(), cwd=str(repo_dir))
        proc.communicate()


def main():
    """Script endpoint
    """
    # Import subcommands
    from . import (  # noqa: falke8
        git,
        gitlab,
        pelican,
        python,
    )
    act()
