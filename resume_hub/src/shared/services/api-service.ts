import { StatusCodes } from 'http-status-codes';
import { redirect } from 'next/navigation';
import createClient, {
  type ClientMethod,
  type FetchOptions,
  type FetchResponse,
  type HeadersOptions,
} from 'openapi-fetch';
import type { FilterKeys, HttpMethod, MediaType, PathsWithMethod as PathsWith } from 'openapi-typescript-helpers';

import { RESUME_MANAGER_BASE_API_URL, isServer } from 'src/configs';
import { LocaleService, TokenStorage } from 'src/shared/utils';

import type { paths as ResumeManager } from './.generated/types/resume-manager';
import { type APIServicesCombinedErrors, HttpError } from './api-service-errors';

type ApiServices = 'resume-manager';
type PathGen<BasePath extends `${ApiServices}:`, Paths> = {
  [k in keyof Paths & string as `${BasePath}${k}`]: Paths[k];
};
type Paths = PathGen<'resume-manager:', ResumeManager>;

export type HttpPaths<M extends HttpMethod> = PathsWith<Paths, M>;
export type HttpRequestData<M extends HttpMethod, P extends HttpPaths<M>> = FetchOptions<FilterKeys<Paths[P], M>>;

type OpenapiResponse<M extends HttpMethod, P extends HttpPaths<M>, Media extends MediaType> = NonNullable<
  FetchResponse<M extends keyof Paths[P] ? Paths[P][keyof Paths[P] & M] : unknown, object, Media>
>;
export type HttpResponseData<M extends HttpMethod, P extends HttpPaths<M>, Media extends MediaType> = NonNullable<
  OpenapiResponse<M, P, Media>['data']
>;

const apiMappings: Record<ApiServices, string> = {
  'resume-manager': RESUME_MANAGER_BASE_API_URL,
};

/**
 *
 * @param path The path of the request that is exists in the Paths.
 * @returns The path value which the : after the service name is replaced with /.
 * @example getRequestPath('sample:/'): 'sample/'
 * @example getRequestPath('sample:/pets'): 'sample/pets'
 */
function getRequestPath(path: keyof Paths) {
  const [service, ...pathname] = path.split(':');
  return `${apiMappings[service as ApiServices]}${pathname.join(':')}`;
}

const client = createClient<Paths>();

export type ClientFetchParams<M extends HttpMethod, P extends HttpPaths<M>> =
  HttpRequestData<M, P> extends { params: any } | { body: any }
    ? [M, P, HttpRequestData<M, P>]
    : [M, P] | [M, P, HttpRequestData<M, P>];
export async function clientFetch<
  M extends HttpMethod,
  P extends HttpPaths<M>,
  Media extends MediaType = 'application/json',
>(
  ...[method, url, options = {} as HttpRequestData<M, P>]: ClientFetchParams<M, P>
): Promise<HttpResponseData<M, P, Media>> {
  try {
    // Inject Accept Language Header only if it's not provided and we are not in the server.
    // To use it in the server, one must provide it in the options.

    options.headers = injectFieldsToRequestHeaders(options.headers, {
      key: 'Accept-Language',
      value: LocaleService.getLocale(),
    });

    const accessToken = TokenStorage.get('access-token');
    accessToken &&
      injectFieldsToRequestHeaders(options.headers, { key: 'Authorization', value: `Bearer ${accessToken}` });

    const { data, error, response } = (await (
      client[method.toUpperCase() as Uppercase<M>] as ClientMethod<any, HttpMethod, MediaType>
    )(getRequestPath(url), options)) as OpenapiResponse<M, P, Media>;

    if (error) {
      if (typeof error === 'string') {
        throw new HttpError({ status: false, message: error, status_code: response.status });
      }

      // Refresh The token and Retry
      if (response.status === StatusCodes.UNAUTHORIZED) {
        const refreshToken = TokenStorage.get('refresh-token');
        if (refreshToken) {
          const refreshTokenResponse = await client.POST('resume-manager:/v1/users/token/refresh', {
            body: { refresh: refreshToken },
          });
          if (refreshTokenResponse.data) {
            const { access: newAccessToken } = refreshTokenResponse.data;

            options.headers = injectFieldsToRequestHeaders(options.headers, {
              key: 'Authorization',
              value: `Bearer ${newAccessToken}`,
            });
            const retryResponse = (await (
              client[method.toUpperCase() as Uppercase<M>] as ClientMethod<any, HttpMethod, Media>
            )(getRequestPath(url), options)) as OpenapiResponse<M, P, Media>;

            if (retryResponse.data) {
              TokenStorage.set('access-token', newAccessToken);
              TokenStorage.set('refresh-token', refreshToken);

              return retryResponse as HttpResponseData<M, P, Media>;
            }
          }
        }

        TokenStorage.empty();
        if (isServer) {
          redirect('/auth/login');
        } else {
          window.location.pathname = '/auth/login';
        }
      }

      throw new HttpError({ ...error, status_code: response.status } as unknown as APIServicesCombinedErrors);
    }

    return data as HttpResponseData<M, P, Media>;
  } catch (error) {
    console.log(error);
    if (error instanceof HttpError) {
      throw error;
    }

    // In case the openapi itself throws an error.
    // Like making request without a network

    // The `${error}` makes sure that the message value is a string
    throw new HttpError({ status: false, message: `${error}`, status_code: StatusCodes.INTERNAL_SERVER_ERROR });
  }
}

function injectFieldsToRequestHeaders(
  header: HeadersOptions | undefined,
  // The value type is based on the type in the
  ...fields: { key: string; value: string }[]
): HeadersOptions {
  if (header instanceof Headers) {
    fields.forEach(({ key, value }) => {
      header.set(key, value);
    });

    return header;
  }

  if (Array.isArray(header)) {
    return [...header, ...fields.map<[string, string]>(({ key, value }) => [key, value])];
  }

  return { ...(header || {}), ...fields.reduce((result, { key, value }) => ({ ...result, [key]: value }), {}) };
}
