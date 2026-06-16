import { createRouter, createWebHashHistory } from 'vue-router'
import LayoutDefault from '@/layout/default.vue'
import Home from '@/views/Home/index.vue'

const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    {
      path: '/',
      component: LayoutDefault,
      children: [
        {
          path: '',
          component: Home,
        },
      ],
    },
  ],
})

export default router
