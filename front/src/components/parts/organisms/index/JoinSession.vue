<template>
  <v-card class="elevation-12">
    <v-toolbar color="accent" dark flat>
      <v-toolbar-title>セッションに参加</v-toolbar-title>
    </v-toolbar>
    <v-card-text>
      <v-form ref="form" v-model="valid" :lazy-validation="true">
        <v-text-field
          label="セッショントークン"
          name="token"
          :rules="tokenRules"
          prepend-icon="mdi-key-variant"
          type="text"
          v-model="form.token"
        />
      </v-form>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <OkButton v-bind:disabled="isInvalid" @click="joinSession">参加</OkButton>
    </v-card-actions>
  </v-card>
</template>

<script lang="ts">
import { Component, Vue, Emit } from 'vue-property-decorator';
import SessionForm from '@/models/forms/session-form';

@Component
export default class JoinSession extends Vue {
  form!: SessionForm;
  valid = false;

  created() {
    this.form = new SessionForm();
  }

  @Emit('joinSession')
  joinSession() {
    if (this.valid) return this.form;
  }

  get tokenRules(): Array<Function> {
    return this.form.getRules('token');
  }

  get isInvalid(): boolean {
    return !this.valid;
  }
}
</script>
