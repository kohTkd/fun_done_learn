<template>
  <div v-bind:class="boardClasses">
    <h2>{{ boardName }}</h2>
  </div>
</template>

<style scoped lang="scss">
$fun-color: #0050ef;
$done-color: #d80073;
$learn-color: #e3c800;
$circle-opacity: 0.3;

.circle {
  border-radius: 50%;
  border: 0.1em solid;
  width: initial;
  margin: initial;
  padding: initial;
  position: relative;

  h2 {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    margin: auto;
    font-size: 3rem;
  }

  &.fun {
    background-color: rgba($fun-color, $circle-opacity);
    border-color: rgba($fun-color, 1);
    h2 {
      color: rgba($fun-color, 1);
    }
  }

  &.done {
    background-color: rgba($done-color, $circle-opacity);
    border-color: rgba($done-color, 1);
    h2 {
      color: rgba($done-color, 1);
    }
  }

  &.learn {
    background-color: rgba($learn-color, $circle-opacity);
    border-color: rgba($learn-color, 1);
    h2 {
      color: rgba($learn-color, 1);
    }
  }
}
</style>

<script lang="ts">
import { Component, Vue, Prop } from 'vue-property-decorator';
import BoardClass from '@/models/interfaces/board-class';

@Component
export default class CircleBoard extends Vue {
  @Prop({ default: false })
  fun?: boolean;

  @Prop({ default: false })
  done?: boolean;

  @Prop({ default: false })
  learn?: boolean;

  get boardClasses(): BoardClass {
    return {
      board: true,
      circle: true,
      fun: this.fun,
      done: this.done,
      learn: this.learn
    };
  }

  get boardName(): string {
    if (this.fun) return 'Fun';
    if (this.done) return 'Done';
    if (this.learn) return 'Learn';
    return '';
  }
}
</script>
