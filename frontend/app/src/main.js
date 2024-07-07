import App from './App.vue'
import router from './router'
import { createApp } from 'vue'
import BootstrapVue3 from 'bootstrap-vue-3'

import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";

const app = createApp(App)
app.use(BootstrapVue3)
app.use(router)
app.mount('#app')