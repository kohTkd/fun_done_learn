<template>
  <VueDragResize :isDraggable="draggable" :isResizable="false" :parentLimitation="true" :x="x" :y="y" :w="w" :h="h" @dragstop="replace">
    <ViewActivityStickyNote v-show="!editable" v-bind:activity="currentActivity" @edit="edit" />
    <EditActivityStickyNote v-if="editable" v-bind:activity="currentActivity" @update="update" @cancel="show" />
  </VueDragResize>
</template>

<script lang="ts">
import { Component, Vue, Prop, Emit, Watch } from 'vue-property-decorator';
import VueDragResize from 'vue-drag-resize';
import Activity from '@/models/activity';
import ViewActivityStickyNote from '@/components/parts/organisms/session-board/sticky-notes/ViewActivityStickyNote.vue';
import EditActivityStickyNote from '@/components/parts/organisms/session-board/sticky-notes/EditActivityStickyNote.vue';
import Placement from '@/models/placement';
import Position from '@/models/interfaces/position';
import PlacementsRepository from '@/repositories/placements-repository';

@Component({
  components: {
    ViewActivityStickyNote: ViewActivityStickyNote,
    EditActivityStickyNote,
    VueDragResize: VueDragResize
  }
})
export default class ActivityStickyNote extends Vue {
  @Prop()
  activity!: Activity;

  currentActivity = Activity.dummy;

  editable = false;
  draggable = true;

  created() {
    this.currentActivity = this.activity;
  }

  @Watch('activity')
  onUpdateActivity(newActivity: Activity, _oldActivity: Activity) {
    this.currentActivity = newActivity;
  }

  @Emit('replaced')
  replace(position: Position) {
    if (position.left != this.activity.left || position.top != this.activity.top) {
      this.activity.place(position);
      return this.updatePlacement(this.activity.placement);
    }
  }

  @Emit('update')
  update(activity: Activity) {
    this.currentActivity.update({ content: activity.content });
    this.show();
    return activity;
  }

  edit() {
    this.editable = true;
    this.draggable = false;
  }

  show() {
    this.editable = false;
    this.draggable = true;
  }

  private async updatePlacement(placement: Placement) {
    const sessionToken = placement.sessionToken;
    const activityToken = placement.activityToken;
    const params = placement.currentPositionParams;
    return PlacementsRepository.update(params, sessionToken, activityToken).then((placement: Placement) => {
      this.activity.placement = placement;
      return this.activity;
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
.sticky-note {
  position: absolute;
  .sticky-content {
    .viewer {
      padding-top: 0.5rem;
      padding-bottom: 0.5rem;
    }
  }
}
</style>
