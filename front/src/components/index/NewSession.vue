<template>
  <v-card class="elevation-12">
    <v-toolbar color="primary" dark flat>
      <v-toolbar-title>Create new session</v-toolbar-title>
    </v-toolbar>
    <v-card-text>
      <v-form ref="form" v-model="valid" :lazy-validation="true">
        <v-text-field
          label="タイトル"
          name="title"
          :counter="titleMaxLength"
          :rules="titleRules"
          prepend-icon="mdi-tag"
          type="text"
          v-model="form.title"
        />
      </v-form>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <OkButton label="開始" v-bind:disabled="isInvalid" @click="createSession" />
    </v-card-actions>
  </v-card>
</template>

<script lang="ts">
import { Component, Vue, Emit } from 'vue-property-decorator';
import NewSessionForm from '@/models/forms/sessions/new-session-form';
import { TITLE_MAX_LENGTH } from '@/constants/session';

@Component
export default class NewSession extends Vue {
  form = new NewSessionForm();
  valid = false;

  @Emit('createSession')
  createSession() {
    return this.valid ? this.form : undefined;
  }

  get titleRules(): Array<Function> {
    return this.form.rules.get('title') || [];
  }

  get titleMaxLength(): number {
    return TITLE_MAX_LENGTH;
  }

  get isInvalid(): boolean {
    return !this.valid;
  }
}
</script>
