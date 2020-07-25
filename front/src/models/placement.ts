import { PlacementResponse, UpdatePlacementRequest } from '@/models/interfaces/api/placements';
import Position from '@/models/interfaces/position';

export default class Placement {
  sessionToken: string;
  activityToken: string;
  top: number;
  left: number;

  constructor({ session_token, activity_token, top, left }: PlacementResponse) {
    this.sessionToken = session_token;
    this.activityToken = activity_token;
    this.top = top;
    this.left = left;
  }

  static default(session_token: string, activity_token: string): Placement {
    return new Placement({ session_token: session_token, activity_token: activity_token, top: 0, left: 0 });
  }

  get values() {
    return { top: this.top, left: this.left };
  }

  moveTo(position: Position) {
    this.top = position.top;
    this.left = position.left;
  }

  get currentPositionParams(): UpdatePlacementRequest {
    return {
      session_token: this.sessionToken,
      activity_token: this.activityToken,
      top: this.top,
      left: this.left
    };
  }
}
