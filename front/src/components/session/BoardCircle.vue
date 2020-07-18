<template>
  <div v-bind:class="circleClasses">
    <h2>{{ circleName }}</h2>
  </div>
</template>

<script lang="ts">
import { Component, Vue, Prop } from 'vue-property-decorator';
import CircleClass from '@/models/interfaces/circle-class';

@Component
export default class BoardCircle extends Vue {
  @Prop({ default: false })
  fun?: boolean;

  @Prop({ default: false })
  done?: boolean;

  @Prop({ default: false })
  learn?: boolean;

  get circleClasses(): CircleClass {
    return {
      circle: true,
      fun: this.fun,
      done: this.done,
      learn: this.learn
    };
  }

  get circleName(): string {
    if (this.fun) return 'Fun';
    if (this.done) return 'Done';
    if (this.learn) return 'Learn';
    return '';
  }
}
</script>

<style scoped lang="scss">
@import '@/sass/_variables';

.circle {
  box-sizing: border-box;
  overflow: hidden;
  border-radius: 50%;
  border: 0.1em solid;
  width: initial;
  margin: initial;
  padding: initial;
  position: relative;

  h2 {
    position: absolute;
    font-size: 5.6rem;
  }

  &.fun {
    background-color: rgba($fun-color, $circle-opacity);
    border-color: rgba($fun-color, $border-opacity);
    h2 {
      top: 20%;
      left: 50%;
      transform: translateX(-50%);
      color: rgba($fun-color, 1);
    }
  }

  &.done {
    background-color: rgba($done-color, $circle-opacity);
    border-color: rgba($done-color, $border-opacity);
    h2 {
      margin-left: 3rem;
      top: 55%;
      color: rgba($done-color, 1);
    }
  }

  &.learn {
    background-color: rgba($learn-color, $circle-opacity);
    border-color: rgba($learn-color, $border-opacity);
    h2 {
      right: 3rem;
      top: 55%;
      color: rgba($learn-color, 1);
    }
  }
}
</style>
