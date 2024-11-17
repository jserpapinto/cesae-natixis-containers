import { defineConfig } from 'vite';

export default defineConfig({
  build: {
    lib: {
      entry: './server.js',
      formats: ['cjs'],
      fileName: () => 'server.js'
    },
    outDir: 'build',
    rollupOptions: {
      external: ['express', 'path', 'buffer', 'events', 'http', 'fs'],
    },
    target: 'node20'
  },
}); 