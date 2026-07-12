"use client";

import { useState } from "react";
import { useApiClient } from "./useApiClient";

interface UseChatStreamProps {
  sessionId: string;
}

export function useChatStream({
  sessionId,
}: UseChatStreamProps) {
  const api = useApiClient();

  const [isStreaming, setIsStreaming] = useState(false);
  const [streamingMessage, setStreamingMessage] = useState("");

  async function sendMessage(message: string): Promise<void> {
    setIsStreaming(true);
    setStreamingMessage("");

    try {
      const response = await api.stream(
        "/chat/stream",
        {
          session_id: sessionId,
          message,
        }
      );

      if (!response.body) {
        throw new Error("No response body.");
      }

      const reader = response.body.getReader();
      const decoder = new TextDecoder();

      let pendingResponse = "";

      while (true) {
        const { done, value } = await reader.read();

        if (done) break;

        pendingResponse += decoder.decode(value, {
          stream: true,
        });

        setStreamingMessage(pendingResponse);

        await new Promise<void>((resolve) =>
          requestAnimationFrame(() => resolve())
        );
        }
        } 
          catch (error) {
          setStreamingMessage("");
          throw error;
          }
          finally {
              setIsStreaming(false);
          }
        }

  function reset() {
    setStreamingMessage("");
  }

  return {
    sendMessage,
    streamingMessage,
    isStreaming,
    reset,
  };
}