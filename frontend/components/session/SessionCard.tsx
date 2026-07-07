import { Card } from "@/components/ui/card";

interface SessionCardProps {
  id: string;
  title: string;
  updatedAt: string;
  onClick: () => void;
  isActive: boolean;
}

export function SessionCard({
  title,
  updatedAt,
  isActive,
  onClick,
}: SessionCardProps) {
  return (
    <Card onClick={onClick} className={`
    cursor-pointer
    p-3
    transition-colors
    ${
      isActive
        ? "bg-zinc-800 border-zinc-700"
        : "hover:bg-zinc-800"
    }
  `}>
      <p className="font-medium text-sm truncate">
        {title}
      </p>

      <p className="text-xs text-muted-foreground mt-1">
        {updatedAt}
      </p>
    </Card>
  );
}