'use client';

import { QueryClientProvider } from '@tanstack/react-query';
import { useLocale } from 'next-intl';
import { type ReactNode } from 'react';
import { ThemeProvider as BootstrapThemeProvider } from 'react-bootstrap';

import { ToastProvider } from 'src/shared/components';
import { queryClient } from 'src/shared/services';
import { getLocaleDir } from 'src/shared/utils';

interface Props {
  children: ReactNode;
}
export function AppProviders({ children }: Props): ReactNode {
  const locale = useLocale() as Locale;

  return (
    <QueryClientProvider client={queryClient}>
      <BootstrapThemeProvider dir={getLocaleDir(locale)}>
        <ToastProvider>{children}</ToastProvider>
      </BootstrapThemeProvider>
    </QueryClientProvider>
  );
}
