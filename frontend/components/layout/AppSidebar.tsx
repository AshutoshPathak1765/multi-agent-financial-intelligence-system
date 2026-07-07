"use client";
import { ScrollArea } from "@/components/ui/scroll-area";
import { NewChatButton } from "@/components/session/NewChatButton";
import { SessionCard } from "@/components/session/SessionCard";
import { useSessions } from "@/hooks/useSessions";
import { usePathname, useRouter } from "next/navigation";

export function AppSidebar() {
  const { sessionsQuery } = useSessions();
  const router = useRouter();
  const pathname = usePathname();
 
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
    <aside className="hidden md:flex w-72 min-h-0 flex-col border-r border-zinc-800 bg-zinc-900">
      <div className="p-4">
        <NewChatButton />
      </div>
    <div className="px-4 pb-2">
    <p className="text-xs font-medium text-muted-foreground uppercase tracking-wide">
    Recent Chats
    </p>
    </div>
    <div className="flex-1 min-h-0">
      <ScrollArea className="h-full px-4">
        <div className="space-y-2 pb-4">
         {sessionsQuery.data?.map((session) => (
          <SessionCard
          key={session.id}
          id={session.id}
          title={session.title}
          updatedAt={new Date(session.created_at).toLocaleDateString()}
          isActive={pathname === `/chat/${session.id}`}
          onClick={() => router.push(`/chat/${session.id}`)}
        />
      ))}
        </div>
      </ScrollArea>
      </div>
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