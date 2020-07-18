import ApplicationForm from '@/models/forms/application-form';
import { blankValidation, maxLengthValidation } from '@/lib/validations';
import { MAX_TITLE_LENGTH } from '@/constants/session';
import { NewSessionParams } from '@/models/interfaces/api-params/sessions';

export default class SessionForm extends ApplicationForm {
  token!: string;
  title!: string;

  constructor({ token = '', title = '' }: { token?: string; title?: string } = {}) {
    super();
    this.token = token;
    this.title = title;
  }

  initRules(): void {
    this.rules.set('title', this.titleRules());
  }

  titleRules(): Array<Function> {
    return this.generateRules(['Session', 'title'], (messageKey: string) => [
      blankValidation(messageKey),
      maxLengthValidation(messageKey, MAX_TITLE_LENGTH)
    ]);
  }

  createParams(): NewSessionParams {
    return {
      title: this.title || ''
    };
  }
}
