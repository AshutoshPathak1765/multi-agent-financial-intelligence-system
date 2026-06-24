import { ScrollArea } from "@/components/ui/scroll-area";
import { NewChatButton } from "@/components/session/NewChatButton";
import { SessionCard } from "@/components/session/SessionCard";

const sessions = [
  {
    title: "Tesla Revenue Analysis",
    updatedAt: "2h ago",
  },
  {
    title: "Apple Earnings Report",
    updatedAt: "Yesterday",
  },
  {
    title: "Nvidia Growth Trends",
    updatedAt: "2 days ago",
  },
];

export function AppSidebar() {
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
          {sessions.map((session) => (
            <SessionCard
              key={session.title}
              title={session.title}
              updatedAt={session.updatedAt}
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