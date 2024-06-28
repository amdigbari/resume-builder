import { getRequestConfig } from 'next-intl/server';
import { notFound } from 'next/navigation';

import { ALL_LOCALES } from 'src/shared/utils';

export default getRequestConfig(async ({ locale }) => {
  // Validate that the incoming `locale` parameter is valid
  if (!ALL_LOCALES.includes(locale as Locale)) notFound();

  return {
    messages: (await import(`./messages/${locale}.json`)).default,
  };
});
