from behave import given, when, then
from selenium import webdriver


@given(u'que acesso o site do python')
def step_impl(context):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.python.org/')


@given(u'preencho o imput de pesquisa')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given preencho o imput de pesquisa')


@when(u'clico no botão de pesquisar')
def step_impl(context):
    raise NotImplementedError(u'STEP: When clico no botão de pesquisar')


@then(u'devo visualizar o resultado da pesquisa')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then devo visualizar o resultado da pesquisa')

