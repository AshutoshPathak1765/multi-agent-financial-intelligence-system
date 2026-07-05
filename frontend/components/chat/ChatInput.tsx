"use client";

import { Send } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { Textarea } from "@/components/ui/textarea";
import { useParams } from "next/navigation";
import { useChat } from "@/hooks/useChat";

export function ChatInput() {
  const { sessionId } = useParams();
  const { chatMutation } = useChat(sessionId);

  const handleSubmit = () => {
    chatMutation.mutate({
        session_id: sessionId,
        message,
    });

  return (
    <div className="border-t border-zinc-800 p-4">
      <div className="mx-auto max-w-4xl">
        <Card className="bg-zinc-900 border-zinc-800 p-3">
          <Textarea
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
            <Button size="icon">
              <Send className="h-4 w-4" />
            </Button>
          </div>
        </Card>
      </div>
    </div>
  );
}