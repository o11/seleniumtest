from selenium import webdriver


class Github:
    """Get total stars and total repositories of any user"""

    __username = ''
    __password = ''
    __repositories = []
    __stars = []
    __driver = None

    def __init__(self, username, password):
        """Initialize Github class"""
        self.__username = username
        self.__password = password
        self.__base_url = 'https://github.com/'
        self.__login_url = self.__base_url + 'login/'
        self.__stars_url = self.__base_url + self.__username + '?page=1&tab=stars'
        self.__repositories_url = self.__base_url + self.__username + '?page=1&tab=repositories'
        self.__driver = webdriver.Chrome('./chromedriver')

    def login(self):
        """Login to github with given credentials"""
        self.__driver.get(self.__login_url)
        element_form = self.__driver.find_element_by_xpath("//form[@action='/session']")

        element_username = self.__driver.find_element_by_id('login_field')
        element_username.send_keys(self.__username)

        element_password = self.__driver.find_element_by_id('password')
        element_password.send_keys(self.__password)

        element_form.submit()

    def get_repositories(self):
        """:return repositories"""
        self.__driver.get(self.__repositories_url)
        while True:
            try:
                self.__repositories.extend([repo.text for repo in self.__driver.find_elements_by_xpath(
                    "//ul[@data-filterable-for='your-repos-filter']/li/div/h3/a")])
                next_page = self.__driver.find_element_by_xpath("//a[@class='next_page']").get_attribute('href')
                self.__driver.get(url=next_page)
            except:
                break
        return self.__repositories

    def get_stars(self):
        """:return stars"""
        self.__driver.get(self.__stars_url)
        while True:
            try:
                self.__stars.extend([repo.text for repo in self.__driver.find_elements_by_xpath(
                    "//div[@class='col-12 d-block width-full py-4 border-bottom']/div/h3/a")])
                next_page = self.__driver.find_element_by_xpath("//a[@class='next_page']").get_attribute('href')
                self.__driver.get(url=next_page)
            except:
                break
        return self.__stars

    def __del__(self):
        """Destructor of class"""
        self.__driver.close()

    @property
    def username(self):
        """:return username"""
        return self.__username

    @username.setter
    def username(self, value):
        """Setter for username
        If username changes the variables depends on username should also change"""
        self.__username = value
        self.__stars_url = self.__base_url + self.__username + '?page=1&tab=stars'
        self.__repositories_url = self.__base_url + self.__username + '?page=1&tab=repositories'
        self.__repositories = []  # delete repositories of other users
        self.__stars = []  # delete all stars of other users
