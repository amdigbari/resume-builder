'use client';

import { QueryClientProvider } from '@tanstack/react-query';
import { type ReactNode } from 'react';
import { ThemeProvider as BootstrapThemeProvider } from 'react-bootstrap';

import { ToastProvider } from 'src/shared/components';
import { queryClient } from 'src/shared/services';
import { LocaleService, useLocaleState } from 'src/shared/utils';

interface Props {
  children: ReactNode;
}
export function AppProviders({ children }: Props): ReactNode {
  // Sets the locale to the Cookies at start
  useLocaleState();

  // Providing all messages to the client
  // side is the easiest way to get started

  return (
    <QueryClientProvider client={queryClient}>
      <BootstrapThemeProvider dir={LocaleService.getLocaleDir()}>
        <ToastProvider>{children}</ToastProvider>
      </BootstrapThemeProvider>
    </QueryClientProvider>
  );
}
