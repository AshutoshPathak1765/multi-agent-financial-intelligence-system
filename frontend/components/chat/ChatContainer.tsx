"use client";

import { ChatInput } from "./ChatInput";
import { ChatWindow } from "./ChatWindow";
// import { useQueryClient } from "@tanstack/react-query";
import { useParams } from "next/navigation";
import { useMessages } from "@/hooks/useMessages";
import { useChatStream } from "@/hooks/useChatStream";
import { useEffect } from "react";

export function ChatContainer() {

  const params = useParams();

  const sessionId = params.sessionId as string;

  // const queryClient = useQueryClient();

  const {
  sendMessage,
  streamingMessage,
  isStreaming,
  reset,
} = useChatStream({
  sessionId,
});

const { messagesQuery } = useMessages(sessionId);

useEffect(() => {
  if (
    !isStreaming &&
    streamingMessage &&
    messagesQuery.data?.length
  ) {
    const lastMessage =
      messagesQuery.data[messagesQuery.data.length - 1];

    if (lastMessage.role === "assistant") {
      reset();
    }
  }
}, [
  isStreaming,
  streamingMessage,
  messagesQuery.data,
  reset,
]);

async function handleSendMessage(message: string) {
  try {
    await sendMessage(message);

    await messagesQuery.refetch();
  } catch (error) {
    console.error(error);
  }
}

  

  return (
    <div className="flex h-full min-h-0 flex-col">
      <ChatWindow 
      messagesQuery={messagesQuery}
      isThinking={false}
      isStreaming={isStreaming}
      streamingMessage={streamingMessage}
      />
      <ChatInput 
        onSendMessage={handleSendMessage}
        isSending={isStreaming}
        />
    </div>
  );
}