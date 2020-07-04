import Vue from 'vue';
import App from '@/App.vue';
import router from '@/router';
import vuetify from '@/plugins/vuetify';
import globalComponents from '@/plugins/components';
import store from './store';
import axios from 'axios';

Vue.config.productionTip = false;
globalComponents.forEach((component, key) => Vue.component(key, component));

axios.defaults.baseURL = process.env.VUE_APP_API_BASE_URL;
Vue.prototype.$axios = axios;

new Vue({
  router,
  vuetify,
  store,
  render: h => h(App)
}).$mount('#app');
