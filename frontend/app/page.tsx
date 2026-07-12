import { MainLayout } from "@/components/layout/MainLayout";
import { EmptyState } from "@/components/chat/EmptyState";


export default function Home() {
  return (
    <MainLayout>
      <EmptyState />
    </MainLayout>
  );
}