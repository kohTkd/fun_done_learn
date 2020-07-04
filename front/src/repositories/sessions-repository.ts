import axios from '@/repositories/axios';
import { NewSessionParams } from '@/models/interfaces/sessions/new-session';

export default class SessionsRepository {
  static async create(params: NewSessionParams) {
    return axios.post('/sessions', params);
  }
}
