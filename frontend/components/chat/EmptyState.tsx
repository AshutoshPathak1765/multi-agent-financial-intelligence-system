import { Card } from "@/components/ui/card";
import { Bot } from "lucide-react";

import {
  ArrowRight,
  Building2,
  FileText,
  TrendingUp,
} from "lucide-react";

const suggestions = [
  {
    icon: Building2,
    text: "Compare Apple's revenue growth with Microsoft",
  },
  {
    icon: FileText,
    text: "Summarize NVIDIA's latest quarterly earnings",
  },
  {
    icon: TrendingUp,
    text: "Analyze Tesla's cash flow trends",
  },
  {
    icon: ArrowRight,
    text: "Identify financial risks in Amazon's annual report",
  },
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

          <p className="mx-auto mt-4 max-w-2xl text-muted-foreground leading-7">
            Analyze annual reports, compare companies, understand
            financial statements, and answer financial questions
            using AI-powered multi-agent workflows.
          </p>

          <div className="mt-4 flex justify-center gap-2 flex-wrap">
          </div>
        </div>

        <div className="grid gap-3 md:grid-cols-2">
          {suggestions.map((item) => {
          const Icon = item.icon;

            return (
              <Card
                key={item.text}
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
                  hover:border-emerald-500/60
                  hover:bg-zinc-800
                "
              >
                <div className="flex items-start gap-3">
                  <Icon className="mt-0.5 h-5 w-5 shrink-0 text-emerald-400" />

                  <p className="text-sm leading-6">
                    {item.text}
                  </p>
                </div>
              </Card>
            );
          })}
        </div>
      <p className="pt-6 text-center text-sm text-muted-foreground">
      Create a new chat from the sidebar to begin your analysis.
      </p>
      </div>
    </div>
  );
}