import pytest
from conftest import *
from pageObjects.HomePage import HomePage
from pageObjects.MoviesPage import MoviesPage

@pytest.mark.usefixtures("browser_setup")
class Test_ViewMovie_CheckSpecies:

    Species = "Wookie"

    def setup_class(self):
        self.driver.get(BaseUrl)
        self.driver.implicitly_wait(ImplicitWait)
        self.home_page = HomePage(self.driver)
        self.movies_page = MoviesPage(self.driver)

    @pytest.mark.web
    def test_ViewMovieTheEmpire(self):
        self.home_page.click_movie_theEmpire()

    @pytest.mark.web
    def test_CheckSpeciesWookie(self):
        print(self.Species)
        assert self.movies_page.findSpecies(self.Species) == True

    def teardown_class(self):
        self.driver.quit()