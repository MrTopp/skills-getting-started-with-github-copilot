def test_root_redirects_to_index(client):
    """
    Arrange: No setup needed
    Act: Request GET /
    Assert: Redirects to /static/index.html with 307 status
    """
    # Arrange
    # (no explicit setup)

    # Act
    response = client.get("/", follow_redirects=False)

    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"
