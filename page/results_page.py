from browser import Browser


class ResultsPage(Browser):
    def get_text_title(self):
        return self.driver.find_element_by_class_name('main-content h2').text
