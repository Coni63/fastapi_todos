from fastapi import FastAPI

from app import routes

description = """
# INFORMATION

This API helps you manage your todos. 🚀
"""

openapi_tags = [
    {
        "name": "todos",
        "description": "Manage todos - CRUD operations",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]

app = FastAPI(
    title="TODO APP",
    description=description,
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Coni",
        "url": "http://x-force.example.com/contact/",
        "email": "dp@x-force.example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    openapi_tags=openapi_tags
)

app.include_router(routes.router)