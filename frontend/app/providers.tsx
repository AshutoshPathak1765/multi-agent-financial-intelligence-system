"use client";

import { ClerkProvider } from "@clerk/nextjs";
import { dark } from '@clerk/ui/themes' 
import {
  QueryClient,
  QueryClientProvider,
} from "@tanstack/react-query";
import { ReactNode, useState } from "react";

interface ProvidersProps {
  children: ReactNode;
}

export default function Providers({
  children,
}: ProvidersProps) {
  const [queryClient] = useState(
    () => new QueryClient()
  );

  return (
    <QueryClientProvider client={queryClient}>
      <ClerkProvider
        appearance={{
          theme: dark,
        }}
      >
        {children}
      </ClerkProvider>
    </QueryClientProvider>
  );
}