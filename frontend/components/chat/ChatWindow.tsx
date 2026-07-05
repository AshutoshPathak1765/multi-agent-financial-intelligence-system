"use client";
import { ScrollArea } from "@/components/ui/scroll-area";

import { ChatMessage } from "./ChatMessage";
import { EmptyState } from "./EmptyState";
import { useParams } from "next/navigation";
import { useMessages } from "@/hooks/useMessages";


export function ChatWindow() {
  const params = useParams();

  const sessionId = params.sessionId as string;

  const { messagesQuery } = useMessages(sessionId);

  if (messagesQuery.isLoading) {
  return <div>Loading...</div>;
}

if (messagesQuery.error) {
  return <div>Failed to load messages.</div>;
}

if (!messagesQuery.data?.length) {
    return <EmptyState />;
}
  return (
    <ScrollArea className="flex-1">
      <div className="mx-auto w-full max-w-4xl px-6 py-8">
        <div className="space-y-6">
          {
            messagesQuery.data.map((message) => (
              <ChatMessage
                  key={message.id}
                  role={message.role}
                  content={message.content}
              />
          ))
          }
        </div>
      </div>
    </ScrollArea>
  );
}