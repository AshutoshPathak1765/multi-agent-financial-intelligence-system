import { createApiClient } from "./client";
import type {
  CreateMessageRequest,
  MessageResponse,
} from "@/lib/api/types";

type ApiClient = ReturnType<typeof createApiClient>;

export function getMessages(
  api: ApiClient,
  sessionId: string,
) {
  return api.get<MessageResponse[]>(
    `/messages/${sessionId}`
  );
}

export function createMessage(
  api: ApiClient,
  data: CreateMessageRequest,
) {
  return api.post<MessageResponse>(
    "/messages",
    data,
  );
}