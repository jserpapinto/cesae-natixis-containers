# FROM: Define a imagem base
FROM ubuntu:latest

# ENV: Define uma variável de ambiente
ENV PORT=8080

# WORKDIR: Define o diretório de trabalho dentro do container
WORKDIR /app

# RUN: Executa comandos durante a construção da imagem
RUN apt-get update && apt-get install -y curl

# ADD: Adiciona e descompacta um arquivo tar.gz
ADD sample.tar.gz /app

# COPY: Copia um script local para o diretório de trabalho no container
COPY sleep.sh .

# EXPOSE: Documenta que o container escutará na porta 8080
EXPOSE ${PORT}

# ENTRYPOINT: Define o comando principal do container
ENTRYPOINT ["sh", "sleep.sh"]

# CMD: Comando padrão, pode ser sobrescrito ao rodar o container
CMD ["3600"]

