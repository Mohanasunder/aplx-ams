import { defineConfig } from 'playwright/test';

export default defineConfig({
  testDir: './e2e',
  use: {
    baseURL: 'http://nginx:80',
    headless: true,
  },
  projects: [
    {
      name: 'chromium',
      use: { browserName: 'chromium' },
    },
  ],
});
