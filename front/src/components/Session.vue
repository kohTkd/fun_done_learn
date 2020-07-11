<template>
  <v-container class="fill-height" fluid>
    <v-app-bar app color="info" dark>
      {{ session.title }}
    </v-app-bar>
    <article class="fun-done-learn-session">
      <div class="boards">
        <CircleBoard v-bind:fun="true" />
        <CircleBoard v-bind:done="true" />
        <CircleBoard v-bind:learn="true" />
      </div>
    </article>
  </v-container>
</template>

<style scoped lang="scss">
$width-coefficient: 0.7;

.fun-done-learn-session {
  width: 100% * $width-coefficient;
  margin: 2rem auto;
}
@supports (shape-outside: polygon(0 0, 0 50%, 50% 50%)) {
  .boards {
    display: grid;
    grid-template-columns: repeat(16, 1fr);
    grid-template-rows: repeat(3, 31.25vw * $width-coefficient);

    &::after {
      display: none;
    }

    .board {
      box-sizing: border-box;
      line-height: 1.3;
      overflow: hidden;

      &.circle {
        &.fun {
          /*   outline: .2em solid #f00; */
          grid-column-start: 4;
          grid-column-end: 14;
          grid-row-start: 1;
          grid-row-end: 3;
        }

        &.done {
          /*   outline: .2em solid #0f0; */
          grid-column-start: 1;
          grid-column-end: 11;
          grid-row-start: 2;
          grid-row-end: 4;
        }

        &.learn {
          /*   outline: .2em solid #00f; */
          grid-column-start: 7;
          grid-column-end: 17;
          grid-row-start: 2;
          grid-row-end: 4;
        }
      }

      &.shape {
        font-size: 2.25vw * $width-coefficient;
        border: initial;
        width: initial;
        margin: initial;
        padding: initial;
        &.fun.learn {
          /*   outline: .2em solid #ff0; */
          grid-column-start: 3;
          grid-column-end: 4;
          grid-row-start: 1;
          grid-row-end: 2;
        }

        &.fun.done {
          /*   outline: .2em solid #f0f; */
          grid-column-start: 2;
          grid-column-end: 4;
          grid-row-start: 2;
          grid-row-end: 2;
        }

        &.done.learn {
          /*   outline: .2em solid #0ff; */
          grid-column-start: 3;
          grid-column-end: 5;
          grid-row-start: 2;
          grid-row-end: 2;
        }

        &.fun.done.learn {
          /*   outline: .2em solid #fff; */
          grid-column-start: 3;
          grid-column-end: 3;
          grid-row-start: 2;
          grid-row-end: 2;
        }
      }
    }
  }
}
</style>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import CircleBoard from '@/components/session/CircleBoard.vue';
import Session from '@/models/session';
import SessionsRepository from '@/repositories/sessions-repository';

@Component({
  components: {
    CircleBoard: CircleBoard
  }
})
export default class Start extends Vue {
  session = new Session({});

  mounted() {
    const token = this.$route.params.token;
    this.fetchSession(token);
  }

  private async fetchSession(token: string) {
    return SessionsRepository.find(token).then(response => {
      this.session = new Session(response.data);
      return this.session;
    });
  }
}
</script>
