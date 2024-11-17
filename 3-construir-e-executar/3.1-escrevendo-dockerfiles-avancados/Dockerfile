# Imagem base
FROM node:20

# Copiar código
COPY . .

# Instalar dependências
RUN npm install

# Build do código
RUN npm run build

# Comando padrão para iniciar a aplicação
CMD ["node", "build/server.js"]