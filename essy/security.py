import secrets
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

security = HTTPBasic()

HTTP_BASIC_USERNAME = b"admin"
HTTP_BASIC_PASSWORD = b"admin"


def verify_basic_auth(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
):
    if not (
        secrets.compare_digest(credentials.username.encode("utf8"), HTTP_BASIC_USERNAME)
        and secrets.compare_digest(
            credentials.password.encode("utf8"), HTTP_BASIC_PASSWORD
        )
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
