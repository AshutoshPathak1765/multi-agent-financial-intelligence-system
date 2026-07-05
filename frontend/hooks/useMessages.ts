"use client";

import {
  useQuery,
  useMutation,
  useQueryClient,
} from "@tanstack/react-query";

import { useApiClient } from "./useApiClient";

import {
  getMessages,
  createMessage,
} from "@/lib/api/message";

import type {
  CreateMessageRequest,
} from "@/lib/api/types";

export const messagesQueryKey = (
  sessionId: string,
) => ["messages", sessionId] as const;

export function useMessages(
  sessionId: string,
) {
  const api = useApiClient();
  const queryClient = useQueryClient();

  const messagesQuery = useQuery({
    queryKey: messagesQueryKey(sessionId),
    queryFn: () => getMessages(api, sessionId),
    enabled: !!sessionId,
  });

  const createMessageMutation = useMutation({
    mutationFn: (data: CreateMessageRequest) =>
      createMessage(api, data),

    onSuccess: () => {
      queryClient.invalidateQueries({
        queryKey: messagesQueryKey(sessionId),
      });
    },
  });

  return {
    messagesQuery,
    createMessageMutation,
  };
}