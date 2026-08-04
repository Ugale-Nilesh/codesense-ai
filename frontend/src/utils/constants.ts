/** Application-wide constants shared across the frontend. */

export const API_BASE_URL: string =
  import.meta.env.VITE_API_BASE_URL ?? 'http://localhost:8000';

export const APP_NAME: string =
  import.meta.env.VITE_APP_NAME ?? 'CodeSense AI';

export const SUPPORTED_FILE_EXTENSIONS: string[] = [
  '.py', '.js', '.ts', '.tsx', '.jsx', '.java', '.c', '.cpp', '.cs',
  '.go', '.rb', '.php', '.rs', '.swift', '.kt', '.html', '.css',
  '.json', '.yaml', '.yml', '.md', '.txt', '.zip',
];

export const MAX_UPLOAD_SIZE_MB = 25;

export const DEFAULT_PAGE_SIZE = 20;
