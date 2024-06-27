import Cookies from 'js-cookie';

import localeData from '../../../../i18n.json';

// Based on next-translate settings. https://github.com/aralroca/next-translate?tab=readme-ov-file#11-how-to-save-the-user-defined-language

export class LocaleService {
  static ALL_LOCALES: Locale[] = localeData.locales as Locale[];
  static SEARCH_PARAMS_KEY = 'lang';
  static LOCALE_COOKIE_KEY = 'NEXT_LOCALE';
  static DEFAULT_LOCALE: Locale = localeData.defaultLocale as Locale;

  private static LOCALE_DIR: { [key in Locale]: Dir } = {
    'fa-IR': 'rtl',
    'en-US': 'ltr',
  };

  static setLocale(value: Locale) {
    if (value !== this.getLocale() && this.ALL_LOCALES.includes(value)) {
      Cookies.set(this.LOCALE_COOKIE_KEY, value);
    }
  }

  static getLocale() {
    const locale = Cookies.get(this.LOCALE_COOKIE_KEY) as Locale | undefined;

    return locale && this.ALL_LOCALES.includes(locale) ? locale : this.DEFAULT_LOCALE;
  }

  static getCookiesLocale() {
    return Cookies.get(this.LOCALE_COOKIE_KEY);
  }

  static empty() {
    Cookies.remove(this.LOCALE_COOKIE_KEY);
  }

  static getLocaleDir(): Dir {
    return this.LOCALE_DIR[this.getLocale()];
  }

  static getLang() {
    return this.getLocale().split('-')[0];
  }
}
