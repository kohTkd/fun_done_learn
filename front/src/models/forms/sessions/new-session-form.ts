import Form from '../form';
import { blankValidation, maxLengthValidation } from '@/lib/validations';
import { TITLE_MAX_LENGTH } from '@/constants/session';
import { NewSession, NewSessionParams } from '@/models/interfaces/sessions/new-session';

export default class NewSessionForm extends Form implements NewSession {
  title: string;
  rules: Map<string, Array<Function>>;

  constructor(title = '') {
    super();
    this.title = title;
    this.rules = new Map<string, Array<Function>>([['title', this.generateTitleRules()]]);
  }

  initRules(): void {
    this.rules.set('title', this.generateTitleRules());
  }

  generateTitleRules(): Array<Function> {
    return this.generateRules(['session', 'title'], (attrName: string) => {
      return [blankValidation(attrName), maxLengthValidation(attrName, TITLE_MAX_LENGTH)];
    });
  }

  toParams(): NewSessionParams {
    return {
      title: this.title
    };
  }
}
