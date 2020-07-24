<template>
  <v-container flued>
    <v-navigation-drawer app right clipped width="280">
      <v-container flued class="px-3 py-6">
        <v-row no-gutters>
          <h2>{{ session.title }}</h2>
        </v-row>
        <v-row no-gutters>
          <NewActivityStickyNote ref="newActivity" v-bind:sessionToken="session.token" @createActivity="createActivity" />
        </v-row>
        <v-row no-gutters>
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
    NewNote: NewNote
  }
})
export default class SessionBoard extends Vue {
  session = Session.dummy;
  activities = new Array<Activity>();
  notes = new Array<Note>();

  created() {
    const token = this.$route.params.token;
    this.fetchSession(token).then(() => this.fetchContents());
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

  private async fetchSession(token: string): Promise<Session> {
    return SessionsRepository.find(token).then((session: Session) => (this.session = session));
  }

  private fetchContents() {
    console.log('fetchContents');
    return Promise.all([this.fetchActivities(), this.fetchNotes()]);
  }

  private async fetchActivities(): Promise<Array<Activity>> {
    console.log('fetchActivities');
    return ActivitiesRepository.fetch(this.session.token).then((activities: Array<Activity>) => (this.activities = activities));
  }

  private async fetchNotes(): Promise<Array<Note>> {
    console.log('fetchNotes');
    return NotesRepository.fetch(this.session.token).then((notes: Array<Note>) => (this.notes = notes));
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
