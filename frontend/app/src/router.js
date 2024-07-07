import { createWebHistory, createRouter } from 'vue-router'
import SignIn from './components/SignIn.vue'
import SignUp from './components/SignUp.vue'
import HomePage from './components/HomePage.vue'

const routes = [
  {
    path: '/',
    name: 'signIn',
    component: SignIn
  },
  {
    path: '/signup',
    name: 'signUp',
    component: SignUp
  },
  {
    path: '/home',
    name: 'home',
    component: HomePage
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router