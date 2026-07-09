import {
  Avatar,
  AvatarFallback,
} from "@/components/ui/avatar";

import { Card } from "@/components/ui/card";

interface ThinkingMessageProps {
  status?: string;
}

export function ThinkingMessage({
  status = "Thinking...",
}: ThinkingMessageProps) {
  return (
    <div className="flex gap-4">
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
        <div className="space-y-3">
        <div className="flex gap-1">
          <div className="h-2 w-2 rounded-full bg-emerald-400 animate-bounce [animation-delay:-0.3s]" />
          <div className="h-2 w-2 rounded-full bg-emerald-400 animate-bounce [animation-delay:-0.15s]" />
          <div className="h-2 w-2 rounded-full bg-emerald-400 animate-bounce" />
        </div>

        <p className="text-sm text-zinc-400">
          {status}
        </p>
      </div>
      </Card>
    </div>
  );
}