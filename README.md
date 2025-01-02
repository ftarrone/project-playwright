# Projeto de Coleta de Dados com Playwright

Este repositório contém um script em Python que utiliza a biblioteca **Playwright** para automatizar a coleta de dados de uma página da web. O objetivo do script é capturar informações relevantes de requisições realizadas e eventos de *dataLayer*, além de gerar dois arquivos JSON contendo as informações coletadas.

## Descrição

O script realiza as seguintes etapas:

1. **Coleta de Requests**: O script intercepta todas as requisições realizadas pela página durante a navegação.
2. **Coleta de Links**: Ele extrai os links de texto da página e interage com um link específico relacionado a "Especialistas de Investimentos".
3. **Captura de Eventos do dataLayer**: Após clicar no link, ele coleta dados do objeto `dataLayer` da página, que contém eventos JavaScript relacionados a interações do usuário.
4. **Armazenamento de Dados**: Todos os dados coletados são armazenados em dois arquivos JSON:
   - `collect.json`: Contém todas as requisições "collect" disparadas pela página.
   - `dataLayer.json`: Armazena os eventos de interesse extraídos do `dataLayer`.

## Requisitos

- Python 3.7 ou superior
- Bibliotecas:
  - **Playwright**: Para automação do navegador e captura das requisições.
  - **json**: Para manipulação dos dados coletados.
  - **time**: Para pausas entre as ações.

Instale as dependências executando o seguinte comando:

```bash
pip install playwright
```

Além disso, execute o seguinte comando para instalar os navegadores necessários:

```bash
python -m playwright install
```

## Como usar

1. Clone o repositório ou baixe o script Python.
2. Abra o script e edite a URL da página de destino, se necessário.
   ```python
   url = 'https://banco.bradesco/investir/'  # Modifique conforme necessário
   ```
3. Execute o script Python:
   ```bash
   python script.py
   ```
   O Playwright abrirá o navegador, navegará até a URL definida e começará a coletar as requisições e os eventos do `dataLayer`.

4. Ao final da execução, dois arquivos JSON serão gerados:
   - `collect.json`: Contém os dados das requisições "collect".
   - `dataLayer.json`: Contém os eventos do `dataLayer` encontrados na página.

## Estrutura do código

- **Função `disparo_collect()`**: Essa função coleta as requisições "collect" e as salva no arquivo `collect.json`.
- **Função `run(playwright)`**: Realiza a automação da navegação na página e coleta os links, interações e dados do `dataLayer`.

## Personalizações

- Modifique a URL no script para coletar dados de diferentes páginas.
- Se necessário, ajuste o código para interagir com outros elementos da página ou capturar eventos específicos.

## Exemplo de saídas

1. **Arquivo `collect.json`**:
   ```json
   [
       ["collect", "url1", "other_data"],
       ["collect", "url2", "other_data"]
   ]
   ```

2. **Arquivo `dataLayer.json`**:
   ```json
   [
       {
           "event": "Event_Data",
           "category": "Investimentos",
           "action": "click"
       },
       {
           "event": "Event_Data",
           "category": "Especialistas",
           "action": "view"
       }
   ]
   ```

## Considerações Finais

Este script é uma forma de automatizar a coleta de dados a partir de interações e requisições de uma página web. Ele pode ser facilmente modificado para capturar diferentes tipos de dados ou para interagir com outros elementos HTML.
