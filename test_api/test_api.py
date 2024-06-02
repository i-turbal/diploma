import pytest
import requests

import allure

from test_api.headers import HEADERS
from test_api.pet_model import PetModel, Tag
from test_api.upload_file_model import UploadModel
from test_api.urls import PET_URL


class TestPetApi:

    @allure.title("Test create pet")
    @allure.description("POST api test checks creating pet")
    @allure.suite("API tests")
    def test_create_pet(self, pet_data):
        post_response = requests.post(
            url=PET_URL,
            headers={"accept": "application/json",
                     "Content-Type": "application/json"},
            json=pet_data
        )
        assert post_response.status_code == 200
        response_date = post_response.json()

    @allure.title("Test find pet")
    @allure.description("GET api test finds created  pet")
    @allure.suite("API tests")
    def test_find_created_pet(self, pet_data):
        get_response = requests.get(
            url=f'{PET_URL}/47096',
            headers={"accept": "application/json",
                     "Content-Type": "application/json"},
        )
        assert get_response.status_code == 200
        assert pet_data == get_response.json()

    @allure.title("Test upload photo")
    @allure.description("POST api test tries to upload file ")
    @allure.suite("API tests")
    def test_upload_photo(self, upload_file):
        post_response = requests.post(
            url=f'{PET_URL}/47096/uploadImage',
            headers={"accept": "application/json"},
            files=upload_file
        )
        response_data = post_response.json()
        response_model: UploadModel = UploadModel(**response_data)
        assert response_model.code == 200
        assert "File uploaded to" in response_model.message

    @allure.title("Test update put pet")
    @allure.description("Put api test updates created pet ")
    @allure.suite("API tests")
    @pytest.mark.xfail
    def test_update_pet(self, update_pet_data, get_updated_data):
        """

        :param update_pet_data:
        :update pet name, and tag name
        """
        put_response = requests.put(
            url=PET_URL,
            headers={"accept": "application/json",
                     "Content-Type": "application/json"},
            json=update_pet_data
        )
        assert put_response.status_code == 200
        response_updated_data = put_response.json()
        response_model_put: PetModel = PetModel(**response_updated_data)
        updated_name = response_model_put.name
        get_name = get_updated_data
        assert updated_name == get_name

    @allure.title("Test filter ")
    @allure.description("Get api test filters by pending status ")
    @allure.suite("API tests")
    def test_find_by_status(self,update_pet_data):
        get_response = requests.get(
            url=f"{PET_URL}/findByStatus?status=pending",
            headers={"accept": "application/json",
                     "Content-Type": "application/json"}
        )
        response = get_response.json()
        assert get_response.status_code == 200
        result_of_search = False
        for pet in response:
            if pet['id'] == update_pet_data["id"]:
                if pet["status"] == update_pet_data["status"]:
                    result_of_search = True
                    break
        assert result_of_search

    @allure.title("Test update name and status of pet ")
    @allure.description("Post api test updated name and status ")
    @allure.suite("API tests")
    @pytest.mark.xfail
    def test_update_name_and_status(self, update_status_and_name_data, get_updated_data, get_updated_status):
        post_response = requests.post(
            url=f"{PET_URL}/47096",
            headers={"accept": "application/json",
                     "Content-Type": "application/x-www-form-urlencoded"},
            data=update_status_and_name_data
        )
        assert post_response.status_code == 200
        assert update_status_and_name_data["name"] == get_updated_data
        assert update_status_and_name_data["status"] == get_updated_status

