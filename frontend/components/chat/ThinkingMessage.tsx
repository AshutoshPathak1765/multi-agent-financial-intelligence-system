import {
  Avatar,
  AvatarFallback,
} from "@/components/ui/avatar";

import { Card } from "@/components/ui/card";

export function ThinkingMessage() {
  return (
    <div className="flex gap-3">
      <Avatar>
        <AvatarFallback>AI</AvatarFallback>
      </Avatar>

      <Card className="max-w-3xl border-zinc-800 bg-zinc-900 p-4">
        <p className="text-zinc-400">
          Thinking...
        </p>
      </Card>
    </div>
  );
}