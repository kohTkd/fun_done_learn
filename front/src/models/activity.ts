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

  update({ content, placement }: { content: string; placement?: Placement }) {
    this.content = content;
    if (placement) {
      this.placement.moveTo({ top: placement.top, left: this.placement.left });
    }
  }

  isSamePosition(placement: Placement): boolean {
    return this.placement.isSamePosition(placement);
  }

  get left() {
    return this.placement.left;
  }

  get top() {
    return this.placement.top;
  }

  get isPresent(): boolean {
    return this.sessionToken.length > 0 && this.token.length > 0 && this.content.length > 0;
  }

  static get dummy(): Activity {
    return new Activity({ session_token: '', token: '', content: '' });
  }
}
