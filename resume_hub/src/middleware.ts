import createMiddleware from 'next-intl/middleware';

import { ALL_LOCALES, DEFAULT_LOCALE } from 'src/shared/utils';

export default createMiddleware({
  locales: ALL_LOCALES,
  defaultLocale: DEFAULT_LOCALE,
  localeDetection: true,
});

export const config = {
  // Match only internationalized pathnames
  matcher: ['/', `/(${ALL_LOCALES.join('|')})/:path*`],
};
