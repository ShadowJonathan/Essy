from fastapi import APIRouter, Request

router = APIRouter()


@router.put("/domain/{domain}")
async def create_domain(request: Request, domain: str):
    pass  # TODO grab domain param from body


@router.delete("/domain/{domain}")
async def delete_domain(request: Request, domain: str):
    pass


@router.get("/file/{domain}/{file_path:path}")
async def get_domain_file(request: Request, domain: str, file_path: str):
    pass


@router.put("/file/{domain}/{file_path:path}")
async def put_domain_file(request: Request, domain: str, file_path: str):
    pass


@router.delete("/file/{domain}/{file_path:path}")
async def delete_domain_file(request: Request, domain: str, file_path: str):
    pass
