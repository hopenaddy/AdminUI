import pytest

@pytest.mark.django_db
class TestUsers:

    def test_view_all_users(self, client):
    	response = client.get('/users/')
    	assert response.status_code == 200

    def test_view_add_user(self, client):
    	response = client.get('/users/add/')
    	assert response.status_code == 200