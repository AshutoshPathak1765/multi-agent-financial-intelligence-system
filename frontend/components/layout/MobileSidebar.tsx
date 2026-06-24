"use client";

import { Menu } from "lucide-react";

import {
  Sheet,
  SheetContent,
  SheetTrigger,
} from "@/components/ui/sheet";

import { Button } from "@/components/ui/button";

import { SessionCard } from "@/components/session/SessionCard";
import { NewChatButton } from "@/components/session/NewChatButton";

const sessions = [
  {
    title: "Tesla Revenue Analysis",
    updatedAt: "2h ago",
  },
  {
    title: "Apple Earnings Report",
    updatedAt: "Yesterday",
  },
];

export function MobileSidebar() {
  return (
    <Sheet>
      <SheetTrigger asChild>
        <Button
          size="icon"
          variant="ghost"
          className="md:hidden"
        >
          <Menu />
        </Button>
      </SheetTrigger>

      <SheetContent side="left">
        <div className="space-y-4">
          <NewChatButton />

          {sessions.map((session) => (
            <SessionCard
              key={session.title}
              title={session.title}
              updatedAt={session.updatedAt}
            />
          ))}
        </div>
      </SheetContent>
    </Sheet>
  );
}