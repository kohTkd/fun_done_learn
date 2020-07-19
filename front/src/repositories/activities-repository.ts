import axios from '@/repositories/axios';
import Activity from '@/models/activity';
import { NewActivityParams, ActivityApiInterface } from '@/models/interfaces/api/activities';

export default class ActivitiesRepository {
  static async create(params: NewActivityParams, sessionToken: string): Promise<Activity> {
    return axios.post(`/sessions/${sessionToken}/activities`, params).then(response => new Activity(response.data));
  }

  static async fetch(sessionToken: string): Promise<Array<Activity>> {
    return axios
      .get(`/sessions/${sessionToken}/activities`)
      .then(response => response.data.map((body: ActivityApiInterface) => new Activity(body)));
  }
}
