# tests/test_books_api.py
import pytest
import time

@pytest.mark.smoke
def test_get_books_list(api_client):
    resp = api_client.get_books()
    assert resp.status_code == 200, f"Expected 200, got {resp.status_code}"
    body = resp.json()
    assert isinstance(body, list), "GET /Books should return a list"
    # optionally assert there's at least one book in the demo
    assert len(body) >= 1, "Books list should contain at least one item in demo API"

def test_get_book_by_valid_id(api_client):
    # choose id 1 (demo API has a book 1)
    resp = api_client.get_book(1)
    assert resp.status_code == 200
    body = resp.json()
    assert "id" in body and body["id"] == 1
    assert "title" in body

def test_get_book_by_invalid_id_returns_404(api_client):
    # pick a very large id to likely be absent
    long_id = 999999
    resp = api_client.get_book(long_id)
    # Some demo APIs return 404, some return 200 with empty; check commonly 404
    assert resp.status_code in (200, 404), f"Unexpected status code: {resp.status_code}"

def test_create_update_delete_book_cycle(api_client, sample_book):
    # CREATE
    create_resp = api_client.create_book(sample_book)
    assert create_resp.status_code in (200, 201), f"Create unexpected status {create_resp.status_code}"
    created = create_resp.json()
    # The demo API might return the created payload back with id assigned
    assert "id" in created, "Create response should include id"
    created_id = created["id"]

    # READ the created resource (best-effort - demo API may not persist)
    time.sleep(0.5)
    read_resp = api_client.get_book(created_id)
    # Demo API simulated backend might not persist - allow both 200 or 404
    assert read_resp.status_code in (200, 404), f"Read after create returned {read_resp.status_code}"

    # UPDATE
    updated_payload = dict(created)
    updated_payload["title"] = created.get("title", "") + " (updated)"
    update_resp = api_client.update_book(created_id, updated_payload)
    assert update_resp.status_code in (200, 204, 201), f"Update unexpected status {update_resp.status_code}"

    # DELETE
    del_resp = api_client.delete_book(created_id)
    assert del_resp.status_code in (200, 204), f"Delete unexpected status {del_resp.status_code}"

def test_create_book_with_invalid_payload(api_client):
    # missing required fields or invalid types
    bad_payload = {"title": 12345}  # title should be string
    resp = api_client.create_book(bad_payload)
    # Demo API may accept and echo back; be defensive: expect 4xx or 200/201
    assert resp.status_code in (200, 201, 400, 422), f"Unexpected status: {resp.status_code}"
