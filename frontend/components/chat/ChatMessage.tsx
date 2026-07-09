import {
  Avatar,
  AvatarFallback,
} from "@/components/ui/avatar";

import { Card } from "@/components/ui/card";

// import { ExecutionDetails } from "./ExecutionDetails";
import { MarkdownRenderer } from "./MarkdownRenderer";

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
  className={`flex gap-4 ${
    isUser ? "justify-end" : "justify-start"
  }`}
>
  {!isUser ? (
    <>
      <Avatar>
        <AvatarFallback className="bg-emerald-500 text-white font-semibold">
          FI
        </AvatarFallback>
      </Avatar>
        <Card
          className="
            max-w-5xl
            rounded-2xl
            border
            border-zinc-800
            bg-zinc-900
            p-5
          "
        >
          <div className="leading-7">
            <MarkdownRenderer content={content} />
          </div>
        </Card>
    </>
  ) : (
    <Card
      className="
        max-w-5xl
        rounded-2xl
        border
        border-emerald-600
        bg-emerald-600
        p-5
        text-white
      "
    >
      <div className="leading-7">
        {content}
      </div>
    </Card>
  )}
</div>
  );
}