from common.common_methods import CommonMethods
from selenium.webdriver.common.by import By

class MoviesPage(CommonMethods):

    lblSpeciesWookie = (By.XPATH, "//h1[text()='Species']/parent::div/following-sibling::ul/child::li[text()='Wookie']")
    lblPlanetsCamino = "//h1[text()='Planets']/parent::div/following-sibling::ul/child::li"

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def findSpecies(self, species):
        return self.webelement_exist(self.lblSpeciesWookie)

    def findPlanet(self, planet):
        eleExists = False

        elePlanets = self.driver.find_elements(By.XPATH, self.lblPlanetsCamino)
        for ele in elePlanets:
            if ele.text == "Camino":
                eleExists = True
                break

        return eleExists