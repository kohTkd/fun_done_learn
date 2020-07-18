<template>
  <v-container class="fill-height" fluid>
    <v-row align="center" justify="center">
      <v-col cols="6" sm="8" md="4">
        <NewSession @createSession="createSession" />
      </v-col>
      <v-col cols="6" sm="8" md="4">
        <JoinSession @joinSession="joinSession" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import NewSession from '@/components/parts/organisms/index/NewSession.vue';
import JoinSession from '@/components/parts/organisms/index/JoinSession.vue';
import Session from '@/models/session';
import SessionForm from '@/models/forms/session-form';
import SessionsRepository from '@/repositories/sessions-repository';

@Component({
  components: {
    NewSession,
    JoinSession
  }
})
export default class IndexComponent extends Vue {
  createSession(form: SessionForm) {
    SessionsRepository.create(form.createParams()).then((session: Session) => this.routeTo(session));
  }

  joinSession(form: SessionForm) {
    SessionsRepository.find(form.token).then((session: Session) => this.routeTo(session));
  }

  private routeTo(session: Session) {
    this.$router.push({ name: 'session', params: { token: session.token } });
  }
}
</script>
