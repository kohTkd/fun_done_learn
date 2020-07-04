import attributeNameOf from '@/lib/attribute-names';
import ApiParams from '../interfaces/api-params';

export default abstract class Form {
  rules: Map<string, Array<Function>>;

  constructor() {
    this.rules = new Map<string, Array<Function>>();
    this.initRules();
  }

  getRules(key: string): Array<Function> {
    return this.rules.get(key) || [];
  }

  generateRules(keys: Array<string>, generator: Function) {
    const attrName = attributeNameOf(...keys);
    return generator(attrName);
  }

  abstract initRules(): void;

  abstract toParams(): ApiParams;
}
