<template>
  <StickyNote>
    <template v-slot:content>
      <v-form ref="form" v-model="valid" :lazy-validation="true">
        <v-textarea name="content" :counter="maxContentLength" :rules="contentRules" auto-grow rows="1" v-model="form.content" />
      </v-form>
    </template>
    <template v-slot:menu>
      <v-btn icon small color="brown darken-4" @click="cancel">
        <v-icon>mdi-cancel</v-icon>
      </v-btn>
      <v-btn :disabled="!valid" icon small color="brown darken-4" @click="update">
        <v-icon>mdi-send</v-icon>
      </v-btn>
    </template>
  </StickyNote>
</template>

<script lang="ts">
import { Component, Vue, Prop, Emit } from 'vue-property-decorator';
import VueDragResize from 'vue-drag-resize';
import StickyNote from '@/components/parts/molecules/StickyNote.vue';

import Activity from '@/models/activity';
import ActivityForm from '@/models/forms/activity-form';
import VForm from '@/lib/v-form';
import ActivitiesRepository from '@/repositories/activities-repository';
import { MAX_CONTENT_LENGTH } from '@/constants/activities';

@Component({
  components: {
    StickyNote: StickyNote,
    VueDragResize: VueDragResize
  }
})
export default class EditActivityStickyNote extends Vue {
  @Prop()
  activity!: Activity;

  form = new ActivityForm();
  valid = false;

  created() {
    this.initializeForm();
  }

  @Emit('update')
  update() {
    if (this.valid) {
      return ActivitiesRepository.update(this.form.updateParams(), this.activity.sessionToken, this.activity.token).then(
        (activity: Activity) => {
          this.refresh();
          return activity;
        }
      );
    }
  }

  @Emit('cancel')
  cancel(event: MouseEvent | TouchEvent) {
    this.refresh();
    return event;
  }

  refresh() {
    setTimeout(() => {
      this.initializeForm();
      this.formRef?.resetValidation();
    }, 100);
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
    this.form = new ActivityForm({ token: this.activity.token, sessionToken: this.activity.sessionToken, content: this.activity.content });
  }

  private get formRef(): VForm {
    // eslint-disable-next-line
    return (this.$refs as any).form;
  }
}
</script>

<style scoped lang="scss"></style>
