from random import randint

import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory

@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory

@pytest.mark.django_db
def test_get_course(client, course_factory):
    course = course_factory(_quantity=1)
    response = client.get(f"/api/v1/courses/{course[0].id}/")

    assert response.status_code == 200
    data = response.json()
    assert data['name'] == course[0].name

@pytest.mark.django_db
def test_get_list_courses(client, course_factory):
    courses = course_factory(_quantity=10)
    response = client.get("/api/v1/courses/")

    assert response.status_code == 200
    data = response.json()
    for i, n in enumerate(data):
        assert n['name'] == courses[i].name

@pytest.mark.django_db
def test_filtering_courses_by_id(client, course_factory):
    courses = course_factory(_quantity=10)
    courses_id = randint(0, 9)
    response = client.get("/api/v1/courses/", data = {'id': courses[courses_id].id})

    assert response.status_code == 200

    data = response.json()
    assert data[0]['name'] == courses[courses_id].name

@pytest.mark.django_db
def test_filtering_courses_by_name(client, course_factory):
    courses = course_factory(_quantity=10)
    courses_id = randint(0, 9)
    response = client.get("/api/v1/courses/", data = {'name': courses[courses_id].name})

    assert response.status_code == 200

    data = response.json()
    assert data[0]['name'] == courses[courses_id].name

@pytest.mark.django_db
def test_create_course(client):
    count_courses = Course.objects.count()
    response = client.post("/api/v1/courses/", data={"name": "Математика"})

    assert response.status_code == 201
    assert Course.objects.count() == count_courses + 1

@pytest.mark.django_db
def test_update_course(client):
    response_create = client.post("/api/v1/courses/", data={"name": "Математика"})
    response_update = client.patch(f"/api/v1/courses/{response_create.json()['id']}/", data={"name": "Химия"})

    assert response_update.status_code == 200

    assert response_update.json()['name'] == Course.objects.get(id=response_create.json()['id']).name

@pytest.mark.django_db
def test_delete_course(client, course_factory):
    course = course_factory(_quantity=1)
    count = Course.objects.count()

    response = client.delete(f"/api/v1/courses/{course[0].id}/")

    assert response.status_code == 204

    assert Course.objects.count() == count - 1

