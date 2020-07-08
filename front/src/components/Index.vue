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
import NewSession from '@/components/index/NewSession.vue';
import JoinSession from '@/components/index/JoinSession.vue';
import NewSessionForm from '@/models/forms/sessions/new-session-form';
import JoinSessionForm from '@/models/forms/sessions/join-session-form';
import SessionsRepository from '@/repositories/sessions-repository';

@Component({
  components: {
    NewSession,
    JoinSession
  }
})
export default class Index extends Vue {
  async createSession(form: NewSessionForm) {
    console.log(form);
    SessionsRepository.create(form.toParams()).then(response =>
      this.$router.push({ name: 'session', params: { token: response.data.token } })
    );
  }

  joinSession(form: JoinSessionForm): void {
    console.log(form);
  }
}
</script>
