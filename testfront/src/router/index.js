import { createRouter, createWebHistory } from 'vue-router';
import store from '../store';
import Home from '../views/FormentPage.vue';
import Login from '../views/LoginPage.vue';
import Signup from '../views/RegisterPage.vue'; 
import commercial from '../views/FormCommercial.vue'; 

const authGuard = (to, from, next) => {
  if (store.state.isAuthenticated) {
    next();
  } else {
    next('/login');
  }
};

const routes = [
  {
    path: '/',
    redirect: '/home',
  },
  {
    path: '/login',
    component: Login,
  },
  {
    path: '/register',
    component: Signup,
  },
  {
    path: '/home',
    component: Home,
    beforeEnter: authGuard,
  },
  {
    path: '/commercial',
    component: commercial,
    beforeEnter: authGuard,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;