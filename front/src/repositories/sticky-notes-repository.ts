import axios from '@/repositories/axios';
import StickyNote from '@/models/sticky-note';
import { NewStickyNoteParams } from '@/models/interfaces/api-params/sticky-notes';

export default class StickyNotesRepository {
  static async create(params: NewStickyNoteParams, sessionToken: string): Promise<StickyNote> {
    return axios.post(`/sessions/${sessionToken}/sticky_notes`, params).then(response => new StickyNote(response.data));
  }
}
