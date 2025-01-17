import ApplicationForm from '@/models/forms/application-form';
import { blankValidation, maxLengthValidation } from '@/lib/validations';
import { MAX_TITLE_LENGTH } from '@/constants/sessions';
import { NewSessionRequest } from '@/models/interfaces/api/sessions';

export default class SessionForm extends ApplicationForm {
  token!: string;
  title!: string;

  constructor({ token = '', title = '' }: { token?: string; title?: string } = {}) {
    super();
    this.token = token;
    this.title = title;
  }

  initRules(): void {
    this.setTitleRules();
    this.setTokenRules();
  }

  createParams(): NewSessionRequest {
    return {
      title: this.title || ''
    };
  }

  private setTitleRules(): void {
    this.setRules(['Session', 'title'], (messageKey: string) => [
      blankValidation(messageKey),
      maxLengthValidation(messageKey, MAX_TITLE_LENGTH)
    ]);
  }

  private setTokenRules(): void {
    this.setRules(['Session', 'token'], (messageKey: string) => [blankValidation(messageKey)]);
  }
}
