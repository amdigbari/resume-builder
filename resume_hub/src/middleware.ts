import createMiddleware from 'next-intl/middleware';

export default createMiddleware({
  // A list of all locales that are supported
  locales: ['fa-IR', 'en-US'],

  // Used when no locale matches
  defaultLocale: 'fa-IR',
});

export const config = {
  // Match only internationalized pathnames
  matcher: ['/', '/(fa-IR|en-US)/:path*'],
};
