import { StickyNoteApiInterface } from '@/models/interfaces/api/sticky-notes';

export default class StickyNote {
  sessionToken: string;
  token: string;
  content: string;
  createdAt?: string | Date;
  updatedAt?: string | Date;

  constructor({ session_token, token, content, created_at, updated_at }: StickyNoteApiInterface) {
    this.sessionToken = session_token;
    this.token = token;
    this.content = content;
    this.createdAt = created_at;
    this.updatedAt = updated_at;
  }

  static get dummy(): StickyNote {
    return new StickyNote({ session_token: '', token: '', content: '', created_at: '' });
  }
}
