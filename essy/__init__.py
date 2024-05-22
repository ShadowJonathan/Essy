import datetime
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .security import verify_basic_auth

from .api import router as api_router
from .form import router as form_router
from .service import domain as domain_srv, files as files_srv


# TODO use lifecycle manager to fetch config and set credentials and such?


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up")
    yield
    print("Shutting down")


app = FastAPI(dependencies=[Depends(verify_basic_auth)], lifespan=lifespan)

app.include_router(api_router, prefix="/api")
app.include_router(form_router, prefix="/form")

ESSY_DIR = Path(__file__).parent.resolve()
STATIC_DIR = ESSY_DIR / "static"
TEMPLATE_DIR = ESSY_DIR / "templates"

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
templates = Jinja2Templates(directory=str(TEMPLATE_DIR))


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse(
        STATIC_DIR / "favicon.ico", media_type="image/vnd.microsoft.icon"
    )


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html.j2",
        context={
            # TODO
            "time": str(datetime.datetime.now())
        },
    )


@app.get("/domains", response_class=HTMLResponse)
async def domains(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="domains.html.j2",
        context={"domains": domain_srv.all_domains()},
    )


@app.get("/domain/{domain}", response_class=HTMLResponse)
async def domain_info(request: Request, domain: str):
    return templates.TemplateResponse(
        request=request,
        name="domain.html.j2",
        context={
            "domain": domain,
        },
    )


@app.get("/files/{domain}", response_class=HTMLResponse)
async def domain_files(request: Request, domain: str):
    return templates.TemplateResponse(
        request=request,
        name="domain_files.html.j2",
        context={
            "domain": domain,
            "files": sorted(files_srv.files_for(domain)),
        },
    )
