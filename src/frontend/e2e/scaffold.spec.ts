// FEAT-035: E2E CI Scaffold — Mode A tests (updated per DEC-068)
// Criterion: STD-001 AC-5
// Given playwright.config.ts specifies baseURL: 'http://localhost' (nginx port 80 exposed to runner host),
// when npx playwright test is invoked in CI against that URL,
// then the Playwright test runner loads the configuration without errors and exits 0.

import { test, expect } from 'playwright/test';
import config from '../playwright.config';

// STD-001 AC-5
test('playwright initialises with baseURL http://localhost', () => {
  // docker-compose.yml exposes nginx port 80:80 to the runner host.
  // Playwright runs on the host, not inside Docker, so http://localhost resolves correctly (DEC-068).
  expect((config as { use?: { baseURL?: string } }).use?.baseURL).toBe('http://localhost');
});
