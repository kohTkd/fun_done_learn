import axios from '@/repositories/axios';
import Note from '@/models/note';
import { NewNoteRequest, NoteResponse } from '@/models/interfaces/api/notes';

export default class NotesRepository {
  static async create(params: NewNoteRequest, sessionToken: string): Promise<Note> {
    return axios.post(this.pathTo(sessionToken), params).then(response => new Note(response.data));
  }

  static async fetch(sessionToken: string): Promise<Array<Note>> {
    return axios.get(this.pathTo(sessionToken)).then(response => response.data.map((body: NoteResponse) => new Note(body)));
  }

  private static pathTo(sessionToken: string): string {
    return `/sessions/${sessionToken}/notes`;
  }
}
