/**
 * Reusable, framework-agnostic input validators. Each function returns a
 * boolean; callers decide how to surface validation failures in the UI.
 */

const EMAIL_PATTERN = /^[^@\s]+@[^@\s]+\.[^@\s]+$/;
const URL_PATTERN = /^https?:\/\/[^\s]+$/i;

export function isValidEmail(value: string): boolean {
  return EMAIL_PATTERN.test(value.trim());
}

export function isValidPassword(value: string): boolean {
  // At least 8 characters, one letter and one number.
  return value.length >= 8 && /[A-Za-z]/.test(value) && /\d/.test(value);
}

export function isValidUrl(value: string): boolean {
  return URL_PATTERN.test(value.trim());
}

export function isEmpty(value: string | null | undefined): boolean {
  return value === null || value === undefined || value.trim().length === 0;
}
