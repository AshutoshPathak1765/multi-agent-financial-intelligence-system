"use client";
import { Plus } from "lucide-react";

import { Button } from "@/components/ui/button";
import { useSessions } from "@/hooks/useSessions";

export function NewChatButton() {
  const { createSessionMutation } = useSessions();

  const handleClick = () => {
  createSessionMutation.mutate({
    title: "New Chat",
  });
};

  return (
    <Button
      className="w-full justify-start gap-2"
      size="lg"
      onClick={handleClick}
    >
      <Plus size={16} />
      {
        createSessionMutation.isPending ? 
          "Creating..." :  "New Chat"
      }
     
    </Button>
  );
}