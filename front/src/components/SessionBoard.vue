<template>
  <v-container flued>
    <v-navigation-drawer app right clipped width="280">
      <h2>{{ session.title }}</h2>
      <NewActivityStickyNote ref="newActivity" v-bind:sessionToken="session.token" @createActivity="createActivity" />
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
import Session from '@/models/session';
import Activity from '@/models/activity';
import ActivityForm from '@/models/forms/activity-form';
import SessionsRepository from '@/repositories/sessions-repository';
import ActivitiesRepository from '@/repositories/activities-repository';

@Component({
  components: {
    Board: Board,
    NewActivityStickyNote: NewActivityStickyNote
  }
})
export default class SessionBoard extends Vue {
  session = Session.dummy;
  activities = new Array<Activity>();

  created() {
    const token = this.$route.params.token;
    this.fetchSession(token).then(() => this.fetchActivities(this.session.token));
  }

  async createActivity(form: ActivityForm) {
    ActivitiesRepository.create(form.createParams(), this.session.token).then((activity: Activity) => {
      this.activities.push(activity);
      this.newActivity.refresh();
    });
  }

  private async fetchSession(token: string) {
    this.session = await SessionsRepository.find(token);
    return this.session;
  }

  private async fetchActivities(sessionToken: string) {
    this.activities = await ActivitiesRepository.fetch(sessionToken);
    return this.activities;
  }

  private get newActivity(): NewActivityStickyNote {
    // eslint-disable-next-line
    return (this.$refs as any).newActivity as NewActivityStickyNote;
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
