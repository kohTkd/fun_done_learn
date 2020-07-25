import moment from 'moment';
import { SessionResponse } from './interfaces/api/sessions';

export default class Session {
  token: string;
  title: string;
  createdAt: moment.Moment;
  updatedAt: moment.Moment;

  constructor({ token, title, created_at, updated_at }: SessionResponse) {
    this.token = token;
    this.title = title;
    this.createdAt = moment(created_at);
    this.updatedAt = moment(updated_at);
  }

  static get dummy(): Session {
    return new Session({ token: '', title: '', created_at: '', updated_at: '' });
  }
}
