export interface NewSessionRequest {
  title: string;
}

export interface SessionResponse {
  token: string;
  title: string;
  created_at: Date | string;
  updated_at: Date | string;
}
