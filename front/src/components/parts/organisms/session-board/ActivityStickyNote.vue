<template>
  <VueDragResize :isResizable="false" :parentLimitation="true" :x="x" :y="y" :w="w" :h="h" @dragstop="moved">
    <StickyNote>
      <template v-slot:content>
        <div class="viewer">{{ activity.content }}</div>
      </template>
      <template v-slot:menu />
    </StickyNote>
  </VueDragResize>
</template>

<script lang="ts">
import { Component, Vue, Prop } from 'vue-property-decorator';
import VueDragResize from 'vue-drag-resize';
import Activity from '@/models/activity';
import StickyNote from '@/components/parts/molecules/StickyNote.vue';
import Position from '@/models/interfaces/position';

@Component({
  components: {
    StickyNote: StickyNote,
    VueDragResize: VueDragResize
  }
})
export default class ActivityViewer extends Vue {
  @Prop()
  activity!: Activity;

  moved(position: Position) {
    this.activity.place(position);
  }

  get x(): number {
    return this.activity.left;
  }

  get y(): number {
    return this.activity.top;
  }

  /**
   * draggableな要素の幅のgetter.
   * resicableではないので実際の幅ではないが、draggableなエリアとして認識されてしまうので、付箋要素内部に収まるサイズを指定
   */
  get w(): number {
    return 10;
  }

  /**
   * draggableな要素の高さのgetter.
   * resicableではないので実際の幅ではないが、draggableなエリアとして認識されてしまうので、付箋要素内部に収まるサイズを指定
   */
  get h(): number {
    return 10;
  }
}
</script>

<style scoped lang="scss">
.vdr.active::before {
  outline: none;
}
.sticky-content {
  .viewer {
    padding-top: 0.5rem;
    padding-bottom: 0.5rem;
  }
}
</style>
