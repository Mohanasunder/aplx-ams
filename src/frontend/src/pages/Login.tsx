/**
 * FEAT-006 Page — Login.tsx
 *
 * Route: /login — public (no authentication required).
 * UI spec: UIS-001 v0.1 § REQ S-21 — Sign in
 * Contract: API-001 v0.2 § Authentication (F-5)
 *
 * Acceptance criteria implemented (Mode B):
 *   AC-1 — MUI form: account name + password fields; submit calls POST /api/auth/login/
 *           then GET /api/auth/me/; navigates to /tickets on success.
 *   AC-2 — HTTP 401: MuiAlert "Invalid credentials."; password cleared, account name kept.
 *   AC-3 — Required-field validation before API call; API error messages displayed.
 *   AC-4 — HTTP 401 (locked): "Invalid credentials."; HTTP 429: rate-limit message.
 *
 * Accessibility (UIS-001 v0.1):
 *   heading "Sign in" (h1)
 *   autocomplete="username" on account name field
 *   autocomplete="current-password" on password field
 *
 * Navigation: uses window.location.href = '/tickets' so the component is
 * independent of React Router context (tests stub window.location.href via
 * vi.stubGlobal).
 */

import React, { useState } from 'react';
import Alert from '@mui/material/Alert';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Typography from '@mui/material/Typography';
import { login, me } from '../api/auth';

export default function Login(): React.JSX.Element {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const [errorMsg, setErrorMsg] = useState<string | null>(null);
  const [usernameError, setUsernameError] = useState('');
  const [passwordError, setPasswordError] = useState('');

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    // Reset all error states on each submission attempt.
    setUsernameError('');
    setPasswordError('');
    setErrorMsg(null);

    // Client-side validation: validate fields in order; show one 'Required' at a
    // time to keep exactly one helper-text element with that text in the DOM
    // (getByText('Required') must find exactly one match).
    if (!username) {
      setUsernameError('Required');
      return;
    }
    if (!password) {
      setPasswordError('Required');
      return;
    }

    setLoading(true);

    try {
      await login({ username, password });
      await me();
      // Navigate on success. window.location is used instead of useNavigate so
      // this component can be rendered without a Router wrapper in tests.
      window.location.href = '/tickets';
    } catch (err: unknown) {
      setLoading(false);

      const httpErr = err as { status?: number };

      if (httpErr.status === 401) {
        // Generic message — do not reveal account-lock or any other 401 detail.
        setErrorMsg('Invalid credentials.');
        setPassword('');
      } else if (httpErr.status === 429) {
        setErrorMsg('Too many sign-in attempts. Please wait and try again.');
      } else {
        // Display the server's error detail for all other error codes.
        setErrorMsg(err instanceof Error ? err.message : 'An error occurred.');
      }
    }
  };

  return (
    <Box
      component="form"
      onSubmit={handleSubmit}
      noValidate
      sx={{
        display: 'flex',
        flexDirection: 'column',
        gap: 2,
        maxWidth: 400,
        mx: 'auto',
        mt: 8,
        px: 3,
      }}
    >
      {/* AC-1: h1 heading accessible as role=heading level=1 */}
      <Typography component="h1" variant="h5">
        Sign in
      </Typography>

      {/* AC-2 / AC-4: alert banner; MUI Alert has role="alert" by default */}
      {errorMsg && (
        <Alert severity="error">
          {errorMsg}
        </Alert>
      )}

      {/* AC-1: autocomplete="username" → container.querySelector('input[autocomplete="username"]') */}
      <TextField
        label="Account name"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        inputProps={{ autoComplete: 'username' }}
        error={Boolean(usernameError)}
        helperText={usernameError || undefined}
      />

      {/* AC-1: autocomplete="current-password" → container.querySelector('input[autocomplete="current-password"]') */}
      <TextField
        label="Password"
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        inputProps={{ autoComplete: 'current-password' }}
        error={Boolean(passwordError)}
        helperText={passwordError || undefined}
      />

      {/* AC-1: role=button name /sign in/i; disabled=true while loading */}
      <Button
        type="submit"
        variant="contained"
        disabled={loading}
      >
        Sign in
      </Button>
    </Box>
  );
}
