from fastapi import APIRouter, Body
from backend.models.binary_tree import BinaryTree
from backend.schemas.binary_tree_schema import BinaryTreeItem

router = APIRouter(
    prefix="/binary-tree",
    tags=["BinaryTree"]
)

binary_tree = BinaryTree()


@router.post("/insert")
async def insert_to_binary_tree(item: BinaryTreeItem):
    binary_tree.insert(item.value)
    return {
        'message': f'{item.value} was inserted into the binary tree',
        'current': binary_tree.in_order_traverse()
    }


@router.get("/search")
async def search_in_binary_tree(value: int):
    depth = binary_tree.search(value)
    if depth == -1:
        return {
            "found": False,
            "message": f"Value {value} not found in the binary tree"
        }
    return {
        "found": True,
        "depth": depth,
        "message": f"Value {value} found at depth {depth} in the binary tree"
    }


@router.get("/in_order-traverse")
async def traversing_inorder():
    steps = binary_tree.in_order_traverse()
    return {"steps": steps, "current": steps}


@router.get("/pre_order-traverse")
async def traversing_pre_order():
    steps = binary_tree.pre_order_traverse()
    return {"steps": steps, "current": steps}


@router.get("/post_order-traverse")
async def traversing_post_order():
    steps = binary_tree.post_order_traverse()
    return {"steps": steps, "current": steps}


@router.get("/height")
async def height_of_binary_tree():
    return {
        'height': binary_tree.height()
    }


@router.delete("/")
async def delete_from_binary_tree(value: int):
    if binary_tree.search(value) == -1:
        return {'error': f'{value} not found in the binary tree'}
    binary_tree.delete(value)
    return {
        'message': f'The {value} has been deleted from the binary tree',
        'current': binary_tree.in_order_traverse()
    }


@router.get("/clear")
async def reset():
    binary_tree.reset()
    return {'message': 'Binary tree has been reset'}


@router.get("/")
async def get_current_tree():
    return {"message": binary_tree.in_order_traverse()}


@router.get("/tree-structure")
async def get_tree_structure():
    return binary_tree.serialize()


@router.get("/is-balanced")
async def check_if_balanced():
    return {"balanced": binary_tree.is_balanced()}


@router.get("/leaf-count")
async def get_leaf_count():
    return {"leaf_count": binary_tree.count_leaf_nodes()}
