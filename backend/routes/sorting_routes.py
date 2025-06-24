from backend.models.sorting import selection_sort,insertion_sort,quick_sort,merge_sort,bubble_sort
from fastapi import APIRouter
from backend.schemas.sorting_schema import SortItem

router = APIRouter(
    prefix="/sort",
    tags=["Sort"]
)
sorting = S


@router.get("/bubble")
async def bubble_s(item: SortItem):
    singly_linked_list.insert_at_head(item.value)
    return {'message': f'{item.value} was inserted at the head of the linked list',
            'current': singly_linked_list.traverse()}


@router.get("/quick")
async def quick_s(item: SortItem):
    singly_linked_list.insert_at_tail(item.value)
    return {'message': f'{item.value} was inserted at the tail of the linked list',
            'current': singly_linked_list.traverse()}

@router.get("/merge")
async def merge_s(item: SortItem):
    singly_linked_list.insert_at_tail(item.value)
    return {'message': f'{item.value} was inserted at the tail of the linked list',
            'current': singly_linked_list.traverse()}

@router.get("/selection")
async def selection_s(item: SortItem):
    singly_linked_list.insert_at_tail(item.value)
    return {'message': f'{item.value} was inserted at the tail of the linked list',
            'current': singly_linked_list.traverse()}

@router.get("/insertion")
async def insertion_s(item: SortItem):
    singly_linked_list.insert_at_tail(item.value)
    return {'message': f'{item.value} was inserted at the tail of the linked list',
            'current': singly_linked_list.traverse()}

