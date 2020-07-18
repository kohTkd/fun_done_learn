<template>
  <v-card class="elevation-12">
    <v-toolbar color="accent" dark flat>
      <v-toolbar-title>セッションに参加</v-toolbar-title>
    </v-toolbar>
    <v-card-text>
      <v-form>
        <v-text-field label="セッショントークン" prepend-icon="mdi-key-variant" type="text" v-model="form.token" />
      </v-form>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <OkButton @click="joinSession">参加</OkButton>
    </v-card-actions>
  </v-card>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import SessionForm from '@/models/forms/session-form';

@Component
export default class JoinSession extends Vue {
  form!: SessionForm;
  valid = false;

  created() {
    this.form = new SessionForm();
  }

  joinSession() {
    this.$emit('joinSession', this.form);
  }
}
</script>
