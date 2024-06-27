'use client';

import { useSearchParams } from 'next/navigation';
import { useEffect, useState } from 'react';

import { LocaleService } from './locale-service';

export function useLocaleState() {
  const searchParams = useSearchParams();
  const searchLocale = searchParams.get(LocaleService.SEARCH_PARAMS_KEY) as Locale;
  if (searchLocale && LocaleService.ALL_LOCALES.includes(searchLocale)) {
    LocaleService.setLocale(searchLocale);
  }

  const [locale, setLocale] = useState(LocaleService.getLocale());

  //   Set Locale to Cookies if not set yet
  useEffect(() => {
    const cookieLocale = LocaleService.getCookiesLocale();

    if (!cookieLocale) {
      LocaleService.setLocale(LocaleService.DEFAULT_LOCALE);
      setLocale(LocaleService.DEFAULT_LOCALE);
    }
  }, []);

  return [locale, setLocale];
}
