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


def run_all():
    test_stack()


if __name__ == "__main__":
    run_all()
