<template>
  <StickyNote>
    <template v-slot:content>
      <v-form ref="form" v-model="valid" :lazy-validation="true">
        <v-textarea name="content" :counter="maxContentLength" :rules="contentRules" auto-grow rows="1" v-model="form.content" />
      </v-form>
    </template>
    <template v-slot:menu>
      <v-btn :disabled="!valid" icon color="brown darken-4" @click="createActivity">
        <v-icon>mdi-pencil-plus</v-icon>
      </v-btn>
    </template>
  </StickyNote>
</template>

<script lang="ts">
import { Component, Vue, Emit, Prop } from 'vue-property-decorator';
import ActivityForm from '@/models/forms/activity-form';
import { MAX_CONTENT_LENGTH } from '@/constants/activities';
import StickyNote from '@/components/parts/molecules/StickyNote.vue';
import VForm from '@/lib/v-form';
import ActivitiesRepository from '@/repositories/activities-repository';
import Activity from '@/models/activity';

@Component({
  components: {
    StickyNote: StickyNote
  }
})
export default class NewActivityStickyNote extends Vue {
  @Prop()
  sessionToken!: string;

  form = new ActivityForm();
  valid = false;

  created() {
    this.initializeForm();
  }

  @Emit('createActivity')
  createActivity() {
    if (this.valid) {
      ActivitiesRepository.create(this.form.createParams(), this.sessionToken).then((activity: Activity) => {
        this.refresh();
        return activity;
      });
    }
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
    this.form = new ActivityForm({ sessionToken: this.sessionToken });
  }

  private get formRef(): VForm {
    // eslint-disable-next-line
    return (this.$refs as any).form;
  }
}
</script>

<style scoped lang="scss">
.sticky-note {
  margin-right: auto;
  margin-left: auto;
}
</style>
