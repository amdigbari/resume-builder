'use client';

import { useMutation } from '@tanstack/react-query';
import useTranslation from 'next-translate/useTranslation';
import { useEffect } from 'react';

import { mutateService } from 'src/shared/services';

export default function Home() {
  const { t } = useTranslation('common');

  const { mutate } = useMutation(mutateService('post', 'resume-manager:/v1/users/token'));

  useEffect(() => {
    mutate({ body: { username: 'digi', password: 'digi' } });
  }, []);

  return (
    <div>
      <h2>{t('hello-world')}</h2>
    </div>
  );
}
