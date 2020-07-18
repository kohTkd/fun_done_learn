export default class StickyNote {
  sessionToken: string;
  token: string;
  content: string;
  createdAt: string | Date;

  constructor({
    session_token,
    token,
    content,
    created_at
  }: {
    session_token: string;
    token: string;
    content: string;
    created_at: string;
  }) {
    this.sessionToken = session_token;
    this.token = token;
    this.content = content;
    this.createdAt = created_at;
  }

  static get dummy(): StickyNote {
    return new StickyNote({ session_token: '', token: '', content: '', created_at: '' });
  }
}
