export function getLocaleLang(locale: Locales): string {
  return locale.split('-')[0];
}
