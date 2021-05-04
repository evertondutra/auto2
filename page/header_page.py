from browser import Browser


class HeaderPage(Browser):
    def preenche_imput_busca(self, texto):
        self.driver.find_element_by_id('id-search-field').send_keys(texto)

    def click_btn_go(self):
        self.driver.find_element_by_id('submit').click()