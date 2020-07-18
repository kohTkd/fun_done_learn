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
    this.rules.set('sessionToken', this.sessionTokenRules());
    this.rules.set('content', this.contentRules());
  }

  sessionTokenRules(): Array<Function> {
    return this.generateRules(['StickyNote', 'sessionToken'], (messageKey: string) => {
      return [blankValidation(messageKey)];
    });
  }

  contentRules(): Array<Function> {
    return this.generateRules(['StickyNote', 'content'], (messageKey: string) => {
      return [blankValidation(messageKey), maxLengthValidation(messageKey, MAX_CONTENT_LENGTH)];
    });
  }

  createParams(): NewStickyNoteParams {
    return {
      session_token: this.sessionToken,
      content: this.content
    };
  }
}
