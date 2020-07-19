<template>
  <v-container class="px-3 py-6">
    <StickyNote>
      <template v-slot:content>{{ activity.content }}</template>
      <template v-slot:menu />
    </StickyNote>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue, Prop } from 'vue-property-decorator';
import Activity from '@/models/activity';
import StickyNote from '@/components/parts/molecules/StickyNote.vue';

@Component({
  components: {
    StickyNote: StickyNote
  }
})
export default class ActivityViewer extends Vue {
  @Prop()
  activity!: Activity;
}
</script>

<style scoped lang="scss"></style>
