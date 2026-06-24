import { Card } from "@/components/ui/card"

interface SessionItemProps {
  title: string;
}


export function SessionItem({ title }: SessionItemProps) {
  return (
    <Card className="cursor-pointer p-3 hover:bg-accent transition-colors">
      <p className="truncate text-sm">{title}</p>
    </Card>
  )
}