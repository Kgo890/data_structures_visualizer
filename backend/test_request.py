import httpx

base_url = "http://127.0.0.1:8000"


def print_response(response):
    print(f"Status code: {response.status_code}")
    print(f"Response text: {response.text}")
    try:
        print("JSON:", response.json())
    except Exception as e:
        print(f"Failed to parse JSON: {e}")


# --- Stack ---
def test_stack():
    print("\n--- Testing Stack ---")
    r1 = httpx.post(f"{base_url}/stack/", json={"value": 10})
    print_response(r1)

    r2 = httpx.post(f"{base_url}/stack/", json={"value": 8})
    print_response(r2)

    r3 = httpx.post(f"{base_url}/stack/", json={"value": 12})
    print_response(r3)

    r4 = httpx.post(f"{base_url}/stack/", json={"value": 10})
    print_response(r4)

    r5 = httpx.get(f"{base_url}/stack/peek")
    print_response(r5)

    r6 = httpx.get(f"{base_url}/stack/empty")
    print_response(r6)

    r7 = httpx.delete(f"{base_url}/stack/")
    print_response(r7)

    r8 = httpx.delete(f"{base_url}/stack/")
    print_response(r8)

    r9 = httpx.delete(f"{base_url}/stack/")
    print_response(r9)

    r10 = httpx.delete(f"{base_url}/stack/")
    print_response(r10)

    r11 = httpx.delete(f"{base_url}/stack/")
    print_response(r11)


# --- Queue ---
def test_queue():
    print("\n--- Testing Queue ---")
    r1 = httpx.post(f"{base_url}/queue/", json={"value": 20})
    print_response(r1)

    r2 = httpx.post(f"{base_url}/queue/", json={"value": 32})
    print_response(r2)

    r3 = httpx.post(f"{base_url}/queue/", json={"value": 40})
    print_response(r3)

    r4 = httpx.post(f"{base_url}/queue/", json={"value": 8})
    print_response(r4)

    r5 = httpx.get(f"{base_url}/queue/peek")
    print_response(r5)

    r6 = httpx.delete(f"{base_url}/queue/")
    print_response(r6)

    r7 = httpx.delete(f"{base_url}/queue/")
    print_response(r7)

    r8 = httpx.delete(f"{base_url}/queue/")
    print_response(r8)

    r9 = httpx.delete(f"{base_url}/queue/")
    print_response(r9)

    r10 = httpx.delete(f"{base_url}/queue/")
    print_response(r10)


# --- Sorting ---
def test_sorting():
    print("\n--- Testing Sorting (Bubble) ---")
    r1 = httpx.post(f"{base_url}/sort/", json={"value": [5, 3, 8, 1], "algorithm": "bubble"})
    print_response(r1)
    print("\n--- Testing Sorting (Selection) ---")
    r2 = httpx.post(f"{base_url}/sort/", json={"value": [5, 3, 8, 1], "algorithm": "selection"})
    print_response(r2)
    print("\n--- Testing Sorting (Insertion) ---")
    r3 = httpx.post(f"{base_url}/sort/", json={"value": [5, 3, 8, 1], "algorithm": "insertion"})
    print_response(r3)
    print("\n--- Testing Sorting (Quick) ---")
    r4 = httpx.post(f"{base_url}/sort/", json={"value": [5, 3, 8, 1], "algorithm": "quick"})
    print_response(r4)
    print("\n--- Testing Sorting (Merge) ---")
    r5 = httpx.post(f"{base_url}/sort/", json={"value": [5, 3, 8, 1], "algorithm": "merge"})
    print_response(r5)


# --- Singly Linked List ---
def test_singly_linked_list():
    print("\n--- Testing Singly Linked List ---")

    r1 = httpx.post(f"{base_url}/singly-linked-list/add-head", json={"value": 1})
    print_response(r1)

    r2 = httpx.post(f"{base_url}/singly-linked-list/add-tail", json={"value": 2})
    print_response(r2)

    r3 = httpx.post(f"{base_url}/singly-linked-list/add-tail", json={"value": 3})
    print_response(r3)

    r4 = httpx.post(f"{base_url}/singly-linked-list/add-tail", json={"value": 10})
    print_response(r4)

    r5 = httpx.post(f"{base_url}/singly-linked-list/add-tail", json={"value": 7})
    print_response(r5)

    r6 = httpx.get(f"{base_url}/singly-linked-list/traverse")
    print_response(r6)

    r7 = httpx.get(f"{base_url}/singly-linked-list/search", params={"value": 2})
    print_response(r7)

    r8 = httpx.delete(f"{base_url}/singly-linked-list/", params={"value": 2})
    print_response(r8)

    r9 = httpx.delete(f"{base_url}/singly-linked-list/", params={"value": 99})
    print_response(r9)

    r10 = httpx.get(f"{base_url}/singly-linked-list/traverse")
    print_response(r10)


def test_double_linked_list():
    pass

def test_binary_tree():
    pass

# --- Run Everything ---
def run_all():
    test_stack()
    test_queue()
    test_sorting()
    test_singly_linked_list()


if __name__ == "__main__":
    run_all()
