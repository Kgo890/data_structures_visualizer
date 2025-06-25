from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routes import (
    stack_routes,
    queue_routes,
    singly_linked_list_routes,
    sorting_routes,
    binary_tree_routes,
    double_linked_list_routes
)

app = FastAPI(
    title="Data Structures Visualizer API",
    version='1.0.0'
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(stack_routes.router)
app.include_router(queue_routes.router)
app.include_router(sorting_routes.router)
app.include_router(singly_linked_list_routes.router)
app.include_router(double_linked_list_routes.router)
app.include_router(binary_tree_routes.router)
