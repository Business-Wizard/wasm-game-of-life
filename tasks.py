import shlex
import subprocess
from typing import Iterable
from invoke import context
import invoke
from pathlib import Path
import webbrowser
import time


ROOT: Path = Path(__file__).parent
WWW_DIR: Path = ROOT / 'www'


@invoke.task
def build_all(context: context.Context) -> None:
    context.run(command='wasm-pack build')
    context.run(command='npm init wasm-app www')


@invoke.task
def build(context: context.Context) -> None:
    with context.cd(path=WWW_DIR):
        context.run(command='npm install')


@invoke.task
def serve(context: context.Context) -> None:
    webbrowser.open(url='http://localhost:8080')
    with context.cd(path=WWW_DIR):
        context.run('npm run start')
