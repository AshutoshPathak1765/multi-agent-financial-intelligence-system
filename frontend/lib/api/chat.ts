import { createApiClient } from "./client";
import type {
  ChatRequest,
  ChatResponse,
} from "@/lib/api/types";

type ApiClient = ReturnType<typeof createApiClient>;

export function chat(
  api: ApiClient,
  data: ChatRequest,
) {
  return api.post<ChatResponse>(
    "/chat",
    data,
  );
}