from pages.main_paige import MainPage
from utils.assert_that import AssertThat


class BBCPage(MainPage):

    def open(self):
        self.driver.get("https://www.bbc.co.uk")

    def check_site_title(self):
        current_title = self.driver.title
        expected_title = "BBC - Home"
        AssertThat(current_title).equal_to(
                expected_title, f"Page  title: #{current_title} is not equal to #{expected_title}")

