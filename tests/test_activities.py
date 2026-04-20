def test_get_activities_returns_all_activities(client):
    """
    Arrange: No setup needed (activities preseeded)
    Act: Request GET /activities
    Assert: Returns dict with at least 9 activities and correct structure
    """
    # Arrange
    expected_activity_count = 9

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    activities = response.json()
    assert len(activities) == expected_activity_count
    assert isinstance(activities, dict)


def test_get_activities_has_correct_structure(client):
    """
    Arrange: No setup needed
    Act: Request GET /activities
    Assert: Each activity has required fields with correct types
    """
    # Arrange
    required_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")
    activities = response.json()

    # Assert
    assert response.status_code == 200
    for activity_name, activity_data in activities.items():
        assert isinstance(activity_name, str)
        assert set(activity_data.keys()) == required_fields
        assert isinstance(activity_data["description"], str)
        assert isinstance(activity_data["schedule"], str)
        assert isinstance(activity_data["max_participants"], int)
        assert isinstance(activity_data["participants"], list)


def test_get_activities_chess_club_has_participants(client):
    """
    Arrange: No setup needed
    Act: Request GET /activities
    Assert: Chess Club activity exists and has initial participants
    """
    # Arrange
    expected_activity = "Chess Club"

    # Act
    response = client.get("/activities")
    activities = response.json()

    # Assert
    assert response.status_code == 200
    assert expected_activity in activities
    assert len(activities[expected_activity]["participants"]) > 0
