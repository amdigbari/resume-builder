import enUS from '../../../messages/en-US.json';

type Messages = typeof enUS;

declare global {
  // Use type safe message keys with `next-intl`
  interface IntlMessages extends Messages {}
}
