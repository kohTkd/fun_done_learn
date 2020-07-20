import Position from '@/models/interfaces/position';

export default class Placement {
  top: number;
  left: number;

  constructor({ top, left }: Position) {
    this.top = top;
    this.left = left;
  }

  static get default(): Placement {
    return new Placement({ top: 0, left: 0 });
  }

  get values() {
    return { top: this.top, left: this.left };
  }

  moveTo(position: Position) {
    this.top = position.top;
    this.left = position.left;
  }
}
