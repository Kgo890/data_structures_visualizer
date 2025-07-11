from backend.models.graphs import Graph
from fastapi import APIRouter
from backend.schemas.graph_schema import NodeItem,EdgeItem

graphs_router = APIRouter(
    prefix="/graphs",
    tags=["Graphs"]
)

graphs = Graph()


@graphs_router.post("/add_node")
async def adding_nodes_to_graphs(item: NodeItem):
    graphs.add_node(item.node)
    return {
        'message': f'{item.value} node was added in the graph',
        'current': graphs.get_graph()
    }


@graphs_router.post("/add_edge")
async def adding_edge_to_graphs(item: EdgeItem ):
    graphs.add_edge(item.first_node, item.second_node)
    return {
        'message': f' a edge was added for {item.first_node} and {item.second_node} in the graph',
        'current': graphs.get_graph()
    }


@graphs_router.get("/unconnected_vertices")
async def getting_unconnected_vertices():
    value = graphs.unconnected_vertices()
    return {
        'message': f'The unconnected vertices in your graph: {value}',
    }


@graphs_router.get("/search_node")
async def searching_node(item: NodeItem):
    result = graphs.search(item.value)
    if not result:
        return {
            'message': f'{item.value} is not in your graph',
        }
    return {
        'message': f'{item.value} is in your graph',
    }


@graphs_router.get("/current")
async def get_current_graph():
    return {
        'message': graphs.get_graph()
    }


@graphs_router.get("/reset")
async def reset_graph():
    graphs.reset()
    return {'message': 'Graph reset successfully'}