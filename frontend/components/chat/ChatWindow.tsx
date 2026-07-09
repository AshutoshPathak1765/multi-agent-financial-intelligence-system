"use client";
import { ScrollArea } from "@/components/ui/scroll-area";

import { ChatMessage } from "./ChatMessage";
import { EmptyState } from "./EmptyState";
import type { UseQueryResult } from "@tanstack/react-query";
import { useEffect, useRef } from "react";
import type { MessageResponse } from "@/lib/api/types";
import { ThinkingMessage } from "./ThinkingMessage";
import { ChatSkeleton } from "./ChatSkeleton";

interface ChatWindowProps {
    messagesQuery: UseQueryResult<MessageResponse[], Error>;
    isThinking: boolean;
}


export function ChatWindow({
    messagesQuery,
    isThinking,
}: ChatWindowProps) {

  const bottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
  bottomRef.current?.scrollIntoView({
    behavior: messagesQuery.data?.length ? "smooth" : "auto"
  });
}, [messagesQuery.data?.length, isThinking]);

  if (messagesQuery.isLoading) {
  return <ChatSkeleton />;
}

if (messagesQuery.error) {
  return <div>Failed to load messages.</div>;
}

if (!messagesQuery.data?.length && !isThinking) {
    return <EmptyState />;
}
  return (
    <div className="flex-1 min-h-0">
    <ScrollArea className="h-full">
      <div className="mx-auto w-full max-w-4xl px-6 py-8">
        <div className="space-y-6">
          {
            messagesQuery.data?.map((message) => (
              <ChatMessage
                  key={message.id}
                  role={message.role}
                  content={message.content}
              />
          ))
          }
          {isThinking && <ThinkingMessage />}
      <div ref={bottomRef} />
        </div>
      </div>
    </ScrollArea>
    </div>
  );
}