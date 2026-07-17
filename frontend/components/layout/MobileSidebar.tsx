"use client";

import { Menu } from "lucide-react";
import { usePathname, useRouter } from "next/navigation";
import { formatDistanceToNow } from "date-fns";

import {
  Sheet,
  SheetContent,
  SheetTrigger,
} from "@/components/ui/sheet";

import { Button } from "@/components/ui/button";
import { SessionCard } from "@/components/session/SessionCard";
import { NewChatButton } from "@/components/session/NewChatButton";
import { Skeleton } from "@/components/ui/skeleton";

import { useSessions } from "@/hooks/useSessions";

export function MobileSidebar() {
  const { sessionsQuery } = useSessions();
  const router = useRouter();
  const pathname = usePathname();

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

      <SheetContent side="left" className="w-80 p-0">
        <div className="flex h-full flex-col">
          <div className="p-4">
            <NewChatButton />
          </div>

          <div className="px-4 pb-2">
            <p className="text-xs font-medium uppercase tracking-wide text-muted-foreground">
              Recent Chats
            </p>
          </div>

          <div className="flex-1 overflow-y-auto px-4 pb-4">
            {sessionsQuery.isLoading ? (
              <div className="space-y-2">
                {Array.from({ length: 6 }).map((_, index) => (
                  <Skeleton
                    key={index}
                    className="h-16 w-full rounded-xl"
                  />
                ))}
              </div>
            ) : sessionsQuery.error ? (
              <div className="text-sm text-muted-foreground">
                Failed to load sessions.
              </div>
            ) : (
              <div className="space-y-2">
                {sessionsQuery.data?.map((session) => (
                  <SessionCard
                    key={session.id}
                    id={session.id}
                    title={session.title}
                    updatedAt={formatDistanceToNow(
                      new Date(session.created_at + "Z"),
                      { addSuffix: true }
                    )}
                    isActive={pathname === `/chat/${session.id}`}
                    onClick={() => {
                      router.push(`/chat/${session.id}`);
                    }}
                  />
                ))}
              </div>
            )}
          </div>
        </div>
      </SheetContent>
    </Sheet>
  );
}