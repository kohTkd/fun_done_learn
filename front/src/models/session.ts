export default class Session {
  token: string;
  title: string;
  createdAt: string | Date;

  constructor({ token, title, created_at }: { token: string; title: string; created_at: string }) {
    this.token = token;
    this.title = title;
    this.createdAt = created_at;
  }

  static get dummy(): Session {
    return new Session({ token: '', title: '', created_at: '' });
  }
}
