 # Cria arquivo .json, com todas as collects disparadas.

def disparo_collect(type_event):

 

        type_event = type_event

        print(type_event)

        for request in requests:

                file_name = request.url.split("/")[-1]    

                collect = file_name.find("collect")

                if collect == 0:

                    file_name = file_name.split("&")

                    disparos.append(file_name)

                json_disparos = json.dumps(disparos)

        with open("collect.json","w") as file:

            json.dump(disparos , file, indent=4)