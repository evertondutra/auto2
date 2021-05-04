from browser import Browser


class HeaderPageElements(object):
    INPUT_BUSCA = 'id-search-field'


class bot(object):
    BTN_GO = 'submit'


class HeaderPage(Browser):
    def preenche_imput_busca(self, texto):
        self.driver.find_element_by_id(HeaderPageElements.INPUT_BUSCA).send_keys(texto)

    def click_btn_go(self):
        self.driver.find_element_by_id(bot.BTN_GO).click()
