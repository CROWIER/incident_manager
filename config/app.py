from fastapi import FastAPI

from config.settings import settings
from api.routes.incidents import router


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_title,
        version=settings.app_version,
        debug=settings.debug,
        description="REST API для справочника инцидентов"
    )

    app.include_router(router)

    return app


app = create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "config.app:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug
    )
