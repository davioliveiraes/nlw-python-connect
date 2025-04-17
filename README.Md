<h1 align="center">NLW Connect trilha de Python da Rocketseat</h1>

<p align="center">
  <a href="#-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-projeto">Projeto</a>&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;
  <a href="#-principais-bibliotecas">Principais Bibliotecas</a>&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp
  <a href="#-Para-executar-o-projeto">Para executar o projeto</a>
</p>

## 🚀 Tecnologias

Esse projeto foi desenvolvido com as seguintes tecnologias:

- Python
- Flask

## 📚 Principais Bibliotecas

- blinker==1.9.0
- Cerberus==1.3.7
- click==8.1.8
- colorama==0.4.6
- distlib==0.3.9
- filelock==3.17.0
- Flask==3.1.0
- greenlet==3.1.1
- iniconfig==2.0.0
- itsdangerous==2.2.0
- Jinja2==3.1.5
- MarkupSafe==3.0.2
- packaging==24.2
- platformdirs==4.3.6
- pluggy==1.5.0
- pytest==8.3.4
- SQLAlchemy==2.0.38
- typing_extensions==4.12.2
- virtualenv==20.29.2
- Werkzeug==3.1.3


## 💻 Projeto

  Api de Gestão de Evento foi desenvolvida utilizando Flask e SQLAlchemy para facilitar a administração de eventos e seus participantes. Ela permite a criação e geranciamento de eventos, o registro de inscritos e a geração de links exclusivos para cada evento. A API segue boas práticas de arquitetura, garantindo escalabilidade, segurança e organização.

## 👨‍💻 Para executar o projeto

1. Clone o repositório: `git clone https://github.com/davioliveiraes/nlw-python-connect.git`
2. Entre na pasta do projeto: `cd nlw-python-connect`
3. Ative o ambiente virtual: `source venv/bin/activate (Linux/Ubuntu)`
4. Instale as dependências: `pip3 install -r requirements.txt`
5. Execute o programa: `python3 run.py`
6. Pode baixar o `postman` e executar os seguintes métodos(Exemplo): 
- POST - `http://localhost:3000/event`
- POST - `http://localhost:3000/subscriber`
- GET - `http://localhost:3000/subscriber/link/:link/event/:event_id`
- GET - `http://localhost:3000/subscriber/ranking/event/:event_id`
- POST - `http://localhost:3000/events_link`
