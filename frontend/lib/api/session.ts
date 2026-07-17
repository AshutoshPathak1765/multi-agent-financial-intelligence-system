import { createApiClient } from "./client";
import {
  CreateSessionRequest,
  SessionResponse,
  UpdateSessionRequest,
} from "@/lib/api/types";

type ApiClient = ReturnType<typeof createApiClient>;

export function createSession(
  api: ApiClient,
  data: CreateSessionRequest,
) {
  return api.post<SessionResponse>(
    "/sessions",
    data,
  );
}

export function getSessions(
  api: ApiClient,
) {
  return api.get<SessionResponse[]>(
    "/sessions",
  );
}

export async function updateSession(
  api: ApiClient,
  sessionId: string,
  data: UpdateSessionRequest,
) {
  return api.patch(
    `/sessions/${sessionId}`,
    data
  );
}

export async function deleteSession(
  api: ApiClient,
  sessionId: string,
) {
  return api.delete<void>(
    `/sessions/${sessionId}`
  );
}