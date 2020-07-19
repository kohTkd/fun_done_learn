import axios from '@/repositories/axios';
import StickyNote from '@/models/sticky-note';
import { NewStickyNoteParams, StickyNoteApiInterface } from '@/models/interfaces/api/sticky-notes';

export default class StickyNotesRepository {
  static async create(params: NewStickyNoteParams, sessionToken: string): Promise<StickyNote> {
    return axios.post(`/sessions/${sessionToken}/sticky_notes`, params).then(response => new StickyNote(response.data));
  }

  static async fetch(sessionToken: string): Promise<Array<StickyNote>> {
    return axios
      .get(`/sessions/${sessionToken}/sticky_notes`)
      .then(response => response.data.map((body: StickyNoteApiInterface) => new StickyNote(body)));
  }
}
