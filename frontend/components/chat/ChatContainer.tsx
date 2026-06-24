import { ChatInput } from "./ChatInput";
import { ChatWindow } from "./ChatWindow";

export function ChatContainer() {
  return (
    <div className="flex h-full flex-col">
      <ChatWindow />
      <ChatInput />
    </div>
  );
}