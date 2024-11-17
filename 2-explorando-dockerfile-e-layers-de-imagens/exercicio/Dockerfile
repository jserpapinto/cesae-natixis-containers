FROM node:20

# Set an environment variable for the port
ENV PORT=3000

# Define the working directory
WORKDIR /app

# Copy file server.js to /app/server.js
COPY ./server.js server.js 

# Show the env var in the build logs
RUN echo ${PORT}

# Expose the port
EXPOSE ${PORT}

# Set the default command to run the server
CMD ["node", "server.js"]
