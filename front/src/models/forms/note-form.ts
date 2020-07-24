import ApplicationForm from '@/models/forms/application-form';
import { blankValidation, maxLengthValidation } from '@/lib/validations';
import { MAX_CONTENT_LENGTH } from '@/constants/notes';
import { NewNoteParams } from '@/models/interfaces/api/notes';

export default class NoteForm extends ApplicationForm {
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
    this.setContentRules();
  }

  createParams(): NewNoteParams {
    return {
      session_token: this.sessionToken,
      content: this.content
    };
  }

  private setContentRules(): void {
    this.setRules(['Note', 'content'], (messageKey: string) => [
      blankValidation(messageKey),
      maxLengthValidation(messageKey, MAX_CONTENT_LENGTH)
    ]);
  }
}
