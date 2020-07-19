export interface NewStickyNoteParams {
  session_token: string;
  content: string;
}

export interface UpdateStickyNoteParams extends NewStickyNoteParams {
  token: string;
}

export interface StickyNoteApiInterface {
  session_token: string;
  token: string;
  content: string;
  created_at?: string | Date;
  updated_at?: string | Date;
}
