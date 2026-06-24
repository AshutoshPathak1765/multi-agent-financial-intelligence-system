import {
  Avatar,
  AvatarFallback,
} from "@/components/ui/avatar";

import { Card } from "@/components/ui/card";

import { ExecutionDetails } from "./ExecutionDetails";

interface ChatMessageProps {
  role: "user" | "assistant";
  content: string;
}

export function ChatMessage({
  role,
  content,
}: ChatMessageProps) {
  const isUser = role === "user";

  return (
    <div
      className={`flex gap-3 ${
        isUser
          ? "justify-end"
          : "justify-start"
      }`}
    >
      {!isUser && (
        <Avatar>
          <AvatarFallback>AI</AvatarFallback>
        </Avatar>
      )}

     <Card
  className={`
    max-w-3xl p-4
    ${
      isUser
        ? "bg-emerald-600 text-white border-emerald-600"
        : "bg-zinc-900 border-zinc-800"
    }
  `}
>
  <div className="max-w-3xl">
    <p className="leading-7">
      {content}
    </p>
  </div>

  {!isUser && (
    <ExecutionDetails />
  )}
  </Card>
    </div>
  );
}