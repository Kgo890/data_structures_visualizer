from backend.models.sorting import selection_sort, insertion_sort, quick_sort, merge_sort, bubble_sort
from fastapi import APIRouter
from backend.schemas.sorting_schema import SortItem

sorting_router = APIRouter(
    prefix="/sort",
    tags=["Sort"]
)


@sorting_router.post("/")
async def sorting_algorithm(item: SortItem):
    if item.algorithm == "selection":
        steps = selection_sort(item.value)
        return {"original": item.value, "steps": steps}

    elif item.algorithm == "insertion":
        steps = insertion_sort(item.value)
        return {"original": item.value, "steps": steps}

    elif item.algorithm == "quick":
        steps = quick_sort(item.value, 0, len(item.value) - 1)
        return {"original": item.value, "steps": steps}

    elif item.algorithm == "merge":
        steps = merge_sort(item.value)
        return {"original": item.value, "steps": steps}

    elif item.algorithm == "bubble":
        steps = bubble_sort(item.value)
        return {"original": item.value, "steps": steps}

    else:
        return {'error': f'{item.algorithm} was not added to the program yet or not found'}
