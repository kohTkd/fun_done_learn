import attributeNameOf from '@/lib/attribute-names';

export default abstract class ApplicationForm {
  rules = new Map<string, Array<Function>>();

  constructor() {
    this.rules = new Map<string, Array<Function>>();
    this.initRules();
  }

  getRules(key: string): Array<Function> {
    return this.rules.get(key) || [];
  }

  generateRules(keys: Array<string>, generator: Function) {
    const messageKey = attributeNameOf(...keys);
    return generator(messageKey);
  }

  abstract initRules(): void;
}
