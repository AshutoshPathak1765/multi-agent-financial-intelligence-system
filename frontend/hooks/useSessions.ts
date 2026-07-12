"use client";

import {
  useMutation,
  useQuery,
  useQueryClient,
} from "@tanstack/react-query";

import { useApiClient } from "./useApiClient";

import {
  createSession,
  getSessions,
  updateSession,
  deleteSession,
} from "@/lib/api/session";

import type {
  CreateSessionRequest,
  UpdateSessionRequest,
} from "@/lib/api/types";

const SESSION_QUERY_KEY = ["sessions"] as const;

export function useSessions() {
  const api = useApiClient();
  const queryClient = useQueryClient();

  const sessionsQuery = useQuery({
    queryKey: SESSION_QUERY_KEY,
    queryFn: () => getSessions(api),
  });

  const createSessionMutation = useMutation({
    mutationFn: (data: CreateSessionRequest) =>
      createSession(api, data),

    onSuccess: () => {
      queryClient.invalidateQueries({
        queryKey: SESSION_QUERY_KEY,
      });
    },
  });

  const updateSessionMutation = useMutation({
  mutationFn: ({
    sessionId,
    data,
  }: {
    sessionId: string;
    data: UpdateSessionRequest;
  }) => updateSession(api, sessionId, data),

  onSuccess: () => {
    queryClient.invalidateQueries({
      queryKey: SESSION_QUERY_KEY,
    });
  },
});

const deleteSessionMutation = useMutation({
  mutationFn: (sessionId: string) =>
    deleteSession(api, sessionId),

  onSuccess: () => {
    queryClient.invalidateQueries({
      queryKey: SESSION_QUERY_KEY,
    });
  },
});

 
  return {
    sessionsQuery,
    createSessionMutation,
    updateSessionMutation,
    deleteSessionMutation
  };
}