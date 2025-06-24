from backend.models.double_linked_list import DoubleLinkedList
from fastapi import APIRouter
from backend.schemas.linked_list_schema import LinkedListItem

router = APIRouter(
    prefix="/double-linked-list",
    tags=["doubleLinkedList"]
)
double_linked_list = DoubleLinkedList()


@router.post("/add-head")
async def insert_list_from_head(item: LinkedListItem):
    double_linked_list.insert_at_head(item.value)
    return {'message': f'{item.value} was inserted at the head of the linked list',
            'current': double_linked_list.traverse()}


@router.post("/add-tail")
async def insert_list_from_tail(item: LinkedListItem):
    double_linked_list.insert_at_tail(item.value)
    return {'message': f'{item.value} was inserted at the tail of the linked list',
            'current': double_linked_list.traverse()}


@router.delete("/")
async def deleting_from_linked_list(value: int):
    if not double_linked_list.search(value):
        return {'error': f'{value} not found in the linked list'}
    double_linked_list.delete(value)
    return {'message': f'The {value} has been deleted from the linked list', 'current': double_linked_list.traverse()}


@router.get('/search')
async def searching_the_linked_list(value: int):
    if double_linked_list.search(value) == -1:
        return {'error': f'{value} was not found in the linked list'}
    return {'message': f'The {value} has been found in the linked list'}


@router.get('/forward-traverse')
async def traversing_the_double_linked_list():
    return {'message': double_linked_list.traverse()}


@router.get('/reverse-traverse')
async def traversing_the_double_linked_list_reverse():
    return {'message': double_linked_list.reverse_traverse()}