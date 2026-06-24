import { MobileSidebar } from "./MobileSidebar";
import { UserButton,Show,SignInButton } from "@clerk/nextjs";

export function AppHeader() {
  return (
    <header className="h-14 border-b border-zinc-800 px-6 flex items-center justify-between">
     <div className="flex items-center gap-3">
    <MobileSidebar />

    <div>
    <h1 className="font-semibold text-lg">
      Financial Research Assistant
    </h1>

    <p className="text-xs text-muted-foreground">
      Analyze earnings reports and company filings
    </p>
  </div>
  </div>
  <Show when="signed-in">
    <UserButton />
  </Show>
  <Show when="signed-out">
    <SignInButton />
  </Show>
  </header>
  );
}