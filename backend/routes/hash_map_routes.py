from backend.models.hash_map import HashMap
from fastapi import APIRouter
from backend.schemas.hash_map_schema import HashMapResponse, KeyValuePair

hash_map_router = APIRouter(
    prefix="/hash-map",
    tags=["HashMap"]
)


hash_map = HashMap(size=10)


@hash_map_router.post("/add")
async def insert_into_hashmap(pair: KeyValuePair):
    hash_map.insert(pair.key, pair.value)
    return {
        'message': f'{pair.key}:{pair.value} was inserted into the hashmap',
        'current': hash_map.items()
    }


@hash_map_router.delete("/delete")
async def delete_from_hashmap(key: str):
    try:
        hash_map.delete(key)
        return {
            'message': f'{key} was deleted from the hashmap',
            'current': hash_map.items()
        }
    except Exception as e:
        return {'error': str(e)}


@hash_map_router.get("/search")
async def search_in_hashmap(key: str):
    try:
        value = hash_map.get(key)
        return {
            'found': True,
            'key': key,
            'value': value
        }
    except Exception as e:
        return {
            'found': False,
            'message': str(e)
        }


@hash_map_router.get("/get-items", response_model=HashMapResponse)
async def get_items():
    return {
        "size": len(hash_map.hashmap),
        "data": hash_map.items()
    }


@hash_map_router.get("/clear")
async def reset():
    hash_map.reset()
    return {'message': 'Hashmap has been cleared'}
