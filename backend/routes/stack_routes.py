from backend.models.stack import Stack
from fastapi import APIRouter
from backend.schemas.stack_schema import StackItem

router = APIRouter(
    prefix="/stack",
    tags=["Stack"]
)
stack = Stack()


@router.post("/")
async def push_to_stack(item: StackItem):
    stack.push(item.value)
    return {'message': f'{item.value} pushed to the stack'}


@router.delete("/")
async def pop_from_stack():
    if stack.is_empty():
        return {'error': 'The stack is empty'}
    value = stack.pop()
    return {'message': f'The {value} has been pop from the stack'}


@router.get('/peek')
async def peek_in_stack():
    if stack.is_empty():
        return {'error': 'The stack is empty'}
    value = stack.peek()
    return {'message': f"{value} is the top of the stack"}


@router.get('/empty')
async def is_stack_empty():
    return {'message': stack.is_empty()}


@router.get('/')
async def get_stack():
    return {'message': stack.items}
