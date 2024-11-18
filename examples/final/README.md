# Exercício Prático: Configuração de Aplicação com Docker Compose

## **Descrição do Problema**

Neste exercício, vais criar e configurar um ficheiro `docker-compose.yml` para orquestrar uma aplicação composta por três serviços:

1. **Frontend**: 
   - Uma página simples em HTML e JavaScript que faz uma chamada à API do backend após 3 segundos e exibe o código da resposta no browser.

2. **Backend**: 
   - Uma API implementada em Python que verifica a conectividade com uma base de dados.
   - Retorna:
     - **200**: Se conseguir conectar à base de dados.
     - **500**: Se não conseguir conectar.

3. **Base de Dados (MySQL)**:
   - Uma base de dados MySQL que será utilizada pelo backend para simular a persistência de dados.

---

## **Objetivo**

Criar o ficheiro `docker-compose.yml` para configurar, levantar e conectar os serviços existentes:
- **Frontend** deve estar acessível no browser através da porta `8080`.
- **Backend** deve comunicar com a base de dados e estar disponível na porta `5000`.
- **Base de Dados** deve ser configurada com as credenciais fornecidas.

---

## **Requisitos do `docker-compose.yml`**

1. **Serviço Frontend:**
   - Utiliza a imagem oficial do NGINX.
   - Utiliza um bind mount para servir o conteúdo do diretório `/frontend` e para que seja possível alterar o código sem ter que reconstruir a imagem.
   - Expõe a aplicação na porta `8080`.
   - A aplicação espera encontrar o serviço do backend a correr no url `http://localhost:5001`.

2. **Serviço Backend:**
   - Constrói a imagem do backend utilizando o Dockerfile no diretório `/backend`.
   - Passa as variáveis de ambiente para configurar a conexão com a base de dados:
     - `DB_HOST`
     - `DB_USER`
     - `DB_PASSWORD`
     - `DB_NAME`
   - Expõe o serviço na porta `5001`.
   - O backend espera encontrar a base de dados a correr no serviço com o nome `db`.

3. **Serviço Base de Dados:**
   - Utiliza a imagem oficial do MySQL.
   - Configura a base de dados com as seguintes credenciais:
     - `DB_USER`: `natixisuser`
     - `DB_PASSWORD`: `natixispass`
     - `DB_NAME`: `natixisdb`
     - `DB_ROOT_PASSWORD`: `natixisrootpass`
   - Utiliza um volume para garantir a persistência dos dados.

---

## **Tarefas**

1. **Escrever o `docker-compose.yml`:**
   - Configura os três serviços no ficheiro `docker-compose.yml`.
   - Define as redes necessárias para que os serviços consigam comunicar.

2. **Testar o Funcionamento:**
   - Levanta os serviços utilizando `docker-compose up`.
   - Acede ao frontend no browser através de `http://localhost:8080` e verifica:
     - Se a página carrega corretamente.
     - Se a validação do backend está a funcionar corretamente.

3. **Descobre o easter egg:**
   - Para quem conseguir levantar os serviços, há um easter egg na página.

---

## **Pontos de Atenção**

- Garante que os serviços utilizam variáveis de ambiente para configurações sensíveis, como as credenciais da base de dados.
- Testa a comunicação entre os serviços para confirmar que estão a funcionar corretamente na rede configurada pelo Docker Compose.
- Certifica-te de que o volume da base de dados está configurado para persistir os dados entre reinicializações.
