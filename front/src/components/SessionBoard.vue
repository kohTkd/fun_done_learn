<template>
  <v-container flued>
    <v-navigation-drawer app right clipped width="350">
      <h2>{{ session.title }}</h2>
      <NewActivityStickyNote ref="newActivity" v-bind:sessionToken="session.token" @createActivity="createActivity" />
    </v-navigation-drawer>
    <div class="fun-done-learn-session">
      <div class="circles">
        <BoardCircle v-bind:fun="true" />
        <BoardCircle v-bind:done="true" />
        <BoardCircle v-bind:learn="true" />
      </div>
    </div>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import BoardCircle from '@/components/parts/organisms/session/BoardCircle.vue';
import NewActivityStickyNote from '@/components/parts/organisms/session/NewActivityStickyNote.vue';
import Session from '@/models/session';
import Activity from '@/models/activity';
import ActivityForm from '@/models/forms/activity-form';
import SessionsRepository from '@/repositories/sessions-repository';
import ActivitiesRepository from '@/repositories/activities-repository';

@Component({
  components: {
    BoardCircle: BoardCircle,
    NewActivityStickyNote: NewActivityStickyNote
  }
})
export default class SessionBoard extends Vue {
  session = Session.dummy;
  newActivityDialog = false;
  activities = new Array<Activity>();

  created() {
    const token = this.$route.params.token;
    this.fetchSession(token).then(() => this.fetchActivities(token));
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
.fun-done-learn-session {
  width: $board-width;
  margin: 2rem auto;

  .circles {
    display: grid;
    grid-template-columns: repeat(16, 1fr);
    // 円盤は横10グリッド縦2グリッドで正円になるようにする
    grid-template-rows: repeat(3, $board-width * 10 / 16 / 2);

    &::after {
      display: none;
    }

    .circle {
      &.fun {
        grid-column-start: 4;
        grid-column-end: 14;
        grid-row-start: 1;
        grid-row-end: 3;
      }

      &.done {
        grid-column-start: 1;
        grid-column-end: 11;
        grid-row-start: 2;
        grid-row-end: 4;
      }

      &.learn {
        grid-column-start: 7;
        grid-column-end: 17;
        grid-row-start: 2;
        grid-row-end: 4;
      }
    }
  }
}
</style>
