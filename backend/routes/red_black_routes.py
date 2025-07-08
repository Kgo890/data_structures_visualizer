from fastapi import APIRouter, Body
from backend.models.red_black_tree import RBTree
from backend.schemas.red_black_tree_schema import RedBlackTreeItem

red_black_tree_router = APIRouter(
    prefix="/red-black-tree",
    tags=["RedBlackTree"]
)

red_black_tree = RBTree


@red_black_tree_router.post("/insert")
async def insert_to_red_black_tree(item: RedBlackTreeItem):
    red_black_tree.insert(item.value)
    return {
        'message': f'{item.value} was inserted into the binary tree',
        'current': red_black_tree.in_order_traverse()
    }


@red_black_tree_router.get("/search")
async def search_in_binary_tree(item: RedBlackTreeItem):
    depth = red_black_tree.search(item.value)
    if depth == -1:
        return {
            "found": False,
            "message": f"Value {item.value} not found in the binary tree"
        }
    return {
        "found": True,
        "depth": depth,
        "message": f"Value {item.value} found at depth {depth} in the binary tree"
    }


@red_black_tree_router.get("/in_order-traverse")
async def traversing_inorder():
    steps = red_black_tree.in_order_traverse()
    return {"steps": steps, "current": steps}


@red_black_tree_router.get("/pre_order-traverse")
async def traversing_pre_order():
    steps = red_black_tree.pre_order_traverse()
    return {"steps": steps, "current": steps}


@red_black_tree_router.get("/post_order-traverse")
async def traversing_post_order():
    steps = red_black_tree.post_order_traverse()
    return {"steps": steps, "current": steps}


@red_black_tree_router.get("/height")
async def height_of_binary_tree():
    return {
        'height': red_black_tree.height()
    }


@red_black_tree_router.delete("/")
async def delete_from_red_black_tree(item: RedBlackTreeItem):
    if red_black_tree.search(item.value) == -1:
        return {'error': f'{item.value} not found in the binary tree'}
    red_black_tree.delete(item.value)
    return {
        'message': f'The {item.value} has been deleted from the binary tree',
        'current': red_black_tree.in_order_traverse()
    }


@red_black_tree_router.get("/clear")
async def reset():
    red_black_tree.reset()
    return {'message': 'Binary tree has been reset'}


@red_black_tree_router.get("/")
async def get_current_tree():
    return {"message": red_black_tree.in_order_traverse()}


@red_black_tree_router.get("/tree-structure")
async def get_tree_structure():
    return red_black_tree.serialize()


@red_black_tree_router.get("/leaf-count")
async def get_leaf_count():
    return {"leaf_count": red_black_tree.count_leaf_nodes()}
