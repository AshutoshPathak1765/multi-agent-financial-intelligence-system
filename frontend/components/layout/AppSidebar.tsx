"use client";
import { ScrollArea } from "@/components/ui/scroll-area";
import { NewChatButton } from "@/components/session/NewChatButton";
import { SessionCard } from "@/components/session/SessionCard";
import { useSessions } from "@/hooks/useSessions";
import { usePathname, useRouter } from "next/navigation";
import { Skeleton } from "@/components/ui/skeleton";
import { formatDistanceToNow } from "date-fns";
import {useUser} from "@clerk/nextjs";


export function AppSidebar() {
  const { sessionsQuery } = useSessions();
  const router = useRouter();
  const pathname = usePathname();
  const { user } = useUser();

  const displayName =
  user?.fullName ||
  user?.firstName ||
  user?.primaryEmailAddress?.emailAddress ||
  "User";
 
  if (sessionsQuery.isLoading) {
  return (
    <aside className="hidden md:flex w-72 flex-col border-r border-zinc-800 bg-zinc-900 p-4">
      <Skeleton className="h-11 w-full rounded-lg" />

      <div className="mt-6 space-y-3">
        {Array.from({ length: 6 }).map((_, index) => (
          <Skeleton
            key={index}
            className="h-16 w-full rounded-xl"
          />
        ))}
      </div>
    </aside>
  );
}

if (sessionsQuery.error) {
    return (
        <aside className="hidden md:flex w-64 border-r border-zinc-800 bg-zinc-900">
            Failed to load sessions.
        </aside>
    );
}
  return (
    <aside className="hidden md:flex w-80 min-h-0 flex-col border-r border-zinc-800 bg-zinc-900">
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
          updatedAt={formatDistanceToNow(new Date(session.created_at + "Z"),{addSuffix: true,})}
          isActive={pathname === `/chat/${session.id}`}
          onClick={() => router.push(`/chat/${session.id}`)}
        />
      ))}
        </div>
      </ScrollArea>
      </div>
      <div className="border-t border-zinc-800 p-4">
    <div className="text-sm font-medium">
      {displayName}
    </div>

  <div className="text-xs text-muted-foreground">
    Free Plan
  </div>
  </div>
    </aside>
  );
}