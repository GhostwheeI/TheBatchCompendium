import { net, ClientRequestConstructorOptions, IncomingMessage } from 'electron'

/**
 * HTTP 请求方法类型
 */
export type HttpMethod = 'GET' | 'POST' | 'PUT' | 'DELETE' | 'PATCH' | 'HEAD' | 'OPTIONS'

/**
 * 请求配置选项
 */
export interface RequestOptions {
  /** 请求 URL */
  url: string
  /** HTTP 方法 */
  method?: HttpMethod
  /** 请求头 */
  headers?: Record<string, string>
  /** 请求体数据 */
  body?: string | Buffer | object
  /** 超时时间（毫秒） */
  timeout?: number
  /** Session 实例 */
  session?: Electron.Session
  /** 分区名称 */
  partition?: string
  /** 是否使用 session cookies */
  useSessionCookies?: boolean
  /** 凭据模式 */
  credentials?: 'omit' | 'include' | 'same-origin'
  /** 跟随重定向 */
  redirect?: 'follow' | 'error' | 'manual'
}

/**
 * 响应对象
 */
export interface Response {
  /** HTTP 状态码 */
  status: number
  /** HTTP 状态消息 */
  statusText: string
  /** 响应头 */
  headers: Record<string, string[] | string>
  /** 响应数据 */
  data: string
  /** 是否成功响应 (2xx 状态码) */
  ok: boolean
  /** 获取 JSON 格式的响应数据 */
  json: <T = any>() => T
  /** 获取文本格式的响应数据 */
  text: () => string
}

/**
 * 网络请求错误
 */
export class RequestError extends Error {
  /** HTTP 状态码 */
  public statusCode?: number
  /** 响应对象 */
  public response?: Response

  constructor(message: string, statusCode?: number, response?: Response) {
    super(message)
    this.name = 'RequestError'
    this.statusCode = statusCode
    this.response = response
  }
}

/**
 * 标准化请求选项
 * @param options - 请求选项
 * @returns 标准化的请求选项
 */
function normalizeOptions(
  options: string | RequestOptions,
): Required<
  Omit<
    RequestOptions,
    'body' | 'session' | 'partition' | 'useSessionCookies' | 'credentials' | 'redirect'
  >
> &
  Pick<
    RequestOptions,
    'body' | 'session' | 'partition' | 'useSessionCookies' | 'credentials' | 'redirect'
  > {
  const opts = typeof options === 'string' ? { url: options } : options

  return {
    method: 'GET',
    headers: {},
    timeout: 30000,
    ...opts,
  }
}

/**
 * 发起 HTTP/HTTPS 请求
 * @param options - 请求选项或 URL 字符串
 * @returns Promise<Response> 响应对象
 * @example
 * // 基本用法
 * const response = await request('https://api.example.com/data');
 * const data = response.json();
 *
 * // POST 请求
 * const response = await request({
 *   url: 'https://api.example.com/users',
 *   method: 'POST',
 *   body: { name: 'John', email: 'john@example.com' },
 *   headers: { 'Authorization': 'Bearer token' }
 * });
 *
 * // 带超时的请求
 * const response = await request({
 *   url: 'https://api.example.com/data',
 *   timeout: 5000
 * });
 */
async function request(options: string | RequestOptions): Promise<Response> {
  const config = normalizeOptions(options)

  return new Promise((resolve, reject) => {
    try {
      const req = net.request(config as ClientRequestConstructorOptions)

      // 设置请求头
      if (config.headers) {
        Object.keys(config.headers).forEach((key) => {
          req.setHeader(key, config.headers![key])
        })
      }

      // 超时处理
      let timeoutId: NodeJS.Timeout | null = null
      if (config.timeout && config.timeout > 0) {
        timeoutId = setTimeout(() => {
          req.abort()
          reject(new RequestError('Request timeout'))
        }, config.timeout)
      }

      // 处理响应
      req.on('response', (response: IncomingMessage) => {
        // 清除超时定时器
        if (timeoutId) {
          clearTimeout(timeoutId)
          timeoutId = null
        }

        let data = ''

        response.on('data', (chunk: Buffer) => {
          data += chunk.toString()
        })

        response.on('end', () => {
          const result: Response = {
            status: response.statusCode,
            statusText: response.statusMessage || '',
            headers: response.headers,
            data,
            ok: response.statusCode >= 200 && response.statusCode < 300,
            json: <T = any>(): T => {
              try {
                return JSON.parse(data) as T
              } catch (e) {
                throw new RequestError(
                  'Response body is not valid JSON',
                  response.statusCode,
                  result,
                )
              }
            },
            text: () => data,
          }

          if (result.ok) {
            resolve(result)
          } else {
            const error = new RequestError(
              `HTTP ${response.statusCode}: ${response.statusMessage || 'Unknown Error'}`,
              response.statusCode,
              result,
            )
            reject(error)
          }
        })
      })

      // 错误处理
      req.on('error', (error: Error) => {
        // 清除超时定时器
        if (timeoutId) {
          clearTimeout(timeoutId)
          timeoutId = null
        }
        reject(new RequestError(`Network error: ${error.message}`))
      })

      // 发送请求体
      if (config.body) {
        if (typeof config.body === 'object' && !(config.body instanceof Buffer)) {
          if (!config.headers || !config.headers['Content-Type']) {
            req.setHeader('Content-Type', 'application/json')
          }
          req.write(JSON.stringify(config.body))
        } else {
          req.write(config.body as string | Buffer)
        }
      }

      req.end()
    } catch (error) {
      reject(new RequestError(`Request setup failed: ${(error as Error).message}`))
    }
  })
}

/**
 * 发起 GET 请求
 * @param url - 请求 URL
 * @param options - 额外的请求选项
 * @returns Promise<Response> 响应对象
 * @example
 * const response = await request.get('https://api.example.com/users');
 * const users = response.json();
 */
request.get = async (
  url: string,
  options: Omit<RequestOptions, 'url' | 'method' | 'body'> = {},
): Promise<Response> => {
  return request({
    url,
    method: 'GET',
    ...options,
  })
}

/**
 * 发起 POST 请求
 * @param url - 请求 URL
 * @param body - 请求体数据
 * @param options - 额外的请求选项
 * @returns Promise<Response> 响应对象
 * @example
 * const response = await request.post('https://api.example.com/users', {
 *   name: 'John',
 *   email: 'john@example.com'
 * });
 * const newUser = response.json();
 */
request.post = async (
  url: string,
  body?: any,
  options: Omit<RequestOptions, 'url' | 'method'> = {},
): Promise<Response> => {
  return request({
    url,
    method: 'POST',
    body,
    ...options,
  })
}

/**
 * 发起 PUT 请求
 * @param url - 请求 URL
 * @param body - 请求体数据
 * @param options - 额外的请求选项
 * @returns Promise<Response> 响应对象
 * @example
 * const response = await request.put('https://api.example.com/users/1', {
 *   name: 'John Updated',
 *   email: 'john.updated@example.com'
 * });
 * const updatedUser = response.json();
 */
request.put = async (
  url: string,
  body?: any,
  options: Omit<RequestOptions, 'url' | 'method'> = {},
): Promise<Response> => {
  return request({
    url,
    method: 'PUT',
    body,
    ...options,
  })
}

/**
 * 发起 DELETE 请求
 * @param url - 请求 URL
 * @param options - 额外的请求选项
 * @returns Promise<Response> 响应对象
 * @example
 * const response = await request.delete('https://api.example.com/users/1');
 * if (response.ok) {
 *   console.log('User deleted successfully');
 * }
 */
request.delete = async (
  url: string,
  options: Omit<RequestOptions, 'url' | 'method'> = {},
): Promise<Response> => {
  return request({
    url,
    method: 'DELETE',
    ...options,
  })
}

/**
 * 发起 PATCH 请求
 * @param url - 请求 URL
 * @param body - 请求体数据
 * @param options - 额外的请求选项
 * @returns Promise<Response> 响应对象
 * @example
 * const response = await request.patch('https://api.example.com/users/1', {
 *   name: 'John Partially Updated'
 * });
 * const updatedUser = response.json();
 */
request.patch = async (
  url: string,
  body?: any,
  options: Omit<RequestOptions, 'url' | 'method'> = {},
): Promise<Response> => {
  return request({
    url,
    method: 'PATCH',
    body,
    ...options,
  })
}

/**
 * 发起 HEAD 请求
 * @param url - 请求 URL
 * @param options - 额外的请求选项
 * @returns Promise<Response> 响应对象
 * @example
 * const response = await request.head('https://api.example.com/users');
 * console.log('Headers:', response.headers);
 */
request.head = async (
  url: string,
  options: Omit<RequestOptions, 'url' | 'method' | 'body'> = {},
): Promise<Response> => {
  return request({
    url,
    method: 'HEAD',
    ...options,
  })
}

export default request
