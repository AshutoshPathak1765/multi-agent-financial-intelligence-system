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
    p-4
    transition-all duration-200
    ${
      isActive
        ? "bg-zinc-800/80 border-zinc-600"
        : "hover:bg-zinc-800/60 hover:border-zinc-700"
    }
  `}>
      <p className="truncate text-sm font-medium">
        {title}
      </p>

      <p className="mt-2 text-xs text-zinc-500">
        {updatedAt}
      </p>
    </Card>
  );
}