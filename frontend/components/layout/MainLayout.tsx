import { ReactNode } from "react";
import { AppHeader } from "./AppHeader";
import { AppSidebar } from "./AppSidebar";

interface MainLayoutProps {
  children: ReactNode;
}

export function MainLayout({ children }: MainLayoutProps) {
  return (
    <div className="h-screen bg-zinc-950 text-zinc-100">
      <AppHeader />

      <div className="flex h-[calc(100vh-56px)]">
        <AppSidebar />

        <main className="flex-1 overflow-hidden">
          {children}
        </main>
      </div>
    </div>
  );
}