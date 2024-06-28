'use client';

import { useTranslations } from 'next-intl';

export default function Home() {
  const t = useTranslations('common');

  return (
    <div>
      <h2>{t('hello-world')}</h2>
    </div>
  );
}
