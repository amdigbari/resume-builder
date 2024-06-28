type SearchParams<T extends string> = {
  [key in T as key extends `${infer k}[]` ? k : key extends `${infer k}?` ? k : key]: T extends `${string}[]`
    ? string[]
    : T extends `${string}?`
      ? string | undefined
      : string;
};

type Locale = 'fa-IR' | 'en-US';

interface PageProps<T extends string = never, U extends string = never> {
  params: { locale: Locale } & { [k in T]: string };
  searchParams: SearchParams<'lang' | U>;
}

interface LayoutProps<T extends string = never, U extends string = never>
  extends Omit<PageProps<T, U>, 'searchParams'> {
  children: ReactNode;
}

// Extracted from Bootstrap color variants
type ColorVariant = 'primary' | 'secondary' | 'success' | 'danger' | 'warning' | 'info' | 'dark' | 'light';

type Dir = 'ltr' | 'rtl';
