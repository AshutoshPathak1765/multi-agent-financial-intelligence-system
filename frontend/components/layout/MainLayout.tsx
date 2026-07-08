import { ReactNode } from "react";
import { AppHeader } from "./AppHeader";
import { AppSidebar } from "./AppSidebar";

interface MainLayoutProps {
  children: ReactNode;
}

export function MainLayout({ children }: MainLayoutProps) {
  return (
          <div
        className="
          h-screen
          bg-zinc-950
          text-zinc-100
          overflow-hidden
        "
      >
      <AppHeader />

      <div className="flex h-[calc(100vh-64px)]">
        <AppSidebar />

      <main
            className="
              flex-1
              overflow-hidden
              bg-zinc-950
            "
      >
          {children}
        </main>
      </div>
    </div>
  );
}