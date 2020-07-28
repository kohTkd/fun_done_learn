<template>
  <v-textarea
    name="content"
    :counter="maxContentLength"
    :rules="contentRules"
    auto-grow
    rows="1"
    v-model="content"
    @input="updateContent"
  />
</template>

<script lang="ts">
import { Component, Vue, Emit, Prop } from 'vue-property-decorator';
import { MAX_CONTENT_LENGTH } from '@/constants/activities';
import ActivityForm from '@/models/forms/activity-form';

@Component
export default class ActivityContentForm extends Vue {
  form = new ActivityForm();

  @Prop({ default: '' })
  value!: string;

  content = '';

  mounted() {
    this.content = this.value;
  }

  @Emit('updateContent')
  updateContent() {
    return this.content;
  }

  get contentRules(): Array<Function> {
    return this.form.getRules('content');
  }

  get maxContentLength(): number {
    return MAX_CONTENT_LENGTH;
  }
}
</script>

<style scoped lang="scss">
.sticky-note {
  margin-right: auto;
  margin-left: auto;
}
</style>
