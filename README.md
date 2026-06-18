# API de gerenciamento de tarefas

A task-manager-API é uma solução minimalista e robusta para o gerenciamento de tarefas pessoais. O foco do projeto não é a complexidade das regras de negócio, mas a excelência na implementação técnica. A API permite que usuários autenticados criem, organizem e monitorem suas tarefas diárias com base em prioridades, garantindo total isolamento de dados entre diferentes usuários.

## Tecnologias utilizadas

- Python 3.12.3 (Linguagem adotada)
- Django com DRF(Django REST Framework, Criação da API)
- drf-spectacular (Documentação API, com Swagger UI e ReDoc)
- django-environ (Uso de variáveis ambientes de forma segura)
- django-filter (Configuração para uso de filtros de pesquisa)
- simplejwt (Uso de token para acesso rápido e seguro as endpoints)
- psycopg2-binary (Adaptador para que o Python converse com PostgreSQL)
- gunicorn (Servidor HTTP WSGI)
- pytest (Utilizado para os testes do projeto)
- Docker
- Nginx (Usado para testar o ambiente em produção)

## Baixar repositório 

1. **Clone repositório:**
    ```bash
    git clone https://github.com/Mavegui/task-manager-API.git
    ```

2. **Instale e execute ambiente virtual:**
    Instalar:
    ```bash
    python -m venv .venv
    ```
    
    Executar:
    ```bash
    source .venv/bin/activate
    ```
    
    Desativar:
    ```bash
    deactivate
    ```

3. **Instalar dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure o seu env:**
   
   - Renomeie o arquivo .env.example para .env e preencha as credenciais.

5. **Executar migrate e servidor:**
    ```bash
    python3 manage.py migrate
    python3 manage.py runserver
    ```

6. **OU USE DOCKER IMAGE**
    - Crie a pasta nginx e copie o nginx.conf
    - Configure o seu .env com base no passo 4.
    - Baixe o docker-compose.prod.yml (Imagem da API citada aqui) e execute:
    ```bash
    docker compose -f docker-compose.prod.yml up -d
    ```
    - Executa migrations na primeira vez no banco:
    ```bash
    docker compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
    ```
    - Libera arquivos estáticos para o Nginx:
    ```bash
    docker compose -f docker-compose.prod.yml exec web python manage.py collectstatic --noinput
    ```
Para saber mais, acesse o [Docker Hub do Projeto](https://hub.docker.com/r/mavegui/task_manager_api).

## Arquitetura de Endpoints

As endpoints tem a capacidade de expansão ainda mais, mas foge do escopo do projeto de ser simples, para aprendizado. Exemplo: Endpoint para retornar os dados do usuário (nome, sobrenome, email...)

- **Método para registrar usuário - POST:**

```bash
/api/v1/register/
```

- **Método para obtenção de tokens JWT(Access/Refresh) - POST:**

```bash
/api/v1/auth/token/
```

- **Método para obtenção de novo token, apos expirar o access (Refresh) - POST:**

```bash
/api/v1/auth/token/refresh
```

- **Lista todas as tarefas do usuário logado(com filtros) - GET:**

```bash
/api/v1/tasks/
```

- **Cria nova tarefa - POST:**

```bash
/api/v1/tasks/
```

- **Lista apenas a tarefa selecionada - GET:**

```bash
/api/v1/tasks/{id}/
```

- **Atualiza multiplos campos de uma tarefa selecionada - PUT:**

```bash
/api/v1/tasks/{id}/
```

- **Atualiza apenas um campo da tarefa escolhida - PATCH:**

```bash
/api/v1/tasks/{id}/
```

- **Remove uma tarefa - DELETE:**

```bash
/api/v1/tasks/{id}/
```

## Docker Conteiner, Contexto e Comandos.

O projeto da API foi criado justamente com o objetivo de utilizar boas práticas e ferramentas modernas do desenvolvimento de software, tendo isso em vista foi utilizado o Docker para isolamento em contêineres buscando aprendizado e evolução nesses setores.

### Contêineres do projeto:

- task_manager_api (Imagem Alpine por ser pixuta kkkkk.)
- task_manager_db (Imagem do postgreSQL)

### Comando utilizados:

#### LEMBRETE: Tenha o Docker já devidamente instalado no seu computador, uso Linux. Abordarei em especifíco sobre este sistema e não citarei sobre permissões aqui, que necessitam para uso de docker, o senhor sudo...

- **Ativa Docker no computador:**

```bash
systemctl start docker
```

- **Desativa Docker no computador, se não estiver usando:**

```bash
systemctl stop docker
systemctl stop docker.socket
```

- **Ativa os contêineres(Usei watch para ter relatórios em desenvolvimento):**

```bash
docker compose up --watch
```

- **Por usar o Django, executei migrate manualmente:**

```bash
docker compose exec web python manage.py migrate
```

- **Pausa os contêineres:**

```bash
docker compose stop
```

- **Desativa os contêineres:**

```bash
docker compose down
```

- **Ver os contêineres ativos no momento( Use '-a' no fim do código para ver todos, inclusive desativados ou com erros):**

```bash
docker ps
```

- **Ver imagens:**

```bash
docker images
```

- **Ver os volumes:**

```bash
docker volume ls
```

- **Remover contêiner por id:**

```bash
docker rm id_container
```

- **Remover imagem por id:**

```bash
docker rmi id_image
```

- **APAGAR TUDO:**

```bash
docker system prune -a --volumes
```

- Tem mais, porém não cheguei a utilizar até o momento.

## Licença

Este projeto está licenciado sob a Licença MIT.  
Consulte o arquivo [LICENSE](./LICENSE) para mais detalhes.
