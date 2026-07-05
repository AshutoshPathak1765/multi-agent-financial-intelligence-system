"use client";

import { Send } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { Textarea } from "@/components/ui/textarea";
import { useParams } from "next/navigation";
import { useChat } from "@/hooks/useChat";
import { useState } from "react";

export function ChatInput() {
  const params = useParams();
  const sessionId = params?.sessionId as string;
  console.log("params:", params);
  console.log("sessionId:", sessionId);
  const { chatMutation } = useChat(sessionId);
  const [message, setMessage] = useState("");

  const handleSubmit = () => {
    const trimmedMessage = message.trim();

    if (!trimmedMessage) {
      return;
    }

  chatMutation.mutate({
    session_id: sessionId as string,
    message: trimmedMessage,
  },
{
  onSuccess: () => {
    setMessage("");
  },
});
};

  return (
    <div className="border-t border-zinc-800 p-4">
      <div className="mx-auto max-w-4xl">
        <Card className="bg-zinc-900 border-zinc-800 p-3">
          <Textarea
          value={message}
          onChange={(e) => setMessage(e.target.value)}
            placeholder="Ask about earnings reports, quarterly filings, revenue growth..."
            className="
              min-h-60
              max-h-200
              resize-none
              border-0
              bg-transparent
              focus-visible:ring-0
            "
          />

          <div className="mt-3 flex justify-end">
            <Button size="icon" 
            onClick={handleSubmit}
            disabled={chatMutation.isPending}>
              <Send className="h-4 w-4" />
            </Button>
          </div>
        </Card>
      </div>
    </div>
  );
}