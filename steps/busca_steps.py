from behave import given, when, then
from utils import Utils
from page.header_page import HeaderPage

utils = Utils()
header_page = HeaderPage()


@given(u'que acesso o site do python')
def step_impl(context):
    utils.navegar('https://www.python.org/')


@given(u'preencho o imput de pesquisa')
def step_impl(context):
    header_page.preenche_imput_busca('Python')

@when(u'clico no botão de pesquisar')
def step_impl(context):
    header_page.click_btn_go()


@then(u'devo visualizar o resultado da pesquisa')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then devo visualizar o resultado da pesquisa')

