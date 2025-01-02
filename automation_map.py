from playwright.sync_api import sync_playwright

import json

import time

import create_json

import interaction

 

requests = []  # Array de todoas as requests

disparos = []

links_data = []

lista  = []        

 

def run(playwright):

 

   

    url = 'https://banco.bradesco/investir/' #''''input(f"Digite URl: ")''''

    elements_search = ['a','button']

    browser = playwright.chromium.launch(headless=True)

    context = browser.new_context()

    page = context.new_page()

 

    # Coleta todas as requests Realizadas

    page.on("request", lambda request: requests.append(request))

    page.goto(url)

    time.sleep(8)

    elements = page.locator('*')

   

    # Realiza a criação do .json, com todos os elementos da página selecionados.

    for e in elements_search:

        create_json.create_json(e,page,lista)

    with open('files/datalayer_full.json','w', encoding='utf-8') as file:

        json.dump(lista,file,indent=2,ensure_ascii=False)

 

    # Realiza a Interação com os elementos guardado no .json

    with open('files/datalayer_full.json','r', encoding='utf-8') as file:

        dados_interacao = json.load(file)

    interaction.interaction(dados_interacao,page)

 

with sync_playwright() as playwright:

    run(playwright)