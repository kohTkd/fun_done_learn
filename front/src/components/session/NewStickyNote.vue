<template>
  <v-container class="px-3 py-6">
    <StickyNote>
      <template v-slot:content>
        <v-form ref="form" v-model="valid" :lazy-validation="true">
          <v-textarea
            name="content"
            :counter="maxContentLength"
            :rules="contentRules"
            auto-grow
            rows="1"
            v-model="form.content"
          />
        </v-form>
      </template>
      <template v-slot:menu>
        <v-btn :disabled="!valid" icon color="brown darken-4" @click="createStickyNote">
          <v-icon>mdi-pencil-plus</v-icon>
        </v-btn>
      </template>
    </StickyNote>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue, Emit, Prop } from 'vue-property-decorator';
import StickyNoteForm from '@/models/forms/sticky-note-form';
import { MAX_CONTENT_LENGTH } from '@/constants/sticky-note';
import StickyNote from '@/components/parts/molecules/StickyNote.vue';
import VForm from '@/lib/v-form';

@Component({
  components: {
    StickyNote: StickyNote
  }
})
export default class NewStickyNote extends Vue {
  @Prop()
  sessionToken!: string;

  form = new StickyNoteForm();
  valid = false;

  created() {
    this.initializeForm();
  }

  @Emit('createStickyNote')
  createStickyNote() {
    if (this.valid) return this.form;
  }

  refresh() {
    this.initializeForm();
    this.formRef.resetValidation();
  }

  get contentRules(): Array<Function> {
    return this.form.rules.get('content') || [];
  }

  get maxContentLength(): number {
    return MAX_CONTENT_LENGTH;
  }

  get isInvalid(): boolean {
    return !this.valid;
  }

  private initializeForm() {
    this.form = new StickyNoteForm({ sessionToken: this.sessionToken });
  }

  private get formRef(): VForm {
    // eslint-disable-next-line
    return (this.$refs as any).form;
  }
}
</script>

<style scoped lang="scss"></style>
