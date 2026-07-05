"use client";

import { useMutation, useQueryClient } from "@tanstack/react-query";

import { useApiClient } from "./useApiClient";
import { chat } from "@/lib/api/chat";
import type { ChatRequest } from "@/lib/api/types";

export function useChat(sessionId: string) {
  const api = useApiClient();
  const queryClient = useQueryClient();

  const chatMutation = useMutation({
    mutationFn: (data: ChatRequest) =>
      chat(api, data),

    onSuccess: () => {
      queryClient.invalidateQueries({
        queryKey: ["messages", sessionId],
      });
    },
  });

  return {
    chatMutation,
  };
}