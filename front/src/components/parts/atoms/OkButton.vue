<template>
  <v-btn :disabled="disabled" rounded depressed min-width="120" large color="primary" @click="$emit('click')">
    {{ label }}
  </v-btn>
</template>

<script lang="ts">
import { Component, Vue, Prop } from 'vue-property-decorator';

@Component
export default class OkButton extends Vue {
  @Prop({ default: 'OK' })
  label!: string;
  @Prop({ default: true })
  disabled!: boolean;
}
</script>
