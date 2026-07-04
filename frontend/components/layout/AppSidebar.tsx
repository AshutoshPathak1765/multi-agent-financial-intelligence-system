"use client";
import { ScrollArea } from "@/components/ui/scroll-area";
import { NewChatButton } from "@/components/session/NewChatButton";
import { SessionCard } from "@/components/session/SessionCard";
import { useSessions } from "@/hooks/useSessions";

export function AppSidebar() {
  const { sessionsQuery } = useSessions();
 
  if (sessionsQuery.isLoading) {
    return (
        <aside className="hidden md:flex w-72 border-r border-zinc-800 bg-zinc-900">
            Loading...
        </aside>
    );
}

if (sessionsQuery.error) {
    return (
        <aside className="hidden md:flex w-72 border-r border-zinc-800 bg-zinc-900">
            Failed to load sessions.
        </aside>
    );
}
  return (
    <aside className="hidden md:flex w-72 border-r border-zinc-800 bg-zinc-900 flex-col">
      <div className="p-4">
        <NewChatButton />
      </div>
    <div className="px-4 pb-2">
    <p className="text-xs font-medium text-muted-foreground uppercase tracking-wide">
    Recent Chats
    </p>
    </div>
      <ScrollArea className="flex-1 px-4">
        <div className="space-y-2 pb-4">
         {sessionsQuery.data?.map((session) => (
          <SessionCard
        key={session.id}
        title={session.title}
        updatedAt={new Date(session.created_at).toLocaleDateString()}
        />
      ))}
        </div>
      </ScrollArea>
      <div className="border-t border-zinc-800 p-4">
    <div className="text-sm font-medium">
      Ashutosh
    </div>

  <div className="text-xs text-muted-foreground">
    Free Plan
  </div>
  </div>
    </aside>
  );
}