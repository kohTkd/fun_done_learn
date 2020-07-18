export interface NewStickyNoteParams {
  session_token: string;
  content: string;
}

export interface UpdateStickyNoteParams extends NewStickyNoteParams {
  token: string;
}
