<template>
  <v-container flued>
    <v-navigation-drawer app right clipped width="280">
      <SideMenu v-bind:session="session" v-bind:notes="notes" @createActivity="createActivity" @createNote="createNote" />
    </v-navigation-drawer>
    <div class="session-board">
      <Board v-bind:activities="activities" @replaced="replaced" @update="updateActivity" />
    </div>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Board from '@/components/parts/organisms/session-board/boards/Board.vue';
import SideMenu from '@/components/parts/organisms/session-board/SideMenu.vue';

import { POLLING_DURATION } from '@/constants/sessions';
import Session from '@/models/session';
import Activity from '@/models/activity';
import Note from '@/models/note';
import SessionsRepository from '@/repositories/sessions-repository';
import ActivitiesRepository from '@/repositories/activities-repository';
import NotesRepository from '@/repositories/notes-repository';

@Component({
  components: {
    Board: Board,
    SideMenu: SideMenu
  }
})
export default class SessionBoard extends Vue {
  session = Session.dummy;
  activities = new Array<Activity>();
  notes = new Array<Note>();
  intervalId?: number;

  created() {
    const token = this.$route.params.token;
    this.fetchSession(token).then((session: Session) => this.fetchContents(session.token));
  }

  mounted() {
    this.setInterval();
  }

  beforeDestroy() {
    this.clearInterval();
  }

  createActivity(activity: Activity) {
    if (activity) this.activities.push(activity);
    this.resetInterval();
  }

  updateActivity(activity: Activity) {
    this.activities.find(act => act.token === activity.token)?.update({ content: activity.content });
  }

  createNote(note: Note) {
    if (note) this.notes.push(note);
    this.resetInterval();
  }

  replaced(_activity?: Activity) {
    this.resetInterval();
  }

  setInterval() {
    this.intervalId = setInterval(() => this.fetchContents(this.session.token), POLLING_DURATION);
  }

  clearInterval() {
    clearInterval(this.intervalId);
  }

  resetInterval() {
    this.clearInterval();
    this.setInterval();
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
}
</script>

<style scoped lang="scss">
@import '@/sass/_variables';
.session-board {
  width: $board-width;
  margin: 2rem auto;
}
</style>
