import json
links_data = []
dataLayer_json = []

def capturar_datalayer(data_layer):
    for item in data_layer:
        if 'event' in item:
            for key, value in item.items():
                if value == 'Event_Data':
                    event_item = item
                    print(event_item)
                    return event_item


def interaction(dados_interacao,page):

    
    # print(dados_interacao)
    for item in dados_interacao:
        name_elements   = item["name_element"] 
        type_elements   = item["type_element"] 
        name_identify   = item["name_identify"] 
        identify        = item["identify"] 
        print(f'{identify}:{name_elements}:{type_elements}:{name_identify}')
        try:
            if identify == "class" and name_identify != "undefined" :
                # print(f'{name_elements}:{type_elements}:{identify}')
                click_selector = (f'{type_elements}.{name_identify}')
                print(click_selector)
                page.wait_for_selector(click_selector,timeout=5000)
                page.click(click_selector)
                data_layer = page.evaluate("window.dataLayer || []")
                event_item = capturar_datalayer(data_layer)

                dataLayer_arr = {
                    "index" : f"{item}",
                    "name_element"  : f"{name_elements}",
                    "type_element"  : f"{type_elements}",
                    "datalayer"     : f"{event_item}",
                    "error"         : f"None"
                }

            elif identify == "id" and name_identify != "undefined" :
                # print(f'{name_elements}:{type_elements}:{identify}')
                click_selector = (f'{type_elements}#{name_identify}')
                print(click_selector)
                page.wait_for_selector(click_selector,timeout=5000)
                page.click(click_selector)
                data_layer = page.evaluate("window.dataLayer || []")
                event_item = capturar_datalayer(data_layer)

                dataLayer_arr = {
                    "index" : f"item",
                    "name_element"  : f"{name_elements}",
                    "type_element"  : f"{type_elements}",
                    "datalayer"     : f"{event_item}",
                    "error"         : f"None"
                }

                dataLayer_json.append(dataLayer_arr)

        except Exception as e:
            print(f'Erro foi : {e}')
        
            dataLayer_arr = {
                "index" : f"item",
                "name_element"  : f"{name_elements}",
                "type_element"  : f"{type_elements}",
                "datalayer"     : f"None",
                "error"         : f"{e}\n"
            }

            dataLayer_json.append(dataLayer_arr)
    # links_data_json = json.dumps(links_data)    
    with open("validacao_datalayer.json","w",) as file:
        json.dump(dataLayer_json,file, indent=4)    



