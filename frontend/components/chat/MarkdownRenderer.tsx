import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import rehypeHighlight from "rehype-highlight";
import "highlight.js/styles/github-dark.css";

interface MarkdownRendererProps {
  content: string;
}

export function MarkdownRenderer({
  content,
}: MarkdownRendererProps) {
  return (
    <ReactMarkdown
      remarkPlugins={[remarkGfm]}
      rehypePlugins={[rehypeHighlight]}
      components={{
        pre: ({ children }) => (
          <pre
            className="
              my-6
              overflow-x-auto
              rounded-xl
              border
              border-zinc-700
              bg-zinc-950
              p-4
            "
          >
            {children}
          </pre>
        ),
        code: ({ className, children }) => {
        const isCodeBlock = className?.startsWith("language-");

        if (isCodeBlock) {
          return (
            <code className={className}>
              {children}
            </code>
          );
        }

        return (
          <code
            className="
              rounded
              bg-zinc-800
              px-1.5
              py-0.5
              font-mono
              text-sm
              text-emerald-300
            "
          >
            {children}
          </code>
        );
      },
        h1: ({ children }) => (
          <h1 className="mb-6 text-4xl font-bold tracking-tight">
            {children}
          </h1>
        ),

        h2: ({ children }) => (
          <h2 className="mt-8 mb-4 text-3xl font-semibold tracking-tight">
            {children}
          </h2>
        ),

        h3: ({ children }) => (
          <h3 className="mt-6 mb-3 text-2xl font-semibold">
            {children}
          </h3>
        ),

        p: ({ children }) => (
          <p className="mb-4 leading-8 text-zinc-200">
            {children}
          </p>
        ),

        ul: ({ children }) => (
          <ul className="mb-4 ml-6 list-disc space-y-2">
            {children}
          </ul>
        ),

        ol: ({ children }) => (
          <ol className="mb-4 ml-6 list-decimal space-y-2">
            {children}
          </ol>
        ),

        li: ({ children }) => (
          <li className="leading-7">
            {children}
          </li>
        ),

        blockquote: ({ children }) => (
          <blockquote
            className="
              my-6
              border-l-4
              border-emerald-500
              pl-4
              italic
              text-zinc-400
            "
          >
            {children}
          </blockquote>
        ),

        hr: () => (
          <hr className="my-8 border-zinc-700" />
        ),
        table: ({ children }) => (
        <div className="my-6 overflow-x-auto rounded-lg border border-zinc-700">
          <table className="w-full text-sm">
            {children}
          </table>
        </div>
      ),

      thead: ({ children }) => (
        <thead className="bg-zinc-800">
          {children}
        </thead>
),

tbody: ({ children }) => (
  <tbody className="divide-y divide-zinc-800">
    {children}
  </tbody>
),

tr: ({ children }) => (
  <tr className="even:bg-zinc-900/40 hover:bg-zinc-900/70 transition-colors">
    {children}
  </tr>
),

th: ({ children }) => (
  <th className="border-b border-zinc-700 px-4 py-3 text-left align-top font-semibold">
    {children}
  </th>
),

td: ({ children }) => (
  <td className="px-4 py-3 align-top">
    {children}
  </td>
),
      }}
    >
      {content}
    </ReactMarkdown>
  );
}