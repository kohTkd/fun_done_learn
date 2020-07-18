import axios from '@/repositories/axios';
import Session from '@/models/session';
import { NewSessionParams } from '@/models/interfaces/api-params/sessions';

export default class SessionsRepository {
  static async create(params: NewSessionParams): Promise<Session> {
    return axios.post('/sessions', params).then(response => new Session(response.data));
  }

  static async find(token: string): Promise<Session> {
    return axios.get(`/sessions/${token}`).then(response => new Session(response.data));
  }
}
