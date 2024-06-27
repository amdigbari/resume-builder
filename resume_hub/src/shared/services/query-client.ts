import { QueryClient, type UseMutationOptions, type UseQueryOptions, isServer } from '@tanstack/react-query';
import type { HttpMethod, MediaType } from 'openapi-typescript-helpers';

import {
  ClientFetchParams,
  type HttpPaths,
  type HttpRequestData,
  type HttpResponseData,
  clientFetch,
} from './api-service';

// This makes sure that if the path requires params, the init will be required
// Otherwise, Optional
type QueryServiceParams<M extends HttpMethod, P extends HttpPaths<M>> =
  HttpRequestData<M, P> extends { params: any } ? [P, HttpRequestData<M, P>] : [P] | [P, HttpRequestData<M, P>];
export function queryService<P extends HttpPaths<'get'>, Media extends MediaType = 'application/json'>(
  ...[url, init]: QueryServiceParams<'get', P>
): UseQueryOptions<HttpResponseData<'get', P, Media>> {
  return { queryKey: [url, init] };
}

// This makes sure that if the path requires body, the data will be required
// Otherwise, Optional
type MutateServiceFnParams<M extends HttpMethod, P extends HttpPaths<M>> =
  HttpRequestData<M, P> extends { body: any } ? HttpRequestData<M, P> : HttpRequestData<M, P> | null;
export function mutateService<
  M extends HttpMethod,
  P extends HttpPaths<M>,
  Media extends MediaType = 'application/json',
>(...[method, url]: [M, P]): UseMutationOptions<HttpResponseData<M, P, Media>, never, MutateServiceFnParams<M, P>> {
  return {
    mutationKey: [url],
    mutationFn: async (options) => clientFetch(...([method, url, options] as ClientFetchParams<M, P>)),
  };
}

export const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      throwOnError: true,
      retry: isServer ? false : undefined,
      queryFn: (context) => {
        const [url, init] = context.queryKey;
        // TODO: validating the shape of the queryKey
        return clientFetch('get', url as HttpPaths<'get'>, init as never);
      },
    },
  },
});
