import { createMemoryHistory, createRouter } from 'vue-router'
import SignIn from './components/SignUp.vue'
import SignUp from './components/SignUp.vue'

const routes = [
  {
    path: '/',
    name: 'SignIn',
    component: SignIn
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp
  }
]

const router = createRouter({
    history: createMemoryHistory(),
    routes,
})

export default router
