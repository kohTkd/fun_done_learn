<template>
  <v-container flued>
    <v-navigation-drawer app right clipped width="350">
      <h2>{{ session.title }}</h2>
      <NewStickyNote ref="newStickyNote" v-bind:sessionToken="session.token" @createStickyNote="createStickyNote" />
    </v-navigation-drawer>
    <div class="fun-done-learn-session">
      <div class="circles">
        <BoardCircle v-bind:fun="true" />
        <BoardCircle v-bind:done="true" />
        <BoardCircle v-bind:learn="true" />
      </div>
    </div>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import BoardCircle from '@/components/parts/organisms/session/BoardCircle.vue';
import NewStickyNote from '@/components/parts/organisms/session/NewStickyNote.vue';
import Session from '@/models/session';
import StickyNote from '@/models/sticky-note';
import StickyNoteForm from '@/models/forms/sticky-note-form';
import SessionsRepository from '@/repositories/sessions-repository';
import StickyNotesRepository from '@/repositories/sticky-notes-repository';

@Component({
  components: {
    BoardCircle: BoardCircle,
    NewStickyNote: NewStickyNote
  }
})
export default class SessionComponent extends Vue {
  session = Session.dummy;
  newStickyNoteDialog = false;
  stickyNotes = new Array<StickyNote>();

  created() {
    const token = this.$route.params.token;
    this.fetchSession(token);
  }

  private async fetchSession(token: string) {
    this.session = await SessionsRepository.find(token);
    return this.session;
  }

  async createStickyNote(form: StickyNoteForm) {
    StickyNotesRepository.create(form.createParams(), this.session.token).then((stickyNote: StickyNote) => {
      this.stickyNotes.push(stickyNote);
      this.newStickyNote.refresh();
    });
  }

  private get newStickyNote(): NewStickyNote {
    // eslint-disable-next-line
    return (this.$refs as any).newStickyNote as NewStickyNote;
  }
}
</script>

<style scoped lang="scss">
@import '@/sass/_variables';
.fun-done-learn-session {
  width: $board-width;
  margin: 2rem auto;

  .circles {
    display: grid;
    grid-template-columns: repeat(16, 1fr);
    // 円盤は横10グリッド縦2グリッドで正円になるようにする
    grid-template-rows: repeat(3, $board-width * 10 / 16 / 2);

    &::after {
      display: none;
    }

    .circle {
      &.fun {
        grid-column-start: 4;
        grid-column-end: 14;
        grid-row-start: 1;
        grid-row-end: 3;
      }

      &.done {
        grid-column-start: 1;
        grid-column-end: 11;
        grid-row-start: 2;
        grid-row-end: 4;
      }

      &.learn {
        grid-column-start: 7;
        grid-column-end: 17;
        grid-row-start: 2;
        grid-row-end: 4;
      }
    }
  }
}
</style>
