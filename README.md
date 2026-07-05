# Agenda de Compromissos CLI

Trabalho desenvolvido para a disciplina de Introdução à Programação, ministrada pelo Prof. Olivindo.

Este projeto é uma aplicação de linha de comando em Python para o gerenciamento de compromissos. O sistema conta com persistência de dados, garantindo que as informações cadastradas não sejam perdidas após o encerramento do programa.

## Funcionalidades

O sistema possui um menu interativo com as seguintes operações:

1. Adicionar novo compromisso (inclui validação de dias, meses e anos bissextos).
2. Editar um compromisso existente.
3. Excluir um compromisso.
4. Mostrar o número total de compromissos cadastrados.
5. Filtrar compromissos por palavra-chave presente na descrição.
6. Listar todos os compromissos em ordem cronológica.
7. Listar apenas os compromissos marcados como prioritários.
8. Identificar e exibir o dia com o maior número de compromissos.
9. Filtrar compromissos por uma data exata.
10. Filtrar compromissos dentro de um período específico (data inicial e data final).

## Bibliotecas Utilizadas

O projeto foi construído utilizando apenas bibliotecas padrão do Python, sem necessidade de instalações externas:

- `python 3.13.14`: Linguagem do projeto.
- `shelve`: Utilizada para criar um banco de dados local e salvar os dados em formato de dicionário.
- `os`: Utilizada para executar comandos do sistema operacional, como limpar o terminal (`cls`) e pausar telas.

## Como executar

Certifique-se de ter o Python instalado na sua máquina. Abra o terminal na pasta onde o arquivo está localizado e execute o comando abaixo:

```bash
python agenda_pessoal.py
