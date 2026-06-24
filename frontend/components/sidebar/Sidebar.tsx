import { NewChatButton } from "./NewChatButton";
import { SessionItem } from "./SessionItem";

const sessions = [
  "Tesla Revenue Analysis",
  "Apple Earnings Report",
  "Nvidia Growth Trends",
];

export function Sidebar() {
  return (
    <aside className="w-72 border-r bg-zinc-950 h-screen p-4">
      <NewChatButton />

      <div className="space-y-2">
        {sessions.map((session) => (
          <SessionItem
            key={session}
            title={session}
          />
        ))}
      </div>
    </aside>
  );
}