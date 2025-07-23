from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routes.stack_routes import stack_router
from backend.routes.queue_routes import queue_router
from backend.routes.singly_linked_list_routes import singly_linked_list_router
from backend.routes.double_linked_list_routes import double_linked_list_router
from backend.routes.binary_tree_routes import binary_tree_router
from backend.routes.sorting_routes import sorting_router
from backend.routes.red_black_routes import red_black_tree_router
from backend.routes.hash_map_routes import hash_map_router
from backend.routes.tries_routes import tries_router
from backend.routes.graphs_routes import graphs_router

app = FastAPI(
    title="Data Structures Visualizer API",
    version='1.0.0'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://data-structures-visualizer-six.vercel.app/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(stack_router)

app.include_router(queue_router)

app.include_router(sorting_router)

app.include_router(singly_linked_list_router)

app.include_router(double_linked_list_router)

app.include_router(binary_tree_router)

app.include_router(red_black_tree_router)

app.include_router(hash_map_router)

app.include_router(tries_router)

app.include_router(graphs_router)
