import { Plus } from "lucide-react";
import { Button } from "@/components/ui/button";

export function NewChatButton() {
  return (
    <Button className="w-full justify-start gap-2">
      <Plus size={16} />
      New Chat
    </Button>
  );
}