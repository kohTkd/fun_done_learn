<template>
  <v-container flued class="px-3 py-3">
    <v-row no-gutters class="py-3">
      <h2>{{ session.title }}</h2>
    </v-row>
    <v-row no-gutters class="py-3">
      <NewActivityStickyNote ref="newActivity" v-bind:sessionToken="session.token" @createActivity="createActivity" />
    </v-row>
    <v-row no-gutters class="py-3">
      <Notes v-bind:notes="currentNotes" />
    </v-row>
    <v-row no-gutters class="py-3">
      <NewNote ref="newNote" v-bind:sessionToken="session.token" @createNote="createNote" />
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue, Prop, Emit, Watch } from 'vue-property-decorator';
import NewActivityStickyNote from '@/components/parts/organisms/session-board/sticky-notes/NewActivityStickyNote.vue';
import NewNote from '@/components/parts/organisms/session-board/notes/NewNote.vue';
import Notes from '@/components/parts/organisms/session-board/notes/Notes.vue';

import Session from '@/models/session';
import Activity from '@/models/activity';
import Note from '@/models/note';

@Component({
  components: {
    NewActivityStickyNote: NewActivityStickyNote,
    NewNote: NewNote,
    Notes: Notes
  }
})
export default class SideMenu extends Vue {
  @Prop({ default: () => Session.dummy })
  session!: Session;

  @Prop({ default: () => new Array<Note>() })
  notes!: Array<Note>;

  currentNotes = new Array<Note>();

  @Watch('notes')
  onUpdateNotes(newNotes: Array<Note>, _oldNotes: Array<Note>) {
    this.currentNotes = newNotes;
  }

  @Emit('createActivity')
  createActivity(activity: Activity) {
    return activity;
  }

  @Emit('createNote')
  createNote(note: Note) {
    return note;
  }
}
</script>

<style scoped lang="scss"></style>
