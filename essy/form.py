from pathlib import Path
from typing import Annotated, Optional

from fastapi import (
    APIRouter,
    Form,
    UploadFile,
    File,
    HTTPException,
)
from starlette.responses import RedirectResponse

from .service import domain as domain_srv, files as files_srv
from .util import persist_file

router = APIRouter()


@router.post("/domain/create", include_in_schema=False)
async def create_domain(domain: Annotated[str, Form()]):
    domain_srv.create(domain)


@router.post("/domain/delete", include_in_schema=False)
async def delete_domain(domain: Annotated[str, Form()]):
    domain_srv.delete(domain)


@router.post("/file/{domain}/upload", include_in_schema=False)
async def upload_file(
    domain: str,
    directory: Annotated[str, Form()],
    new_file: Annotated[UploadFile, File()],
    file_name: Optional[str] = Form(None),
):
    if not domain_srv.exists(domain):
        raise HTTPException(status_code=404)

    file_name = Path(file_name or new_file.filename)

    if file_name.is_absolute():
        file_name = file_name.relative_to("/")

    file_path = (Path("/") / directory.strip() / file_name).resolve()

    to_path = files_srv.real_path(domain, file_path)

    await persist_file(new_file.file, to_path)

    return RedirectResponse(f"/files/{domain}", status_code=303)




@router.post("/file/{domain}/delete", include_in_schema=False)
async def delete_file(domain: str, file_path: Annotated[str, Form()]):
    files_srv.delete_file(domain, file_path)
