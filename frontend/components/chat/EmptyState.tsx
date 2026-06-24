import { Badge } from "@/components/ui/badge";
import { Card } from "@/components/ui/card";

const suggestions = [
  "Analyze Tesla Q1 earnings",
  "Compare Apple and Microsoft revenue",
  "Summarize Nvidia quarterly filing",
  "Identify growth risks in Tesla reports",
];

export function EmptyState() {
  return (
    <div className="flex flex-1 items-center justify-center p-6">
      <div className="max-w-3xl w-full space-y-6">
        <div className="text-center">
          <h2 className="text-3xl font-bold">
            Financial Research Assistant
          </h2>

          <p className="mt-3 text-muted-foreground">
            Analyze earnings reports, compare companies,
            review quarterly filings and discover market insights.
          </p>

          <div className="mt-4 flex justify-center gap-2 flex-wrap">
            <Badge variant="secondary">LangGraph</Badge>
            <Badge variant="secondary">RAG</Badge>
            <Badge variant="secondary">Multi-Agent</Badge>
          </div>
        </div>

        <div className="grid gap-3 md:grid-cols-2">
          {suggestions.map((prompt) => (
            <Card
              key={prompt}
              className="cursor-pointer p-4 bg-zinc-900 border-zinc-800 hover:bg-zinc-800 transition-colors"
            >
              <p className="text-sm">{prompt}</p>
            </Card>
          ))}
        </div>
      </div>
    </div>
  );
}