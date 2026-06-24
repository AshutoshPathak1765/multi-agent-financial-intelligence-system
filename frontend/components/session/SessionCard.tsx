import { Card } from "@/components/ui/card";

interface SessionCardProps {
  title: string;
  updatedAt: string;
}

export function SessionCard({
  title,
  updatedAt,
}: SessionCardProps) {
  return (
    <Card className="cursor-pointer p-3 hover:bg-zinc-800 transition-colors">
      <p className="font-medium text-sm truncate">
        {title}
      </p>

      <p className="text-xs text-muted-foreground mt-1">
        {updatedAt}
      </p>
    </Card>
  );
}