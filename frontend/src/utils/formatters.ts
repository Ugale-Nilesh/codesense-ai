/** Presentation formatters. Pure functions - no side effects. */

export function formatFileSize(bytes: number): string {
  if (bytes < 0) throw new Error('bytes must be non-negative');

  const units = ['B', 'KB', 'MB', 'GB', 'TB'];
  let size = bytes;
  let unitIndex = 0;

  while (size >= 1024 && unitIndex < units.length - 1) {
    size /= 1024;
    unitIndex += 1;
  }

  const formatted = unitIndex === 0 ? String(size) : size.toFixed(1);
  return formatted + ' ' + units[unitIndex];
}

export function formatDate(date: Date | string, locale = 'en-US'): string {
  const d = typeof date === 'string' ? new Date(date) : date;
  return d.toLocaleDateString(locale, { year: 'numeric', month: 'short', day: 'numeric' });
}

export function formatTime(date: Date | string, locale = 'en-US'): string {
  const d = typeof date === 'string' ? new Date(date) : date;
  return d.toLocaleTimeString(locale, { hour: '2-digit', minute: '2-digit' });
}

export function formatPercentage(value: number, decimals = 0): string {
  return value.toFixed(decimals) + '%';
}
