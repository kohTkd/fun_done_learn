<template>
  <v-card class="elevation-12">
    <v-toolbar color="primary" dark flat>
      <v-toolbar-title>新規セッションの開始</v-toolbar-title>
    </v-toolbar>
    <v-card-text>
      <v-form ref="form" v-model="valid" :lazy-validation="true">
        <v-text-field
          label="タイトル"
          name="title"
          :counter="maxTitleLength"
          :rules="titleRules"
          prepend-icon="mdi-tag"
          type="text"
          v-model="form.title"
        />
      </v-form>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <OkButton v-bind:disabled="isInvalid" @click="createSession">開始</OkButton>
    </v-card-actions>
  </v-card>
</template>

<script lang="ts">
import { Component, Vue, Emit } from 'vue-property-decorator';
import SessionForm from '@/models/forms/session-form';
import { MAX_TITLE_LENGTH } from '@/constants/session';

@Component
export default class NewSession extends Vue {
  form!: SessionForm;
  valid = false;

  created() {
    this.form = new SessionForm();
  }

  @Emit('createSession')
  createSession() {
    return this.valid ? this.form : undefined;
  }

  get titleRules(): Array<Function> {
    return this.form.rules.get('title') || [];
  }

  get maxTitleLength(): number {
    return MAX_TITLE_LENGTH;
  }

  get isInvalid(): boolean {
    return !this.valid;
  }
}
</script>
