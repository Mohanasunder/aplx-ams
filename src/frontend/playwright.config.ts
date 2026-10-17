// Minimal Playwright config for FEAT-001 scaffold — no E2E tests yet (A-041, DEC-056).
// The first story feature that adds a page will add tests to the e2e/ directory
// and remove the --pass-with-no-tests flag from CI.

export default {
  testDir: './e2e',
};
