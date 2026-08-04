/** API helper functions: URL building, headers, and response/error parsing. */

import axios from 'axios';
import { API_BASE_URL } from './constants';

export function buildApiUrl(path: string): string {
  const cleanPath = path.startsWith('/') ? path : '/' + path;
  return API_BASE_URL + cleanPath;
}

export function getDefaultHeaders(): Record<string, string> {
  return {
    'Content-Type': 'application/json',
  };
}

export interface ApiErrorShape {
  status: number;
  code: string;
  message: string;
  details?: unknown[];
}

export function formatApiError(error: unknown): ApiErrorShape {
  if (axios.isAxiosError(error) && error.response?.data) {
    const data = error.response.data as Partial<ApiErrorShape>;
    return {
      status: data.status ?? error.response.status ?? 500,
      code: data.code ?? 'UNKNOWN_ERROR',
      message: data.message ?? 'An unexpected error occurred.',
      details: data.details ?? [],
    };
  }

  return {
    status: 500,
    code: 'UNKNOWN_ERROR',
    message: error instanceof Error ? error.message : 'An unexpected error occurred.',
  };
}
