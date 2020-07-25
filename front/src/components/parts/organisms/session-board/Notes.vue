<template>
  <v-card v-if="notes" outlined width="100%">
    <v-container id="display-notes" class="overflow-y-auto">
      <v-row v-scroll:#display-notes="onScroll">
        <v-list flat dense width="100%" class="notes-list">
          <v-list-item v-for="note in notes || []" v-bind:key="note.token">
            <v-list-item-content>
              <v-list-item-title class="note-content">{{ note.content }}</v-list-item-title>
              <v-list-item-subtitle>{{ note.timestamp }}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-row>
    </v-container>
  </v-card>
</template>

<script lang="ts">
import { Component, Vue, Prop } from 'vue-property-decorator';
import Note from '@/models/note';

@Component
export default class Notes extends Vue {
  @Prop({ default: new Array<Note>() })
  notes!: Array<Note>;

  created() {
    this.notes = this.notes || new Array<Note>();
  }

  onScroll() {
    // Do nothing.
  }
}
</script>

<style scoped lang="scss">
@import '@/sass/_variables';

#display-notes {
  max-height: 20rem;

  .notes-list {
    padding-top: 0;
    padding-bottom: 0;
  }

  .v-list-item {
    line-height: 1.2rem;

    &:nth-child(odd) {
      background-color: $light-grey;
    }

    .note-content {
      overflow-wrap: anywhere;
      word-break: break-all;
      overflow-x: unset !important;
      white-space: pre-wrap;
    }
  }
}
</style>
