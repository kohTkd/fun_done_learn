import Vue from 'vue';
import Vuetify from 'vuetify';
import globalComponents from '@/plugins/components';

Vue.use(Vuetify);
globalComponents.forEach((component, key) => Vue.component(key, component));
Vue.config.devtools = false;
Vue.config.productionTip = false;
