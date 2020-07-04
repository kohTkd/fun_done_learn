<template>
  <v-card class="elevation-12">
    <v-toolbar color="accent" dark flat>
      <v-toolbar-title>Join Session</v-toolbar-title>
    </v-toolbar>
    <v-card-text>
      <v-form>
        <v-text-field label="セッショントークン" prepend-icon="mdi-key-variant" type="text" v-model="form.token" />
      </v-form>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <OkButton label="Join" @click="joinSession" />
    </v-card-actions>
  </v-card>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import JoinSessionForm from '@/models/forms/sessions/join-session-form';

@Component
export default class JoinSession extends Vue {
  form = new JoinSessionForm();
  errors = new Array<string>();

  joinSession() {
    this.$emit('joinSession', this.form);
  }
}
</script>
