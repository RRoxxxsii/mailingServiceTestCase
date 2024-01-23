import datetime

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_create_mailing(api_client: APIClient, celery_fixture) -> None:
    url = reverse("create_mailing")
    data = {
        "started_at": datetime.datetime(2024, 1, 23, 10, 10),
        "finished_at": datetime.datetime(2024, 1, 23, 10, 10) + datetime.timedelta(hours=5),
        "message": "message",
        "filter": '{"tag": "10"}',
    }
    response = api_client.post(url, data=data)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_list_mailing(api_client: APIClient) -> None:
    url = reverse("list_mailing")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
