export type MessageRole = "user" | "assistant";


export interface CreateMessageRequest {
  session_id: string;
  role: string;
  content: string;
}

export interface MessageResponse {
  id: string;
  session_id: string;
  role: MessageRole;
  content: string;
  created_at: string;
}