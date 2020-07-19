import { ActivityApiInterface } from '@/models/interfaces/api/activities';

export default class Activity {
  sessionToken: string;
  token: string;
  content: string;
  createdAt?: string | Date;
  updatedAt?: string | Date;

  constructor({ session_token, token, content, created_at, updated_at }: ActivityApiInterface) {
    this.sessionToken = session_token;
    this.token = token;
    this.content = content;
    this.createdAt = created_at;
    this.updatedAt = updated_at;
  }

  static get dummy(): Activity {
    return new Activity({ session_token: '', token: '', content: '', created_at: '' });
  }
}