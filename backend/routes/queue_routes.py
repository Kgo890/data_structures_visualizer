from backend.models.queue import Queue
from fastapi import APIRouter
from backend.schemas.queue_schema import QueueItem

router = APIRouter(
    prefix="/queue",
    tags=["Queue"]
)
queue = Queue()


@router.post("/")
async def enqueue_to_queue(item: QueueItem):
    queue.enqueue(item.value)
    return {'message': f'{item.value} enqueue to the queue'}


@router.delete("/")
async def dequeue_from_queue():
    if queue.is_empty():
        return {'error': 'The queue is empty'}
    value = queue.dequeue()
    return {'message': f'The {value} removed from the head of the queue'}


@router.get('/peek')
async def peek_in_queue():
    if queue.is_empty():
        return {'error': 'The queue is empty'}
    value = queue.peek()
    return {'message': f"{value} is head of the queue"}


@router.get('/empty')
async def is_queue_empty():
    return {'message': queue.is_empty()}


@router.get('/get-items')
async def get_queue():
    return {'message': queue.items}


@router.get('/size')
async def get_size():
    return {'message': queue.size()}


@router.get('/clear')
async def reset_queue():
    return {'message': queue.reset()}
