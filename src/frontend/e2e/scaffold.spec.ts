// FEAT-035: E2E CI Scaffold — Mode A tests
// Criterion: STD-001 AC-5
// Given playwright.config.ts specifies baseURL: 'http://nginx:80' (the local-dev Docker Nginx service),
// when npx playwright test is invoked in CI against that URL,
// then the Playwright test runner loads the configuration without errors and exits 0.
//
// Red state: current playwright.config.ts has no `use.baseURL` — this test fails with
// "Expected: 'http://nginx:80', Received: undefined" until Mode B upgrades the config.

import { test, expect } from 'playwright/test';
import config from '../playwright.config';

// STD-001 AC-5
test('playwright initialises with baseURL http://nginx:80', () => {
  // The config must specify baseURL so the E2E runner targets the correct Docker Nginx service.
  // Until playwright.config.ts is upgraded (Mode B), config.use?.baseURL is undefined → test is red.
  expect((config as { use?: { baseURL?: string } }).use?.baseURL).toBe('http://nginx:80');
});
