<template>
  <div class="board">
    <div class="circles">
      <BoardCircle v-bind:fun="true" />
      <BoardCircle v-bind:done="true" />
      <BoardCircle v-bind:learn="true" />
    </div>
    <ActivityStickyNote v-for="activity in activities" v-bind:activity="activity" v-bind:key="activity.token" @replaced="replaced" />
  </div>
</template>

<script lang="ts">
import { Component, Vue, Prop, Emit } from 'vue-property-decorator';
import BoardCircle from '@/components/parts/organisms/session-board/boards/BoardCircle.vue';
import ActivityStickyNote from '@/components/parts/organisms/session-board/sticky-notes/ActivityStickyNote.vue';
import Activity from '@/models/activity';

@Component({
  components: {
    BoardCircle: BoardCircle,
    ActivityStickyNote: ActivityStickyNote
  }
})
export default class Board extends Vue {
  @Prop({ default: [] })
  activities!: Array<Activity>;

  @Emit('update')
  update(activity: Activity) {
    return activity;
  }

  @Emit('replaced')
  replaced(activity?: Activity) {
    return activity;
  }
}
</script>

<style scoped lang="scss">
@import '@/sass/_variables';
.board {
  position: relative;

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
