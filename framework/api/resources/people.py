import allure

from framework.api.base.base_api import BaseApi
from framework.api.response_models.people import PeopleResponse


class PeopleResource(BaseApi):
    def get_people(self):
        response = self.get('/people', PeopleResponse)
        return response

    def check_pagination(self):
        people = self.get_people()
        total_count = people.count
        expected_results_per_page = 10

        expected_pages_quantity = total_count // expected_results_per_page
        if total_count % expected_results_per_page:
            expected_pages_quantity += 1

        for current_page in range(expected_pages_quantity):
            current_page += 1

            with allure.step(f'Check page {current_page}'):
                if current_page == 1:
                    with allure.step('Check empty previous page link'):
                        assert not people.previous
                    with allure.step('Check correct next page link'):
                        assert str(people.next) == self.build_url(f'/people/?page=2')
                    with allure.step('Check correct results per page'):
                        assert len(people.results) == expected_results_per_page
                elif current_page == expected_pages_quantity:
                    with allure.step('Check correct previous page link'):
                        assert str(people.previous) == self.build_url(f'/people/?page={expected_pages_quantity - 1}')
                    with allure.step('Check empty next page link'):
                        assert not people.next
                    with allure.step('Check correct results per page'):
                        assert len(people.results) == total_count % expected_results_per_page
                    return
                else:
                    with allure.step('Check correct previous page link'):
                        assert str(people.previous) == self.build_url(f'/people/?page={current_page - 1}')
                    with allure.step('Check correct next page link'):
                        assert str(people.next) == self.build_url(f'/people/?page={current_page + 1}')
                    with allure.step('Check correct results per page'):
                        assert len(people.results) == expected_results_per_page

                with allure.step('Open next page'):
                    people = self.get(str(people.next), response_model=PeopleResponse)
