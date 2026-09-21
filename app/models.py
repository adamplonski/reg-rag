from pydantic import BaseModel, ConfigDict


class ServiceInfo(BaseModel):
    ok: bool
    version: str
    uptime_seconds: int


class EchoResponse(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)
    response: str
