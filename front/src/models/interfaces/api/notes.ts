export interface NewNoteParams {
  session_token: string;
  content: string;
}

export interface UpdateNoteParams extends NewNoteParams {
  token: string;
}

export interface NoteApiInterface {
  session_token: string;
  token: string;
  content: string;
  created_at?: string | Date;
  updated_at?: string | Date;
}
