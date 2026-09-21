import time
from typing import Annotated

from fastapi import FastAPI, Path

from app.models import EchoResponse, ServiceInfo

START_TIME = time.time()
VERSION = "dev"

app = FastAPI(title="reg-rag")


@app.get("/health", status_code=200, response_model=ServiceInfo)
def health():
    return ServiceInfo(
        ok=True, version=VERSION, uptime_seconds=int(time.time() - START_TIME)
    )


@app.get("/echo/{text}", response_model=EchoResponse)
def echo(text: Annotated[str, Path(max_length=500)]):
    return EchoResponse(response=text)
