"use client";

import { Send } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { Textarea } from "@/components/ui/textarea";
import { UseMutationResult } from "@tanstack/react-query";
import type { ChatRequest, ChatResponse } from "@/lib/api/types";
import { useEffect, useRef, useState } from "react";

interface ChatInputProps {
  sessionId: string;
  chatMutation: UseMutationResult<
    ChatResponse,
    Error,
    ChatRequest
  >;
}

export function ChatInput({
  sessionId,
  chatMutation,
}: ChatInputProps) {

  const [message, setMessage] = useState("");
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  const handleSubmit = () => {
    const trimmedMessage = message.trim();

    if (!trimmedMessage) {
      return;
    }

  chatMutation.mutate({
    session_id: sessionId,
    message: trimmedMessage,
  },
{
  onSuccess: () => {
    setMessage("");
  },
});
};

const handleKeyDown = (
  e: React.KeyboardEvent<HTMLTextAreaElement>
) => {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    handleSubmit();
  }
};

useEffect(() => {
  const textarea = textareaRef.current;

  if (!textarea) {
    return;
  }

  textarea.style.height = "0px";

  const scrollHeight = textarea.scrollHeight;

  textarea.style.height =
    Math.min(scrollHeight, 200) + "px";
}, [message]);

  return (
    <div className="border-t border-zinc-800 p-4">
      <div className="mx-auto max-w-4xl">
       <Card className="border-zinc-800 bg-zinc-900 p-3">
        <div className="relative">
          <Textarea
          ref={textareaRef}
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          onKeyDown={handleKeyDown}
          disabled={chatMutation.isPending}
          placeholder="Ask about a company or financial report..."
          className="
              min-h-52px
              max-h-200px
              overflow-y-auto
              resize-none
              border-0
              pr-14
              bg-transparent
              focus-visible:ring-0
            "
          />
            <Button size="icon" 
            onClick={handleSubmit}
            disabled={chatMutation.isPending}
             className="
              absolute
              right-3
              top-1/2
              -translate-y-1/2
              rounded-full
            "
            >
              <Send className="h-4 w-4" />
            </Button>
          </div>
        </Card>
      </div>
    </div>
  );
}