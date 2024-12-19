from playwright.sync_api import sync_playwright

import json

import time

 

requests = []  # Array de todoas as requests

disparos = []

  # Cria arquivo .json, com todas as collects disparadas.

def disparo_collect():

        for request in requests:

                file_name = request.url.split("/")[-1]    

                collect = file_name.find("collect")

                if collect == 0:

                    file_name = file_name.split("&")

                    disparos.append(file_name)

                json_disparos = json.dumps(disparos)

        with open("collect.json","w") as file:

            json.dump(disparos , file, indent=4)

 

def run(playwright):

 

    url = 'https://banco.bradesco/investir/' #''''input(f"Digite URl: ")''''

 

    browser = playwright.chromium.launch(headless=True)

    context = browser.new_context()

    page = context.new_page()

 

   

   

    element_arr = []

    links_data = []

 

    # Coleta todas as requests Realizadas

    page.on("request", lambda request: requests.append(request))

    page.goto(url)

   

    time.sleep(8)

 

    elements = page.locator('*')    

    # count = elements.count()

    links = page.locator('a')

    count = links.count()

    #button = page.locator('button')

 

    for i in range(count):

        html = elements.nth(i).inner_html()

        text = elements.nth(i).text_content()

        link = links.nth(i).text_content()

        i+=1

        if link != '':

            link1 = link.split(',')[-1]

            link1 = link1.replace('\n','')

            link1 = link1.replace('\t','')

            link1 = link1.replace('|','')

            element_arr.append(link1)

 

    links_count = len(element_arr)

   

    for i in range(links_count):

        contar = element_arr[i].find('Especialistas de Investimentos')

        if contar == 0:

         

            click_link = page.locator(f'text={element_arr[i]}')

            click_link.click()

            data_layer = page.evaluate("window.dataLayer || []")

 

            for item in data_layer:

                if 'event' in item:

                    for key, value in item.items():

                        if value == 'Event_Data':

                            print(f"DataLayer : {item}")

                            links_data.append(item)

                        links_data_json = json.dumps(links_data)

            with open("dataLayer.json","w", encoding="utf-8") as file:

                json.dump(links_data,file, indent=4)

           

            disparo_collect()

 

                       

       

   

 

with sync_playwright() as playwright:

    run(playwright)