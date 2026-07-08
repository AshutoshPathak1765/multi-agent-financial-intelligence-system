import { MobileSidebar } from "./MobileSidebar";
import { UserButton } from "@clerk/nextjs";

export function AppHeader() {
  return (
    <header 
    className="h-16
    border-b
    border-zinc-800
    px-6
    flex
    items-center
    justify-between">
     <div className="flex items-center gap-4">
    <MobileSidebar />

    <div className="space-y-0.5">
    <h1 className="text-xl font-semibold tracking-tight">
      Financial Research Assistant
    </h1>

    <p className="text-sm text-zinc-400">
    AI-powered financial research
    </p>
  </div>
  </div>
  <div className="flex items-center gap-3">
  <UserButton />
  </div>
  </header>
  );
}