from pydantic import BaseModel


class HealthCheck(BaseModel):
    """
    Health check response
    """

    status: str
    environment: str
    version: str
    timestamp: str


class ReadyCheck(BaseModel):
    """
    Ready check response
    """

    status: str
    environment: str
    version: str
    app: str
    database: str
    redis: str
    timestamp: str
