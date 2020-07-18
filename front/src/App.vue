<template>
  <v-app>
    <v-app-bar app clippedRight flat color="primary" dark>
      <h1>Fun Done Learn</h1>
    </v-app-bar>
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

@Component
export default class App extends Vue {}
</script>

<style scoped lang="scss">
main {
  background-image: repeating-linear-gradient(90deg, #ddd, #ddd 1px, transparent 1px, transparent 72px),
    repeating-linear-gradient(0deg, #ddd, #ddd 1px, #fff 1px, #fff 72px);
}
</style>
