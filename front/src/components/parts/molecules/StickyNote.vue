<template>
  <div class="sticky-note">
    <div class="sticky-container">
      <div class="sticky-content">
        <slot name="content" />
      </div>
      <div class="sticky-menu">
        <slot name="menu" />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue, Prop } from 'vue-property-decorator';

@Component
export default class StickyNote extends Vue {
  @Prop({ default: false })
  draggable!: boolean;
}
</script>

<style scoped lang="scss">
@import '@/sass/_variables';

.sticky-note {
  width: $sticky-note-width;
  box-shadow: 0.25rem 0 0.25rem rgba(0, 0, 0, 0.1);
  background-image: linear-gradient(90deg, hsla(0, 0%, 45%, 0.1) 2rem, hsla(0, 100%, 100%, 0) 2.5rem),
    linear-gradient(90deg, hsla(60, 100%, 85%, 1), hsla(60, 100%, 85%, 1));
  box-sizing: border-box;

  position: absolute;

  .sticky-container {
    padding: 0;
    margin: 0;
    position: relative;
    display: flex;
    align-items: center;

    .sticky-content {
      padding-left: 2.3rem;
      text-overflow: ellipsis;
      width: calc(100% - 2.5rem);
    }

    .sticky-menu {
      text-align: right;
    }

    &::after {
      content: '';
      display: block;
      position: absolute;
      z-index: -1;
      bottom: 3px;
      right: 0;
      height: 10px;
      width: 99%;
      background-color: rgba(0, 0, 0, 0.1);
      box-shadow: 0.25rem 0.25rem 0.25rem rgba(0, 0, 0, 0.1);
      transform: rotate(2deg);
    }
  }
}
</style>
