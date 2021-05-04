# Aqui se reuneos comandos que se usa com maior frequencia
from browser import Browser


class Utils(Browser):
    def navegar(self, url):
        self.driver.get(url)
