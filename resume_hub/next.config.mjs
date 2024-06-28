import NextBundleAnalyzer from '@next/bundle-analyzer';
import createNextIntlPlugin from 'next-intl/plugin';
import path, { dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const withBundleAnalyzer = NextBundleAnalyzer({
  enabled: process.env.BUNDLE_ANALYZE === 'true',
});

const withNextIntl = createNextIntlPlugin();

/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'standalone',
  sassOptions: {
    includePaths: [path.resolve(__dirname, 'src', 'shared', 'theme')],
  },
  reactStrictMode: true,
};

export default withBundleAnalyzer(withNextIntl(nextConfig));
