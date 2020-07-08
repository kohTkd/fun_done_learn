export default class Session {
  token?: string;
  title?: string;
  created_at?: string | Date;

  constructor(
    { token = '', title = '', created_at = ''}:
    { token?: string, title?: string, created_at?: string }
  ) {
    this.token = token;
    this.title = title;
    this.created_at = created_at;
  }
}
