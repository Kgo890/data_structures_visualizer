from backend.models.binary_tree import BinaryTree
from fastapi import APIRouter
from backend.schemas.binary_tree_schema import BinaryTreeItem

router = APIRouter(
    prefix="/binary-tree",
    tags=["BinaryTree"]
)
binary_tree = BinaryTree()


@router.post("/")
async def insert_to_binary_tree(item: BinaryTreeItem):
    binary_tree.insert(item.value)
    return {'message': f'{item.value} was inserted into the binary tree',
            'current': binary_tree.in_order_traverse()}


@router.get("/search")
async def search_in_binary_tree(value: int):
    if not binary_tree.search(value):
        return {'error': f'{value} was not found in the binary tree'}
    return {'message': f'The {value} has been found in the binary tree'}


@router.get('/in_order-traverse')
async def traversing_inorder():
    return {'message': binary_tree.in_order_traverse()}


@router.get('/pre_order-traverse')
async def traversing_pre_order():
    return {'message': binary_tree.pre_order_traverse()}


@router.get('/post_order-traverse')
async def traversing_post_order():
    return {'message': binary_tree.post_order_traverse()}


@router.get('/height')
async def height_of_binary_tree():
    return {'message': f'The height of this Binary Tree is {binary_tree.height()}'}


@router.delete('/')
async def delete_from_binary_tree(value: int):
    if not binary_tree.search(value):
        return {'error': f'{value} not found in the binary tree'}
    binary_tree.delete(value)
    return {'message': f'The {value} has been deleted from the binary tree', 'current': binary_tree.in_order_traverse()}
