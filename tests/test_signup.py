def test_signup_adds_participant_successfully(client):
    """
    Arrange: Get initial participant count for Programming Class
    Act: Sign up a new participant
    Assert: Participant added and response confirms success
    """
    # Arrange
    activity = "Programming Class"
    email = "newstudent@mergington.edu"
    expected_message = f"Signed up {email} for {activity}"

    # Act
    response = client.post(
        f"/activities/{activity}/signup",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 200
    result = response.json()
    assert result["message"] == expected_message


def test_signup_reflects_in_activities_list(client):
    """
    Arrange: Get initial participants for Art Class
    Act: Sign up a new student, then fetch activities
    Assert: New participant appears in activities list
    """
    # Arrange
    activity = "Art Class"
    email = "newartist@mergington.edu"

    # Act
    signup_response = client.post(
        f"/activities/{activity}/signup",
        params={"email": email}
    )
    activities_response = client.get("/activities")

    # Assert
    assert signup_response.status_code == 200
    activities = activities_response.json()
    assert email in activities[activity]["participants"]


def test_signup_fails_for_nonexistent_activity(client):
    """
    Arrange: Use an invalid activity name
    Act: Try to sign up for a non-existent activity
    Assert: Returns 404 with appropriate error message
    """
    # Arrange
    activity = "Nonexistent Activity"
    email = "student@mergington.edu"

    # Act
    response = client.post(
        f"/activities/{activity}/signup",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 404
    result = response.json()
    assert result["detail"] == "Activity not found"


def test_signup_fails_for_duplicate_signup(client):
    """
    Arrange: Use an email already signed up for Tennis Club
    Act: Try to sign up that email again
    Assert: Returns 400 with duplicate signup error
    """
    # Arrange
    activity = "Tennis Club"
    email = "isabella@mergington.edu"  # Already in Tennis Club participants

    # Act
    response = client.post(
        f"/activities/{activity}/signup",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 400
    result = response.json()
    assert result["detail"] == "Student already signed up for this activity"
