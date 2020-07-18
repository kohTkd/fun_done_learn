import attributeNameOf from '@/lib/attribute-names';

export default abstract class ApplicationForm {
  private rules = new Map<string, Array<Function>>();

  constructor() {
    this.rules = new Map<string, Array<Function>>();
    this.initRules();
  }

  getRules(key: string): Array<Function> {
    return this.rules.get(key) || [];
  }

  protected setRules(keys: Array<string>, generator: Function) {
    const messageKey = attributeNameOf(...keys);
    const key = keys.slice(-1)[0];
    this.rules.set(key, generator(messageKey));
  }

  abstract initRules(): void;
}
