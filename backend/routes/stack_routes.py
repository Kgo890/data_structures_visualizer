from backend.models.stack import Stack
from fastapi import APIRouter
from backend.schemas.stack_schema import StackItem

stack_router = APIRouter(
    prefix="/stack",
    tags=["Stack"]
)
stack = Stack()


@stack_router.post("/")
async def push_to_stack(item: StackItem):
    stack.push(item.value)
    return {'message': f'{item.value} pushed to the stack'}


@stack_router.delete("/")
async def pop_from_stack():
    if stack.is_empty():
        return {'error': 'The stack is empty'}
    value = stack.pop()
    return {'message': f'The {value} has been pop from the stack'}


@stack_router.get('/peek')
async def peek_in_stack():
    if stack.is_empty():
        return {'error': 'The stack is empty'}
    value = stack.peek()
    return {'message': f"{value} is the top of the stack"}


@stack_router.get('/empty')
async def is_stack_empty():
    return {'message': stack.is_empty()}


@stack_router.get('/get-items')
async def get_stack():
    return {'message': stack.items}


@stack_router.get("/clear")
async def reset_stack():
    return {'message': stack.reset()}


@stack_router.get('/size')
async def get_size():
    return {'message': stack.size()}
