export interface CreateSessionRequest {
  title: string;
}

export interface SessionResponse {
  id: string;
  user_id: string;
  title: string;
  created_at: string;
}

export interface UpdateSessionRequest {
  title: string;
}