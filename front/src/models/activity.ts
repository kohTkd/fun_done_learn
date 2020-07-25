import moment from 'moment';

import { ActivityResponse } from '@/models/interfaces/api/activities';
import Placement from '@/models/placement';
import Position from '@/models/interfaces/position';

export default class Activity {
  sessionToken: string;
  token: string;
  content: string;
  createdAt: moment.Moment;
  updatedAt: moment.Moment;

  placement: Placement;

  constructor({ session_token, token, content, created_at, updated_at, placement }: ActivityResponse) {
    this.sessionToken = session_token;
    this.token = token;
    this.content = content;
    this.createdAt = moment(created_at);
    this.updatedAt = moment(updated_at);

    if (placement) {
      this.placement = new Placement(placement);
    } else {
      this.placement = Placement.default(this.sessionToken, token);
    }
  }

  place(position: Position) {
    this.placement.moveTo(position);
  }

  get left() {
    return this.placement.left;
  }

  get top() {
    return this.placement.top;
  }

  static get dummy(): Activity {
    return new Activity({ session_token: '', token: '', content: '' });
  }
}
