import pytest
import requests

from test_api.pet_model import PetModel
from test_api.urls import PET_URL


@pytest.fixture
def pet_data():
    pet_data = {
        "id": 47096,
        "category": {
            "id": 1,
            "name": "cat"
        },
        "name": "tux",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "cat"
            }
        ],
        "status": "pending"
    }
    return pet_data


@pytest.fixture()
def upload_file():
    upload_file = {"file": open("cat1.jpeg", 'rb')}
    return upload_file


@pytest.fixture()
def update_pet_data():
    update_pet_data = {
        "id": 47096,
        "category": {
            "id": 1,
            "name": "cat"
        },
        "name": "Tuhtasun",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "hairless cat"
            }
        ],
        "status": "pending"
    }
    return update_pet_data


@pytest.fixture()
def update_status_and_name_data():
    updated_data = {"name": "tuxtasu nekaterinovic",
                    "status": "available"}
    return updated_data


@pytest.fixture()
def get_updated_data():
    get_response = requests.get(
        url=f'{PET_URL}/47096',
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
    )
    response_data = get_response.json()
    response_model: PetModel = PetModel(**response_data)
    cat_name = response_model.name
    return cat_name


@pytest.fixture()
def get_updated_status():
    get_response = requests.get(
        url=f'{PET_URL}/47096',
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
    )
    response_data = get_response.json()
    response_model: PetModel = PetModel(**response_data)
    pet_status = response_model.status
    return pet_status
