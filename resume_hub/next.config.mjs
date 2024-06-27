import NextBundleAnalyzer from '@next/bundle-analyzer';
import createNextIntlPlugin from 'next-intl/plugin';
import path, { dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));

const withNextIntl = createNextIntlPlugin();

const withBundleAnalyzer = NextBundleAnalyzer({
  enabled: process.env.BUNDLE_ANALYZE === 'true',
});

/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'standalone',
  sassOptions: {
    includePaths: [path.resolve(__dirname, 'src', 'shared', 'theme')],
  },
  reactStrictMode: true,

  async rewrites() {
    return [
      {
        source: '/api/resume-manager/:path*',
        destination: 'http://localhost:8000/:path*',
      },
    ];
  },
};

export default withBundleAnalyzer(withNextIntl(nextConfig));
