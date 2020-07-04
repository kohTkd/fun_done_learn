import Vue from 'vue';
import { VueConstructor } from 'vue/types/umd';
import OkButton from '@/components/parts/atoms/OkButton.vue';

const globalComponents = new Map<string, VueConstructor<Vue>>();
globalComponents.set('OkButton', OkButton);

export default globalComponents;
