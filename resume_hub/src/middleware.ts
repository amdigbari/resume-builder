import createMiddleware from 'next-intl/middleware';
import type { NextRequest } from 'next/server';

import { ALL_LOCALES, DEFAULT_LOCALE } from 'src/shared/utils';

const intlMiddleware = createMiddleware({
  locales: ALL_LOCALES,
  defaultLocale: DEFAULT_LOCALE,
  localeDetection: true,
});

export default function middleware(request: NextRequest) {
  const { pathname } = request.nextUrl;

  const shouldHandle =
    pathname === '/' || new RegExp(`^/(${ALL_LOCALES.join('|')})(/.*)?$`).test(request.nextUrl.pathname);
  if (!shouldHandle) return;

  return intlMiddleware(request);
}
