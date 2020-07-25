import moment from 'moment';

import { NoteResponse } from '@/models/interfaces/api/notes';

export default class Note {
  sessionToken: string;
  token: string;
  content: string;
  createdAt: moment.Moment;
  updatedAt: moment.Moment;

  constructor({ session_token, token, content, created_at, updated_at }: NoteResponse) {
    this.sessionToken = session_token;
    this.token = token;
    this.content = content;
    this.createdAt = moment(created_at);
    this.updatedAt = moment(updated_at);
  }

  get sortKey(): number {
    return this.createdAt.valueOf();
  }

  get timestamp(): string {
    return this.createdAt.format('YYYY-MM-DD hh:mm:ss');
  }
}
