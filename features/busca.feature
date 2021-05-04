   # language: pt

     Funcionalidade: fluxo de busca

       @busca
       Cenario: realizar busca
         Dado que acesso o site do python
         E preencho o imput de pesquisa
         Quando clico no botão de pesquisar
         Então devo visualizar o resultado da pesquisa
         