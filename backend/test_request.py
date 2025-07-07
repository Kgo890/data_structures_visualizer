import httpx

base_url = "http://127.0.0.1:8000"

def print_response(response):
    print(f"Status code: {response.status_code}")
    print(f"Response text: {response.text}")
    try:
        print("JSON:", response.json())
    except Exception as e:
        print(f"Failed to parse JSON: {e}")

def test_all_routes():
    endpoints = {
        "Stack": [
            ("POST", "/stack/", {"value": 10}),
            ("POST", "/stack/", {"value": 8}),
            ("POST", "/stack/", {"value": 12}),
            ("GET", "/stack/peek", None),
            ("GET", "/stack/empty", None),
            ("DELETE", "/stack/", None),
        ],
        "Queue": [
            ("POST", "/queue/", {"value": 20}),
            ("POST", "/queue/", {"value": 32}),
            ("GET", "/queue/peek", None),
            ("DELETE", "/queue/", None),
        ],
        "Sorting": [
            ("POST", "/sort/", {"value": [5, 3, 8, 1], "algorithm": "bubble"}),
            ("POST", "/sort/", {"value": [5, 3, 8, 1], "algorithm": "selection"}),
            ("POST", "/sort/", {"value": [5, 3, 8, 1], "algorithm": "insertion"}),
            ("POST", "/sort/", {"value": [5, 3, 8, 1], "algorithm": "quick"}),
            ("POST", "/sort/", {"value": [5, 3, 8, 1], "algorithm": "merge"}),
        ],
        "Singly Linked List": [
            ("POST", "/singly-linked-list/add-head", {"value": 1}),
            ("POST", "/singly-linked-list/add-tail", {"value": 2}),
            ("GET", "/singly-linked-list/traverse", None),
            ("DELETE", "/singly-linked-list/", {"value": 2}),
        ],
        "Doubly Linked List": [
            ("POST", "/double-linked-list/add-head", {"value": 1}),
            ("POST", "/double-linked-list/add-tail", {"value": 2}),
            ("GET", "/double-linked-list/forward-traverse", None),
            ("GET", "/double-linked-list/reverse-traverse", None),
            ("DELETE", "/double-linked-list/", {"value": 2}),
        ],
        "Binary Tree": [
            ("POST", "/binary-tree/insert", {"value": 50}),
            ("POST", "/binary-tree/insert", {"value": 30}),
            ("POST", "/binary-tree/insert", {"value": 70}),
            ("GET", "/binary-tree/in_order-traverse", None),
            ("GET", "/binary-tree/pre_order-traverse", None),
            ("GET", "/binary-tree/post_order-traverse", None),
            ("GET", "/binary-tree/height", None),
            ("GET", "/binary-tree/search", {"value": 30}),
            ("DELETE", "/binary-tree/", {"value": 30}),
        ],
    }

    for name, actions in endpoints.items():
        print(f"\n--- Testing {name} ---")
        for method, route, data in actions:
            try:
                if method == "POST":
                    res = httpx.post(base_url + route, json=data)
                elif method == "GET":
                    res = httpx.get(base_url + route, params=data)
                elif method == "DELETE":
                    res = httpx.delete(base_url + route, params=data)
                else:
                    continue
                print_response(res)
            except Exception as e:
                print(f"Request failed: {e}")

if __name__ == "__main__":
    test_all_routes()
