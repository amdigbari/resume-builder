import { isServer } from 'src/configs';

export const ALL_LOCALES: Locale[] = ['fa-IR', 'en-US'];
export const DEFAULT_LOCALE: Locale = 'fa-IR';

const LOCALE_DIR: { [key in Locale]: Dir } = {
  'fa-IR': 'rtl',
  'en-US': 'ltr',
};

export async function getCurrentLocale(): Promise<Locale> {
  try {
    const { getLocale: intlGetLocale } = await import('next-intl/server');
    return (await intlGetLocale()) as unknown as Promise<Locale>;
  } catch {
    console.log(window.location.pathname, window.location.pathname.split('/')[1]);
    return !isServer ? (window.location.pathname.split('/')[1] as Locale) : DEFAULT_LOCALE;
  }
}

export function getLocaleDir(locale: Locale): Dir {
  return LOCALE_DIR[locale];
}

export function getLocaleLang(locale: Locale) {
  return locale.split('-')[0];
}
