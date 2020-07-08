<template>
  <v-container class="fill-height" fluid>
    <v-app-bar app color="info" dark>
      {{ session.title }}
    </v-app-bar>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Session from '@/models/session';
import SessionsRepository from '@/repositories/sessions-repository';

@Component
export default class Start extends Vue {
  session = new Session({});

  mounted() {
    const token = this.$route.params.token;
    this.fetchSession(token);
  }

  private async fetchSession(token: string) {
    return SessionsRepository.find(token).then(response => {
      console.log(response);
      this.session = new Session(response.data);
      return this.session;
    });
  }
}
</script>
