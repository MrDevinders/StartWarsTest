import pytest
from conftest import *
from pageObjects.HomePage import HomePage

@pytest.mark.usefixtures("browser_setup")
class Test_SortTitle_AssertLastMovie:

    LastMovie = "The Phantom Menace"

    def setup_class(self):
        self.driver.get(BaseUrl)
        self.home_page = HomePage(self.driver)

    @pytest.mark.web
    def test_SortTitle(self):
        self.home_page.sortTitle()

    @pytest.mark.web
    def test_CheckLastMovie(self):
        print(self.LastMovie)
        assert self.home_page.lastMovie() == self.LastMovie

    def teardown_class(self):
        self.driver.quit()