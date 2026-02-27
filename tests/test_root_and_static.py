def test_root_redirect(client):
    # Arrange: none

    # Act
    response = client.get("/", allow_redirects=False)

    # Assert
    assert response.status_code in (301, 302, 307)
    assert response.headers.get("location") == "/static/index.html"
