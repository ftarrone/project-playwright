    import json

 

def create_json(element_search,page,lista):  

   

    page = page

    links = page.locator(f'{element_search}')

    count = links.count()

    for i in range(count):

   

        # html = elements.nth(i).inner_html()

        # text = elements.nth(i).text_content()

        link = links.nth(i).text_content()

       

        elements_search = links.nth(i)

        identify_id = elements_search.get_attribute('id')

        identify_class = elements_search.get_attribute('class')    

        identify_title = elements_search.get_attribute('title')

 

        try:

            if identify_id != None:

                identify = 'id'

                name_identify = identify_id

            elif identify_class != None:

                identify = 'class'

                name_identify = identify_class

            else:

                identify = 'title'

                name_identify = identify_title

        except ValueError:

            identify = 'error'

       

        # print(f'{element_search}:{identify_id}:{identify_class}:{identify_title}')

 

        if link != '':

            link1 = link.split(',')[-1]

            link1 = link1.strip()

            link1 = link1.replace('\n','')

            link1 = link1.replace('\t','')

            link1 = link1.replace('|','')

         

               

        element_arr = {

            "index"         : f'{i}',

            "name_element"  : f'{link1}',

            "type_element"  : f'{element_search}',

            "identify"      : f'{identify}',

            "name_identify" : f'{identify_class}',

            "description"   : f'testando'

        }

 

       

        lista.append(element_arr)

    return lista