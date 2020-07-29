import axios from '@/repositories/axios';
import Activity from '@/models/activity';
import { NewActivityRequest, ActivityResponse, UpdateActivityRequest } from '@/models/interfaces/api/activities';

export default class ActivitiesRepository {
  static async create(params: NewActivityRequest, sessionToken: string): Promise<Activity> {
    return axios.post(this.pathTo(sessionToken), params).then(response => new Activity(response.data));
  }

  static async fetch(sessionToken: string): Promise<Array<Activity>> {
    return axios.get(this.pathTo(sessionToken)).then(response => response.data.map((body: ActivityResponse) => new Activity(body)));
  }

  static async update(params: UpdateActivityRequest, sessionToken: string, token: string): Promise<Activity> {
    return axios.patch(this.pathTo(sessionToken, token), params).then(response => new Activity(response.data));
  }

  static async destroy(sessionToken: string, token: string) {
    return axios.delete(this.pathTo(sessionToken, token));
  }

  private static pathTo(sessionToken: string, token?: string): string {
    const path = `/sessions/${sessionToken}/activities`;
    if (!token) return path;

    return `${path}/${token}`;
  }
}
