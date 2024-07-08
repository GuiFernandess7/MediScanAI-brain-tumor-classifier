import App from "./App.vue";
import router from "./router";
import { createApp } from "vue";
import axios from "axios";

const app = createApp(App);

axios.defaults.baseURL = "http://localhost:8000";

app.use(router);
app.mount("#app");
