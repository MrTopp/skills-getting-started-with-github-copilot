def test_unregister_removes_participant_successfully(client):
    """
    Arrange: Use an email already signed up for Debate Club
    Act: Unregister that participant
    Assert: Participant removed and response confirms success
    """
    # Arrange
    activity = "Debate Club"
    email = "alex@mergington.edu"  # Already in Debate Club participants
    expected_message = f"Unregistered {email} from {activity}"

    # Act
    response = client.post(
        f"/activities/{activity}/unregister",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 200
    result = response.json()
    assert result["message"] == expected_message


def test_unregister_reflects_in_activities_list(client):
    """
    Arrange: Get initial participant list for Science Olympiad
    Act: Unregister a participant, then fetch activities
    Assert: Participant removed from activities list
    """
    # Arrange
    activity = "Science Olympiad"
    email = "noah@mergington.edu"  # Already in Science Olympiad

    # Act
    unregister_response = client.post(
        f"/activities/{activity}/unregister",
        params={"email": email}
    )
    activities_response = client.get("/activities")

    # Assert
    assert unregister_response.status_code == 200
    activities = activities_response.json()
    assert email not in activities[activity]["participants"]


def test_unregister_fails_for_nonexistent_activity(client):
    """
    Arrange: Use an invalid activity name
    Act: Try to unregister from a non-existent activity
    Assert: Returns 404 with appropriate error message
    """
    # Arrange
    activity = "Nonexistent Activity"
    email = "student@mergington.edu"

    # Act
    response = client.post(
        f"/activities/{activity}/unregister",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 404
    result = response.json()
    assert result["detail"] == "Activity not found"


def test_unregister_fails_for_non_participant(client):
    """
    Arrange: Use an email not signed up for Basketball Team
    Act: Try to unregister that email
    Assert: Returns 404 with not-signed-up error
    """
    # Arrange
    activity = "Basketball Team"
    email = "notasignup@mergington.edu"

    # Act
    response = client.post(
        f"/activities/{activity}/unregister",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 404
    result = response.json()
    assert result["detail"] == "Student is not signed up for this activity"
