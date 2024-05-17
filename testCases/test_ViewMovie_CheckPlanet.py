import pytest
from conftest import *
from pageObjects.HomePage import HomePage
from pageObjects.MoviesPage import MoviesPage

@pytest.mark.usefixtures("browser_setup")
class Test_ViewMovie_CheckSpecies:

    Planet = "Camino"

    def setup_class(self):
        self.driver.get(BaseUrl)
        self.driver.implicitly_wait(ImplicitWait)
        self.home_page = HomePage(self.driver)
        self.movies_page = MoviesPage(self.driver)
    
    @pytest.mark.web
    def test_ViewMovieThePhantom(self):
        self.home_page.click_movie_thePhantom()

    @pytest.mark.web
    def test_CheckSpeciesWookie(self):
        print(self.Planet)
        assert self.movies_page.findPlanet(self.Planet) == False

    def teardown_class(self):
        self.driver.quit()