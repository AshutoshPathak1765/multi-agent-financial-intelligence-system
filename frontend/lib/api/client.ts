import { API_BASE_URL } from "./config";

type GetToken = () => Promise<string | null | undefined>;

type HttpMethod =
  | "GET"
  | "POST"
  | "PUT"
  | "PATCH"
  | "DELETE";

export function createApiClient(
  getToken: GetToken
) {
  async function request<T>(
    method: HttpMethod,
    path: string,
    body?: unknown,
  ): Promise<T> {

    const token = await getToken();

    if (!token) {
      throw new Error("User is not authenticated.");
    }

    const response = await fetch(
      `${API_BASE_URL}${path}`,
      {
        method,
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json",
        },
        body: body ? JSON.stringify(body) : undefined,
      }
    );

  if (!response.ok) {
  let message = "Something went wrong.";

  try {
    const error = await response.json();
    message = error.detail ?? message;
  } catch {
    // Ignore JSON parsing errors
  }

  throw new Error(message);
}

if (response.status === 204) {
  return undefined as T;
}

return response.json() as Promise<T>;

}

async function stream(
  path: string,
  body: unknown,
): Promise<Response> {

  const token = await getToken();

  if (!token) {
    throw new Error("User is not authenticated.");
  }

  const response = await fetch(
    `${API_BASE_URL}${path}`,
    {
      method: "POST",
      headers: {
        Authorization: `Bearer ${token}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    }
  );

  if (!response.ok) {
    throw new Error("Streaming request failed.");
  }

  return response;
}

  return {
    get: <T>(path: string) =>
      request<T>("GET", path),

    post: <T>(
      path: string,
      body: unknown,
    ) =>
      request<T>("POST", path, body),

    put: <T>(
      path: string,
      body: unknown,
    ) =>
      request<T>("PUT", path, body),

    patch: <T>(
      path: string,
      body: unknown,
    ) =>
      request<T>("PATCH", path, body),

    delete: <T>(path: string) =>
      request<T>("DELETE", path),
    stream,
  };
}