<template>
  <v-card outlined width="100%">
    <v-form ref="form" v-model="valid" :lazy-validation="true">
      <v-textarea outlined name="content" :counter="maxContentLength" :rules="contentRules" rows="2" v-model="form.content" />
    </v-form>
    <v-card-actions>
      <v-spacer />
      <OkButton v-bind:disabled="isInvalid" @click="createNote" :large="false" :min-width="100">コメント</OkButton>
    </v-card-actions>
  </v-card>
</template>

<script lang="ts">
import { Component, Vue, Emit, Prop } from 'vue-property-decorator';
import NoteForm from '@/models/forms/note-form';
import { MAX_CONTENT_LENGTH } from '@/constants/notes';
import VForm from '@/lib/v-form';

@Component
export default class NewNote extends Vue {
  @Prop()
  sessionToken!: string;

  form = new NoteForm();
  valid = false;

  created() {
    this.initializeForm();
  }

  @Emit('createNote')
  createNote() {
    if (this.valid) return this.form;
  }

  refresh() {
    this.initializeForm();
    this.formRef.resetValidation();
  }

  get contentRules(): Array<Function> {
    return this.form.getRules('content');
  }

  get maxContentLength(): number {
    return MAX_CONTENT_LENGTH;
  }

  get isInvalid(): boolean {
    return !this.valid;
  }

  private initializeForm() {
    this.form = new NoteForm({ sessionToken: this.sessionToken });
  }

  private get formRef(): VForm {
    // eslint-disable-next-line
    return (this.$refs as any).form;
  }
}
</script>

<style scoped lang="scss">
form {
  width: 100%;
}
</style>
