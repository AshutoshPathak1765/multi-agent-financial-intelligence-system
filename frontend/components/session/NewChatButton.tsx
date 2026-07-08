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
      size="lg"
  onClick={handleClick}
  className="
    h-11
    w-full
    justify-start
    gap-2
    rounded-xl
    border
    border-zinc-700
    bg-zinc-100
    text-zinc-900
    transition-all
    duration-200
    hover:scale-[1.01]
    hover:bg-white
    active:scale-[0.99]
  "
    >
      <Plus size={16} />
      {
        createSessionMutation.isPending ? 
          "Creating..." :  "New Chat"
      }
     
    </Button>
  );
}