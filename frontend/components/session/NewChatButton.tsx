"use client";
import { Plus } from "lucide-react";

import { Button } from "@/components/ui/button";
import { useSessions } from "@/hooks/useSessions";
import { useRouter } from "next/navigation";

export function NewChatButton() {
  const { createSessionMutation } = useSessions();
  const router = useRouter();

  const handleClick = () => {
  createSessionMutation.mutate({
    title: "New Chat",
  },
  {
    onSuccess: (session) => {
      router.push(`/chat/${session.id}`);
    },
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