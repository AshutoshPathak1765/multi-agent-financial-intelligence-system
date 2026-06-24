"use client";

import { ChevronDown } from "lucide-react";

import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from "@/components/ui/collapsible";

import { Separator } from "@/components/ui/separator";

export function ExecutionDetails() {
  return (
    <Collapsible className="mt-3">
      <CollapsibleTrigger className="flex items-center gap-2 text-sm text-muted-foreground hover:text-white transition-colors">
        <ChevronDown className="h-4 w-4" />
        Execution Details
      </CollapsibleTrigger>

      <CollapsibleContent>
        <div className="mt-4 rounded-lg border border-zinc-800 bg-zinc-900 p-4">
          <div className="space-y-4">
            <div>
              <p className="font-medium">🧠 Planner</p>
              <p className="text-sm text-muted-foreground">
                Generated execution plan
              </p>
            </div>

            <Separator />

            <div>
              <p className="font-medium">📄 Retriever</p>
              <p className="text-sm text-muted-foreground">
                Retrieved 4 relevant financial documents
              </p>
            </div>

            <Separator />

            <div>
              <p className="font-medium">🌐 Search</p>
              <p className="text-sm text-muted-foreground">
                Retrieved latest earnings news
              </p>
            </div>

            <Separator />

            <div>
              <p className="font-medium">🧐 Critic</p>
              <p className="text-sm text-muted-foreground">
                Approved final response
              </p>
            </div>
          </div>
        </div>
      </CollapsibleContent>
    </Collapsible>
  );
}