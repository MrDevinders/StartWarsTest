from common.common_methods import CommonMethods
from selenium.webdriver.common.by import By

class HomePage(CommonMethods):

    lblTitle = (By.XPATH, "//th[text()='Title']")
    tblRows = "//tr"
    tblLastRowData = "((//tr)[<LAST>]/child::td)[1]/child::a"

    lblMovieTheEmpire = (By.XPATH, "//a[text()='The Empire Strikes Back']")
    lblMovieThePhantom = (By.XPATH, "//a[text()='The Phantom Menace']")

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def sortTitle(self):
        self.webelement_click(self.lblTitle)

    def lastMovie(self):
        moviesCount = len(self.driver.find_elements(By.XPATH, self.tblRows))
        self.tblLastRowData = self.tblLastRowData.replace("<LAST>", str(moviesCount))
        lastMovieTitle = self.driver.find_element(By.XPATH, self.tblLastRowData)
        return lastMovieTitle.text

    def click_movie_theEmpire(self):
        self.webelement_click(self.lblMovieTheEmpire)

    def click_movie_thePhantom(self):
        self.webelement_click(self.lblMovieThePhantom)
