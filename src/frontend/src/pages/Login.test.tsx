/**
 * FEAT-006 Acceptance Criterion Coverage Map — Login.test.tsx
 *
 * Criterion  │ Test name                                                            │ What it asserts
 * ───────────┼──────────────────────────────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────
 * AC-1       │ REQ-021 AC-1: heading 'Sign in' rendered as h1                       │ role=heading level=1, accessible name /sign in/i present in DOM
 * AC-1       │ REQ-021 AC-1: account name field has autocomplete='username'         │ input with autocomplete='username' in DOM
 * AC-1       │ REQ-021 AC-1: password field has autocomplete='current-password'     │ input with autocomplete='current-password' in DOM
 * AC-1       │ REQ-021 AC-1: renders Sign in button                                │ role=button, name /sign in/i present in DOM
 * AC-1       │ REQ-021 AC-1: successful login calls login() then me() then navigates to /tickets │ login mock called with {username,password}; me mock called; window.location.href='/tickets'
 * AC-1       │ REQ-021 AC-1: Sign in button disabled and loading indicator shown while submitting │ button disabled during in-flight login call
 * AC-2       │ REQ-021 AC-2: HTTP 401 shows generic 'Invalid credentials.' alert    │ MuiAlert with text 'Invalid credentials.' visible; role=alert
 * AC-2       │ REQ-021 AC-2: password cleared and account name retained after 401   │ password input value=''; account name input retains typed value
 * AC-3       │ REQ-021 AC-3: empty account name shows Required before API call      │ helper text 'Required' visible; login() not called
 * AC-3       │ REQ-021 AC-3: empty password shows Required before API call          │ helper text 'Required' visible; login() not called
 * AC-3       │ REQ-021 AC-3: API error message from server is displayed             │ arbitrary server error text visible in DOM after non-401 API error
 * AC-4       │ REQ-021 AC-4: HTTP 401 for locked account shows 'Invalid credentials.' │ MuiAlert 'Invalid credentials.' (same generic message; no lockout detail)
 * AC-4       │ REQ-021 AC-4: HTTP 429 shows rate-limit message                      │ MuiAlert 'Too many sign-in attempts. Please wait and try again.'
 *
 * Mode A RED reasons (all tests fail because Login stub returns null):
 *   AC-1 tests — getByRole('heading') / querySelector / getByRole('button') throw
 *                because no DOM elements exist; login and me mocks are never called.
 *   AC-2 tests — getByRole('button', { name: /sign in/i }) throws before form can
 *                be submitted; error alert never appears.
 *   AC-3 tests — getByRole('button', ...) throws before empty submission can be
 *                attempted; Required helper text never appears.
 *   AC-4 tests — getByRole('button', ...) throws before 401/429 response can be
 *                triggered; rate-limit alert never appears.
 *
 * These tests turn GREEN in Mode B when Login:
 *   - Renders h1 "Sign in", account name input (autocomplete=username), password
 *     input (autocomplete=current-password), Sign in MuiButton.
 *   - On submit: calls login({username, password}), then me(); on success navigates
 *     to /tickets (window.location.href = '/tickets').
 *   - During in-flight call: Sign in button is disabled (loading state).
 *   - On HTTP 401: MuiAlert "Invalid credentials."; password cleared, account name kept.
 *   - On HTTP 429: MuiAlert "Too many sign-in attempts. Please wait and try again."
 *   - On empty field submit: shows "Required" helper text; login() not called.
 *   - On other API error: shows the detail string from the API error response.
 */

import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import React from 'react';
import Login from './Login';

// ── API mock ──────────────────────────────────────────────────────────────────
// vi.mock replaces ../api/auth for all tests in this file.
// Individual tests override the mock return value with mockResolvedValueOnce /
// mockRejectedValueOnce as needed.

vi.mock('../api/auth', () => ({
  login: vi.fn(),
  logout: vi.fn(),
  me: vi.fn(),
}));

// Import after vi.mock so we get the mocked versions.
import { login, me } from '../api/auth';

// ── Helpers ───────────────────────────────────────────────────────────────────

/** Default successful UserMe returned by login() and me() */
const MOCK_USER = {
  id: 1,
  name: 'Alice Smith',
  email: 'alice@applexus.com',
  role: 'l1_support' as const,
  is_active: true,
  client_organization_id: null,
  client_organization_name: null,
};

/** Error object thrown when server returns HTTP 401. */
class HttpError extends Error {
  constructor(
    public status: number,
    public detail: string,
  ) {
    super(detail);
  }
}

/** Render Login with a clean location stub for navigation checks. */
function renderLogin() {
  return render(<Login />);
}

// ── Test setup ────────────────────────────────────────────────────────────────

beforeEach(() => {
  vi.clearAllMocks();
  // Stub window.location so navigation assertions work in jsdom.
  vi.stubGlobal('location', { href: '' });
});

// ── AC-1: Successful sign-in ──────────────────────────────────────────────────

describe('REQ-021 AC-1: successful sign-in flow', () => {
  it('REQ-021 AC-1: heading "Sign in" rendered as h1', () => {
    renderLogin();
    expect(
      screen.getByRole('heading', { level: 1, name: /sign in/i }),
    ).toBeDefined();
  });

  it("REQ-021 AC-1: account name field has autocomplete='username'", () => {
    const { container } = renderLogin();
    const input = container.querySelector('input[autocomplete="username"]');
    expect(input).not.toBeNull();
  });

  it("REQ-021 AC-1: password field has autocomplete='current-password'", () => {
    const { container } = renderLogin();
    const input = container.querySelector(
      'input[autocomplete="current-password"]',
    );
    expect(input).not.toBeNull();
  });

  it('REQ-021 AC-1: renders Sign in button', () => {
    renderLogin();
    expect(
      screen.getByRole('button', { name: /sign in/i }),
    ).toBeDefined();
  });

  it('REQ-021 AC-1: successful login calls login() then me() then navigates to /tickets', async () => {
    vi.mocked(login).mockResolvedValueOnce(MOCK_USER);
    vi.mocked(me).mockResolvedValueOnce(MOCK_USER);

    const { container } = renderLogin();

    // Fill account name
    const usernameInput = container.querySelector(
      'input[autocomplete="username"]',
    ) as HTMLInputElement;
    fireEvent.change(usernameInput, {
      target: { value: 'alice@applexus.com' },
    });

    // Fill password
    const passwordInput = container.querySelector(
      'input[autocomplete="current-password"]',
    ) as HTMLInputElement;
    fireEvent.change(passwordInput, { target: { value: 'Abcdefg1' } });

    // Submit
    fireEvent.click(screen.getByRole('button', { name: /sign in/i }));

    await waitFor(() => {
      expect(vi.mocked(login)).toHaveBeenCalledWith({
        username: 'alice@applexus.com',
        password: 'Abcdefg1',
      });
    });

    await waitFor(() => {
      expect(vi.mocked(me)).toHaveBeenCalledTimes(1);
    });

    await waitFor(() => {
      expect(window.location.href).toBe('/tickets');
    });
  });

  it('REQ-021 AC-1: Sign in button disabled and loading indicator shown while submitting', async () => {
    // login() never resolves — keeps the component in loading state.
    vi.mocked(login).mockReturnValueOnce(new Promise(() => undefined));

    const { container } = renderLogin();

    const usernameInput = container.querySelector(
      'input[autocomplete="username"]',
    ) as HTMLInputElement;
    fireEvent.change(usernameInput, {
      target: { value: 'alice@applexus.com' },
    });

    const passwordInput = container.querySelector(
      'input[autocomplete="current-password"]',
    ) as HTMLInputElement;
    fireEvent.change(passwordInput, { target: { value: 'Abcdefg1' } });

    fireEvent.click(screen.getByRole('button', { name: /sign in/i }));

    // Button should be disabled immediately after submit while login() is pending.
    await waitFor(() => {
      const btn = screen.getByRole('button', { name: /sign in/i });
      expect((btn as HTMLButtonElement).disabled).toBe(true);
    });
  });
});

// ── AC-2: Wrong password (HTTP 401) ──────────────────────────────────────────

describe('REQ-021 AC-2: wrong password shows generic error', () => {
  it("REQ-021 AC-2: HTTP 401 shows generic 'Invalid credentials.' alert", async () => {
    vi.mocked(login).mockRejectedValueOnce(
      new HttpError(401, 'Invalid credentials.'),
    );

    const { container } = renderLogin();

    const usernameInput = container.querySelector(
      'input[autocomplete="username"]',
    ) as HTMLInputElement;
    fireEvent.change(usernameInput, {
      target: { value: 'alice@applexus.com' },
    });

    const passwordInput = container.querySelector(
      'input[autocomplete="current-password"]',
    ) as HTMLInputElement;
    fireEvent.change(passwordInput, { target: { value: 'WrongPass1' } });

    fireEvent.click(screen.getByRole('button', { name: /sign in/i }));

    await waitFor(() => {
      expect(screen.getByRole('alert')).toBeDefined();
      expect(screen.getByText('Invalid credentials.')).toBeDefined();
    });
  });

  it('REQ-021 AC-2: password cleared and account name retained after 401', async () => {
    vi.mocked(login).mockRejectedValueOnce(
      new HttpError(401, 'Invalid credentials.'),
    );

    const { container } = renderLogin();

    const usernameInput = container.querySelector(
      'input[autocomplete="username"]',
    ) as HTMLInputElement;
    fireEvent.change(usernameInput, {
      target: { value: 'alice@applexus.com' },
    });

    const passwordInput = container.querySelector(
      'input[autocomplete="current-password"]',
    ) as HTMLInputElement;
    fireEvent.change(passwordInput, { target: { value: 'WrongPass1' } });

    fireEvent.click(screen.getByRole('button', { name: /sign in/i }));

    await waitFor(() => {
      expect(screen.getByText('Invalid credentials.')).toBeDefined();
    });

    // Account name field must retain its value; password field must be cleared.
    expect(usernameInput.value).toBe('alice@applexus.com');
    expect(passwordInput.value).toBe('');
  });
});

// ── AC-3: Required-field validation and API error display ─────────────────────

describe('REQ-021 AC-3: required-field validation and API error display', () => {
  it('REQ-021 AC-3: empty account name shows Required before API call', async () => {
    renderLogin();

    // Submit without filling the account name field.
    fireEvent.click(screen.getByRole('button', { name: /sign in/i }));

    await waitFor(() => {
      expect(screen.getByText('Required')).toBeDefined();
    });
    expect(vi.mocked(login)).not.toHaveBeenCalled();
  });

  it('REQ-021 AC-3: empty password shows Required before API call', async () => {
    const { container } = renderLogin();

    // Fill account name but leave password empty.
    const usernameInput = container.querySelector(
      'input[autocomplete="username"]',
    ) as HTMLInputElement;
    fireEvent.change(usernameInput, {
      target: { value: 'alice@applexus.com' },
    });

    fireEvent.click(screen.getByRole('button', { name: /sign in/i }));

    await waitFor(() => {
      expect(screen.getByText('Required')).toBeDefined();
    });
    expect(vi.mocked(login)).not.toHaveBeenCalled();
  });

  it('REQ-021 AC-3: API error message from server is displayed', async () => {
    vi.mocked(login).mockRejectedValueOnce(
      new HttpError(400, 'Password must contain at least one upper-case letter.'),
    );

    const { container } = renderLogin();

    const usernameInput = container.querySelector(
      'input[autocomplete="username"]',
    ) as HTMLInputElement;
    fireEvent.change(usernameInput, {
      target: { value: 'alice@applexus.com' },
    });

    const passwordInput = container.querySelector(
      'input[autocomplete="current-password"]',
    ) as HTMLInputElement;
    fireEvent.change(passwordInput, { target: { value: 'abcdefg1' } });

    fireEvent.click(screen.getByRole('button', { name: /sign in/i }));

    await waitFor(() => {
      expect(
        screen.getByText(
          'Password must contain at least one upper-case letter.',
        ),
      ).toBeDefined();
    });
  });
});

// ── AC-4: Locked account (HTTP 401) and rate limit (HTTP 429) ────────────────

describe('REQ-021 AC-4: locked account and rate limit', () => {
  it("REQ-021 AC-4: HTTP 401 for locked account shows 'Invalid credentials.' (generic message)", async () => {
    // After 5 failed sign-ins the backend still returns HTTP 401 with the same
    // generic message — the frontend must not reveal the account is locked.
    vi.mocked(login).mockRejectedValueOnce(
      new HttpError(401, 'Invalid credentials.'),
    );

    const { container } = renderLogin();

    const usernameInput = container.querySelector(
      'input[autocomplete="username"]',
    ) as HTMLInputElement;
    fireEvent.change(usernameInput, {
      target: { value: 'alice@applexus.com' },
    });

    const passwordInput = container.querySelector(
      'input[autocomplete="current-password"]',
    ) as HTMLInputElement;
    fireEvent.change(passwordInput, { target: { value: 'CorrectPass1' } });

    fireEvent.click(screen.getByRole('button', { name: /sign in/i }));

    await waitFor(() => {
      expect(screen.getByRole('alert')).toBeDefined();
      expect(screen.getByText('Invalid credentials.')).toBeDefined();
    });
    // Must NOT reveal lock-specific text.
    expect(
      screen.queryByText(/locked/i),
    ).toBeNull();
  });

  it("REQ-021 AC-4: HTTP 429 shows 'Too many sign-in attempts. Please wait and try again.'", async () => {
    vi.mocked(login).mockRejectedValueOnce(
      new HttpError(429, 'Too many sign-in attempts. Please wait and try again.'),
    );

    const { container } = renderLogin();

    const usernameInput = container.querySelector(
      'input[autocomplete="username"]',
    ) as HTMLInputElement;
    fireEvent.change(usernameInput, {
      target: { value: 'alice@applexus.com' },
    });

    const passwordInput = container.querySelector(
      'input[autocomplete="current-password"]',
    ) as HTMLInputElement;
    fireEvent.change(passwordInput, { target: { value: 'AnyPass1' } });

    fireEvent.click(screen.getByRole('button', { name: /sign in/i }));

    await waitFor(() => {
      expect(screen.getByRole('alert')).toBeDefined();
      expect(
        screen.getByText(
          'Too many sign-in attempts. Please wait and try again.',
        ),
      ).toBeDefined();
    });
  });
});
