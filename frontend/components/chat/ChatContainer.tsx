"use client";

import { ChatInput } from "./ChatInput";
import { ChatWindow } from "./ChatWindow";

import { useParams } from "next/navigation";
import { useChat } from "@/hooks/useChat";
import { useMessages } from "@/hooks/useMessages";

export function ChatContainer() {

  const params = useParams();

  const sessionId = params.sessionId as string;

  const { chatMutation } = useChat(sessionId);

  const { messagesQuery } = useMessages(sessionId);

  return (
    <div className="flex h-full min-h-0 flex-col">
      <ChatWindow 
      messagesQuery={messagesQuery}
      isThinking={chatMutation.isPending}
      />
      <ChatInput 
        sessionId={sessionId}
        chatMutation={chatMutation} />
    </div>
  );
}