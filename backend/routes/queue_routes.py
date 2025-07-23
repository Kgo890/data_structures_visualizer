from backend.models.queue import Queue
from fastapi import APIRouter
from backend.schemas.queue_schema import QueueItem

queue_router = APIRouter(
    prefix="/queue",
    tags=["Queue"]
)
queue = Queue()


@queue_router.post("/enqueue")
async def enqueue_to_queue(item: QueueItem):
    queue.enqueue(item.value)
    return {'message': f'{item.value} enqueue to the queue'}


@queue_router.delete("/dequeue")
async def dequeue_from_queue():
    if queue.is_empty():
        return {'error': 'The queue is empty'}
    value = queue.dequeue()
    return {'message': f'The {value} removed from the head of the queue'}


@queue_router.get('/peek')
async def peek_in_queue():
    if queue.is_empty():
        return {'error': 'The queue is empty'}
    value = queue.peek()
    return {'message': f"{value} is head of the queue"}


@queue_router.get('/empty')
async def is_queue_empty():
    return {'message': queue.is_empty()}


@queue_router.get('/get-items')
async def get_queue():
    return {'message': queue.items}


@queue_router.get('/size')
async def get_size():
    return {'message': queue.size()}


@queue_router.get('/clear')
async def reset_queue():
    return {'message': queue.reset()}
