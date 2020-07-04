<template>
  <v-container class="fill-height" fluid>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="4">This is Session Page. {{ token }}</v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

@Component
export default class Start extends Vue {
  token = '';

  created() {
    this.token = this.$route.params.token;
  }
}
</script>
