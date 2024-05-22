import shutil
import tempfile
from pathlib import Path
from tempfile import TemporaryFile
from typing import BinaryIO

from starlette.requests import Request
from anyio import to_thread


async def save_request_as_tempfile(request: Request) -> TemporaryFile:
    f = tempfile.TemporaryFile()
    async for chunk in request.stream():
        f.write(chunk)

    f.seek(0)

    return f


async def persist_file(f: BinaryIO, to_location: Path):
    with open(to_location, "wb") as new_file:
        await to_thread.run_sync(shutil.copyfileobj, f, new_file)
