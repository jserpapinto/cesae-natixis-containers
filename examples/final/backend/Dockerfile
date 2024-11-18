# Imagem base Python leve
FROM python:3.10-slim

ENV APP_PORT=5000

# Definir diretório de trabalho
WORKDIR /app

# Copiar os arquivos necessários
COPY requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o resto do código
COPY . .

# Expor a porta da aplicação
EXPOSE ${APP_PORT}

# Comando para iniciar o servidor Flask
CMD ["python", "app.py"]