from backend.models.tries import Trie
from fastapi import APIRouter
from backend.schemas.tries_schema import TriesItems, AdvancedMatchRequest

tries_router = APIRouter(
    prefix="/tries",
    tags=["Tries"]
)

tries = Trie()


@tries_router.post("/add")
async def adding_to_trie(item: TriesItems):
    tries.add(item.value)
    return {
        'message': f'"{item.value}" was added to the trie',
        'current': tries.items()
    }


@tries_router.delete("/delete")
async def delete_from_trie(word: str):
    try:
        tries.delete(word)
        return {
            'message': f'"{word}" was deleted from the trie',
            'current': tries.items()
        }
    except Exception as e:
        return {'error': str(e)}


@tries_router.get("/find-match")
async def find_matches_in_trie(item: AdvancedMatchRequest):
    try:
        value = tries.find_matches(item.document)
        return {
            'found': True,
            'document': item.document,
            'matches': value
        }
    except Exception as e:
        return {
            'found': False,
            'message': str(e)
        }


@tries_router.get("/advanced-find-match")
async def find_advanced_matches_in_trie(item: AdvancedMatchRequest):
    try:
        value = tries.advanced_find_matches(item.document, item.variations)
        return {
            'found': True,
            'document': item.document,
            'matches': value
        }
    except Exception as e:
        return {
            'found': False,
            'message': str(e)
        }


@tries_router.get("/search")
async def search_in_trie(word: str):
    try:
        found = tries.search(word)
        return {
            'found': found,
            'word': word
        }
    except Exception as e:
        return {
            'found': False,
            'message': str(e)
        }


@tries_router.get("/prefix-search")
async def prefix_search_in_trie(prefix: str):
    try:
        found = tries.prefix_search(prefix)
        return {
            'found': found,
            'prefix': prefix
        }
    except Exception as e:
        return {
            'found': False,
            'message': str(e)
        }


@tries_router.get("/get-items")
async def get_items():
    return {
        "items": tries.items()
    }


@tries_router.get("/clear")
async def reset():
    tries.reset()
    return {'message': 'Trie has been cleared'}
