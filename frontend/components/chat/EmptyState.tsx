import { Card } from "@/components/ui/card";
import { Bot } from "lucide-react";

const suggestions = [
  "Compare Apple's revenue growth with Microsoft",
  "Summarize NVIDIA's latest quarterly earnings",
  "Analyze Tesla's cash flow trends",
  "Identify financial risks in Amazon's annual report",
];

export function EmptyState() {
  return (
    <div className="flex flex-1 items-center justify-center p-6">
      <div className="max-w-3xl w-full space-y-8">
        <div className="text-center">
          <h2 className="text-4xl font-bold">
          <Bot className="mx-auto mb-6 h-12 w-12 text-emerald-400" />
            Financial Intelligence
          </h2>

          <p className="mt-3 text-muted-foreground">
            AI-powered financial research for earnings reports,
            SEC filings and company analysis.
          </p>

          <div className="mt-4 flex justify-center gap-2 flex-wrap">
          </div>
        </div>

        <div className="grid gap-3 md:grid-cols-2">
          {suggestions.map((prompt) => (
            <Card
              key={prompt}
             className="
            cursor-pointer
            rounded-2xl
            border
            border-zinc-800
            bg-zinc-900
            p-5
            transition-all
            duration-200
            hover:-translate-y-1
            hover:border-zinc-700
            hover:bg-zinc-800/70
            " 
            >
              <p className="text-sm">{prompt}</p>
            </Card>
          ))}
        </div>
      </div>
    </div>
  );
}