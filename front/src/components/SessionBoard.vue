<template>
  <v-container flued>
    <v-navigation-drawer app right clipped width="280">
      <SideMenu v-bind:session="session" v-bind:notes="notes" @createActivity="createActivity" @createNote="createNote" />
    </v-navigation-drawer>
    <div class="session-board">
      <Board v-bind:activities="activities" @replaced="replaced" @updateActivity="updateActivity" @destroyActivity="destroyActivity" />
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
    const foundActivity = this.activities.find(act => act.token === activity.token);
    if (!foundActivity) return false;
    if (foundActivity.content === activity.content && foundActivity.isSamePosition(activity.placement)) return true;

    foundActivity.update({ content: activity.content, placement: activity.placement });
    return true;
  }

  updateNote(note: Note) {
    const foundNote = this.notes.find(act => act.token === note.token);
    if (!foundNote) return false;
    if (foundNote.content === note.content) return true;
  }

  destroyActivity(activity: Activity) {
    const index = this.activities.findIndex(act => act.token === activity.token);
    if (index >= 0) {
      this.activities.splice(index, 1);
    }
    this.resetInterval();
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

  private async fetchSession(token: string): Promise<Session> {
    return SessionsRepository.find(token).then((session: Session) => (this.session = session));
  }

  private fetchContents(sessionToken: string) {
    return Promise.all([this.fetchActivities(sessionToken), this.fetchNotes(sessionToken)]);
  }

  private async fetchActivities(sessionToken: string): Promise<Array<Activity>> {
    return ActivitiesRepository.fetch(sessionToken).then((activities: Array<Activity>) => {
      this.updateContents(this.activities, activities, this.updateActivity);
      return this.activities;
    });
  }

  private async fetchNotes(sessionToken: string): Promise<Array<Note>> {
    return NotesRepository.fetch(sessionToken).then((notes: Array<Note>) => {
      this.updateContents(this.notes, notes, this.updateNote);
      return this.notes;
    });
  }

  private updateContents(originals: Array<Activity | Note>, others: Array<Activity | Note>, updateStrategy: Function) {
    others.forEach((other: Activity | Note) => {
      if (!updateStrategy(other)) {
        originals.push(other);
        console.log(other);
      }
    });

    let length = originals.length;
    for (let i = 0; i < length; i++) {
      if (!others.some(other => other.token === originals[i].token)) {
        originals.splice(i--, 1);
        length--;
      }
    }
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
