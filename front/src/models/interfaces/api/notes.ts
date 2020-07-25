export interface NewNoteRequest {
  session_token: string;
  content: string;
}

export interface UpdateNoteRequest extends NewNoteRequest {
  token: string;
}

export interface NoteResponse {
  session_token: string;
  token: string;
  content: string;
  created_at: Date | string;
  updated_at: Date | string;
}
