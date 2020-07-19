export interface NewSessionParams {
  title: string;
}

export interface FindSessionParams {
  token: string;
}

export interface StickyNoteApiInterface {
  token: string;
  title: string;
  created_at?: string | Date;
  updated_at?: string | Date;
}
