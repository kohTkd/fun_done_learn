import axios from '@/repositories/axios';
import Activity from '@/models/activity';
import { NewActivityRequest, ActivityResponse } from '@/models/interfaces/api/activities';

export default class ActivitiesRepository {
  static async create(params: NewActivityRequest, sessionToken: string): Promise<Activity> {
    return axios.post(this.pathTo(sessionToken), params).then(response => new Activity(response.data));
  }

  static async fetch(sessionToken: string): Promise<Array<Activity>> {
    return axios.get(this.pathTo(sessionToken)).then(response => response.data.map((body: ActivityResponse) => new Activity(body)));
  }

  private static pathTo(sessionToken: string): string {
    return `/sessions/${sessionToken}/activities`;
  }
}
