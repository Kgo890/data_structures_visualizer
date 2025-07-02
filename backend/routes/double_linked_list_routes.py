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


@router.delete("/delete-back")
async def delete_back():
    value = double_linked_list.delete_from_back()
    if value is None:
        return {'error': 'List is already empty'}
    return {
        'message': f'Delete: {value} from back',
        'current': double_linked_list.traverse()
    }


@router.delete("/delete-front")
async def delete_front():
    value = double_linked_list.delete_from_front()
    if value is None:
        return {'error': 'List is already empty'}
    return {
        'message': f'Delete: {value} from front',
        'current': double_linked_list.traverse()
    }


@router.get('/search')
async def searching_the_double_linked_list(value: int):
    index = double_linked_list.search(value)
    if index == -1:
        return {
            'found': False,
            'message': f'{value} was not found in the double linked list'
        }
    return {
        'found': True,
        'index': index,
        'message': f' Value {value} found at index {index} in the double linked list'
    }


@router.get('/forward-traverse')
async def traversing_the_double_linked_list():
    return {'message': double_linked_list.traverse()}


@router.get('/reverse-traverse')
async def traversing_the_double_linked_list_reverse():
    return {'message': double_linked_list.reverse_traverse()}


@router.get('/reverse')
async def reverse_linked_list():
    steps = double_linked_list.reverse()
    return {
        'message': 'Reversed the linked list',
        'steps': steps,
        'current': double_linked_list.traverse()
    }


@router.get('/clear')
async def reset():
    return {'message': double_linked_list.reset()}
