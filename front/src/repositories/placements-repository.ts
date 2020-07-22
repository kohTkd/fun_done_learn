import axios from '@/repositories/axios';
import Placement from '@/models/placement';
import { UpdatePlacementParams } from '@/models/interfaces/api/placements';

export default class PlacementsRepository {
  static async update(params: UpdatePlacementParams, sessionToken: string, activityToken: string): Promise<Placement> {
    return axios.put(this.pathTo(sessionToken, activityToken), params).then(response => new Placement(response.data));
  }
  private static pathTo(sessionToken: string, activityToken: string): string {
    return `/sessions/${sessionToken}/activities/${activityToken}/placement`;
  }
}
