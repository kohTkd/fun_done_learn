<template>
  <StickyNote v-if="activity.isPresent">
    <template v-slot:content>
      <div class="viewer">{{ activity.content }}</div>
    </template>
    <template v-slot:menu>
      <v-btn icon small color="brown darken-4" @click="edit">
        <v-icon>mdi-pencil</v-icon>
      </v-btn>
      <v-btn icon small olor="brown darken-4" @click="destroy">
        <v-icon>mdi-delete</v-icon>
      </v-btn>
    </template>
  </StickyNote>
</template>

<script lang="ts">
import { Component, Vue, Prop, Emit, Watch } from 'vue-property-decorator';
import Activity from '@/models/activity';
import StickyNote from '@/components/parts/molecules/StickyNote.vue';

@Component({
  components: {
    StickyNote: StickyNote
  }
})
export default class ViewActivityStickyNote extends Vue {
  @Prop({ default: () => Activity.dummy })
  activity!: Activity;

  currentActivity = Activity.dummy;

  @Watch('activity')
  onUpdateActivity(newActivity: Activity, _oldActivity: Activity) {
    this.currentActivity.update({ content: newActivity.content });
  }

  @Emit('edit')
  edit(event: MouseEvent | TouchEvent) {
    return event;
  }

  destroy() {}
}
</script>

<style scoped lang="scss"></style>
