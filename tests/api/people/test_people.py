import allure
import pytest


class TestPeopleResource:
    @allure.title('Check /people endpoint')
    @pytest.mark.api
    def test_positive(self, resource):
        with allure.step('Verify /people'):
            resource.people.get_people()

    @allure.title('Check /people endpoint pagination')
    @pytest.mark.api
    def test_pagination(self, resource):
        with allure.step('Verify /people pagination'):
            resource.people.check_pagination()
