<template>
  <v-container class="fill-height" fluid>
    <v-row align="center" justify="center">
      <v-col cols="6" sm="8" md="4">
        <NewSession @createSession="openSession" />
      </v-col>
      <v-col cols="6" sm="8" md="4">
        <JoinSession @joinSession="openSession" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import NewSession from '@/components/parts/organisms/index/NewSession.vue';
import JoinSession from '@/components/parts/organisms/index/JoinSession.vue';
import Session from '@/models/session';

@Component({
  components: {
    NewSession,
    JoinSession
  }
})
export default class Index extends Vue {
  openSession(session: Session) {
    this.routeTo(session);
  }

  private routeTo(session: Session) {
    this.$router.push({ name: 'session', params: { token: session.token } });
  }
}
</script>
