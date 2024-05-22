export default defineConfig({
  plugins: [react()],
  server: {
    host: '0.0.0.0', // The host is also important, for hosting react projects. Set it to 0.0.0.0, like here.
    port: 3000, // Change the port!
  },
})
