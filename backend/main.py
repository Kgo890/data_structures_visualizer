from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routes import stack_routes,queue_routes,linked_list_routes,sorting_routes,trees_routes

app = FastAPI(
    title="Data Structures Visualizer API",
    version='1.0.0'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["frontend http"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(stack_routes.router)
app.include_router(queue_routes.router)
app.include_router(linked_list_routes.router)
app.include_router(sorting_routes.router)
app.include_router(trees_routes.router)