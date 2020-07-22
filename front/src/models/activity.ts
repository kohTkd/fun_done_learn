import { ActivityApiInterface } from '@/models/interfaces/api/activities';
import Placement from '@/models/placement';
import Position from '@/models/interfaces/position';

export default class Activity {
  sessionToken: string;
  token: string;
  content: string;
  createdAt?: string | Date;
  updatedAt?: string | Date;

  placement: Placement;

  constructor({ session_token, token, content, created_at, updated_at, placement }: ActivityApiInterface) {
    this.sessionToken = session_token;
    this.token = token;
    this.content = content;
    this.createdAt = created_at;
    this.updatedAt = updated_at;

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
    return new Activity({ session_token: '', token: '', content: '', created_at: '' });
  }
}
