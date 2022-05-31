from fastapi import FastAPI


from src.api.v1.routers import routers
from src.views.endpoints import pages_router
from src.core.events import set_on_startup, set_on_shutdown


def build_application():
    app = FastAPI()
    
    for path, router in routers.items():
        app.include_router(router, prefix=path)

    app.include_router(pages_router)

    app.add_event_handler("startup", set_on_startup())
    app.add_event_handler("shutdown", set_on_shutdown())

    return app