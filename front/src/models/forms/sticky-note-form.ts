import ApplicationForm from '@/models/forms/application-form';
import { blankValidation, maxLengthValidation } from '@/lib/validations';
import { MAX_CONTENT_LENGTH } from '@/constants/sticky-note';
import { NewStickyNoteParams } from '@/models/interfaces/api-params/sticky-notes';

export default class StickyNoteForm extends ApplicationForm {
  sessionToken!: string;
  content!: string;
  token!: string;

  constructor({
    sessionToken = '',
    content = '',
    token = ''
  }: { sessionToken?: string; content?: string; token?: string } = {}) {
    super();
    this.sessionToken = sessionToken;
    this.content = content;
    this.token = token;
  }

  initRules(): void {
    this.setSessionTokenRules();
    this.setContentRules();
  }

  createParams(): NewStickyNoteParams {
    return {
      session_token: this.sessionToken,
      content: this.content
    };
  }

  private setSessionTokenRules(): void {
    this.setRules(['StickyNote', 'sessionToken'], (messageKey: string) => [blankValidation(messageKey)]);
  }

  private setContentRules(): void {
    this.setRules(['StickyNote', 'content'], (messageKey: string) => [
      blankValidation(messageKey),
      maxLengthValidation(messageKey, MAX_CONTENT_LENGTH)
    ]);
  }
}
