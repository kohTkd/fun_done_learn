import axios from '@/repositories/axios';
import Session from '@/models/session';
import { NewSessionRequest } from '@/models/interfaces/api/sessions';

export default class SessionsRepository {
  static async create(params: NewSessionRequest): Promise<Session> {
    return axios.post('/sessions', params).then(response => new Session(response.data));
  }

  static async find(token: string): Promise<Session> {
    return axios.get(`/sessions/${token}`).then(response => new Session(response.data));
  }
}
