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
} from "@/lib/api/session";

import type {
  CreateSessionRequest,
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

  return {
    sessionsQuery,
    createSessionMutation,
  };
}