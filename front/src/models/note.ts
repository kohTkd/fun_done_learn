import { NoteApiInterface } from '@/models/interfaces/api/notes';

export default class Note {
  sessionToken: string;
  token: string;
  content: string;
  createdAt?: string | Date;
  updatedAt?: string | Date;

  constructor({ session_token, token, content, created_at, updated_at }: NoteApiInterface) {
    this.sessionToken = session_token;
    this.token = token;
    this.content = content;
    this.createdAt = created_at;
    this.updatedAt = updated_at;
  }
}
