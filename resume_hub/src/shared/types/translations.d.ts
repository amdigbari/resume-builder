import enUS from '../../../messages/fa-IR.json';
import faIR from '../../../messages/fa-IR.json';

type Messages = typeof enUS | typeof faIR;

declare global {
  // Use type safe message keys with `next-intl`
  interface IntlMessages extends Messages {}
}
