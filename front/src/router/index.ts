import Vue from 'vue';
import VueRouter, { RouteConfig } from 'vue-router';
import Index from '@/components/Index.vue';
import SessionBoard from '@/components/SessionBoard.vue';

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'index',
    component: Index
  },
  {
    path: '/sessions/:token',
    name: 'session',
    component: SessionBoard
  }
];

const router = new VueRouter({
  routes
});

export default router;
