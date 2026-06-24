import { ScrollArea } from "@/components/ui/scroll-area";

import { ChatMessage } from "./ChatMessage";
import { EmptyState } from "./EmptyState";

const messages = [
  {
    role: "user" as const,
    content:
      "Compare Tesla and Apple revenue growth.",
  },
  {
    role: "assistant" as const,
    content:
      "Tesla experienced faster revenue growth while Apple demonstrated stronger stability and margins.",
  },
];

export function ChatWindow() {
  if (messages.length === 0) {
    return <EmptyState />;
  }

  return (
    <ScrollArea className="flex-1">
      <div className="mx-auto w-full max-w-4xl px-6 py-8">
        <div className="space-y-6">
          {messages.map((message, index) => (
            <ChatMessage
              key={index}
              role={message.role}
              content={message.content}
            />
          ))}
        </div>
      </div>
    </ScrollArea>
  );
}