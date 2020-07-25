<template>
  <v-container flued>
    <v-navigation-drawer app right clipped width="280">
      <v-container flued class="px-3 py-3">
        <v-row class="py-3">
          <h2>{{ session.title }}</h2>
        </v-row>
        <v-row class="py-3">
          <NewActivityStickyNote ref="newActivity" v-bind:sessionToken="session.token" @createActivity="createActivity" />
        </v-row>
        <v-row class="py-3">
          <Notes v-bind:notes="sortedNotes" />
        </v-row>
        <v-row class="py-3">
          <NewNote ref="newNote" v-bind:sessionToken="session.token" @createNote="createNote" />
        </v-row>
      </v-container>
    </v-navigation-drawer>
    <div class="session-board">
      <Board v-bind:activities="activities" />
    </div>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Board from '@/components/parts/organisms/session-board/Board.vue';
import NewActivityStickyNote from '@/components/parts/organisms/session-board/NewActivityStickyNote.vue';
import NewNote from '@/components/parts/organisms/session-board/NewNote.vue';
import Notes from '@/components/parts/organisms/session-board/Notes.vue';

import Session from '@/models/session';
import Activity from '@/models/activity';
import Note from '@/models/note';
import ActivityForm from '@/models/forms/activity-form';
import NoteForm from '@/models/forms/note-form';
import SessionsRepository from '@/repositories/sessions-repository';
import ActivitiesRepository from '@/repositories/activities-repository';
import NotesRepository from '@/repositories/notes-repository';

@Component({
  components: {
    Board: Board,
    NewActivityStickyNote: NewActivityStickyNote,
    NewNote: NewNote,
    Notes: Notes
  }
})
export default class SessionBoard extends Vue {
  session = Session.dummy;
  activities = new Array<Activity>();
  notes = new Array<Note>();

  created() {
    const token = this.$route.params.token;
    this.fetchSession(token).then((session: Session) => this.fetchContents(session.token));
  }

  async createActivity(form: ActivityForm) {
    ActivitiesRepository.create(form.createParams(), this.session.token).then((activity: Activity) => {
      this.activities.push(activity);
      this.newActivity.refresh();
    });
  }

  async createNote(form: NoteForm) {
    NotesRepository.create(form.createParams(), this.session.token).then((note: Note) => {
      this.notes.push(note);
      this.newNote.refresh();
    });
  }

  get sortedNotes(): Array<Note> {
    return this.notes.sort((a: Note, b: Note) => a.sortKey - b.sortKey);
  }

  private async fetchSession(token: string): Promise<Session> {
    return SessionsRepository.find(token).then((session: Session) => (this.session = session));
  }

  private fetchContents(sessionToken: string) {
    return Promise.all([this.fetchActivities(sessionToken), this.fetchNotes(sessionToken)]);
  }

  private async fetchActivities(sessionToken: string): Promise<Array<Activity>> {
    return ActivitiesRepository.fetch(sessionToken).then((activities: Array<Activity>) => (this.activities = activities));
  }

  private async fetchNotes(sessionToken: string): Promise<Array<Note>> {
    return NotesRepository.fetch(sessionToken).then((notes: Array<Note>) => (this.notes = notes));
  }

  private get newActivity(): NewActivityStickyNote {
    // eslint-disable-next-line
    return (this.$refs as any).newActivity as NewActivityStickyNote;
  }

  private get newNote(): NewNote {
    // eslint-disable-next-line
    return (this.$refs as any).newNote as NewNote;
  }
}
</script>

<style scoped lang="scss">
@import '@/sass/_variables';
.session-board {
  width: $board-width;
  margin: 2rem auto;
}
</style>
