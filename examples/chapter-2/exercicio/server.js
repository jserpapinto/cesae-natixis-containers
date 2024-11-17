const http = require('http');

// Get the port from the environment variables or use 3000 as a default
const PORT = process.env.PORT || 3000;

// Create a simple HTTP server
const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello, World!\n');
});

// Start the server
server.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

// Gracefully handle shutdown
const shutdown = (signal) => {
  console.log(`Received ${signal}, shutting down server gracefully...`);
  server.close(() => {
    console.log('Server closed.');
    process.exit(0);
  });

  // Force shutdown if it takes too long
  setTimeout(() => {
    console.error('Forcing server shutdown...');
    process.exit(1);
  }, 5000); // 5 seconds timeout
};

// Handle SIGINT (Ctrl+C)
process.on('SIGINT', () => shutdown('SIGINT'));

// Handle SIGTERM (optional, if stopping container with `docker stop`)
process.on('SIGTERM', () => shutdown('SIGTERM'));
