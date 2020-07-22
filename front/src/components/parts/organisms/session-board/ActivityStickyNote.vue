<template>
  <VueDragResize :isResizable="false" :parentLimitation="true" :x="x" :y="y" :w="w" :h="h" @dragstop="place">
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
import Placement from '@/models/placement';
import Position from '@/models/interfaces/position';
import PlacementsRepository from '@/repositories/placements-repository';

@Component({
  components: {
    StickyNote: StickyNote,
    VueDragResize: VueDragResize
  }
})
export default class ActivityViewer extends Vue {
  @Prop()
  activity!: Activity;

  place(position: Position) {
    if (position.left != this.activity.left || position.top != this.activity.top) {
      this.activity.place(position);
      this.updatePlacement(this.activity.placement);
    }
  }

  private async updatePlacement(placement: Placement) {
    const sessionToken = placement.sessionToken;
    const activityToken = placement.activityToken;
    const params = placement.currentPositionParams;
    PlacementsRepository.update(params, sessionToken, activityToken).then((placement: Placement) => {
      this.activity.placement = placement;
    });
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
