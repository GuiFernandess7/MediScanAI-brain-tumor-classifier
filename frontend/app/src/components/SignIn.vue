<template>
  <div class="login-container">
    <AuthPage />
    <div class="right-panel">
      <h2>Sign In</h2>
      <div class="login">
        <input v-model="crm" type="text" placeholder="CRM" />
        <input v-model="password" type="password" placeholder="Password" />
        <div class="options">
          <label>
            <input v-model="rememberPassword" type="checkbox" />
            Remember Password
          </label>
          <a href="#">Reset Password</a>
        </div>
        <button class="login-button" @click="login">Log In</button>
        <p v-if="message" class="message">{{ message }}</p>
        <p>
          Don't have an account?
          <router-link to="/signup">Sign up</router-link>
        </p>
        <button class="google-auth">Authorize with Google</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import AuthPage from "./AuthPage.vue";

export default {
  name: "SignIn",
  components: {
    AuthPage,
  },
  data() {
    return {
      crm: "",
      password: "",
      message: "",
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post("/auth/login/", {
          crm: this.crm,
          password: this.password,
        });

        this.message = response.data.message;
        this.redirectToHome();
      } catch (error) {
        console.error("Error during login:", error.response);
        this.message = "Invalid credentials. Please try again.";
      }
    },
    redirectToHome() {
      this.$router.push("/home");
    },
  },
};
</script>

<style>
html,
body {
  height: 90%;
  padding-left: 0%;
}

.message {
  font-size: 14px;
  margin-top: 5px;
}

.right-panel {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 20px;
  margin-right: -8px;
  margin-top: -59px;
}

.right-panel h2 {
  margin-bottom: 35px;
  size: 15px;
  color: #333;
}

.login {
  width: 100%;
  max-width: 300px;
}

.login input {
  width: 100%;
  height: 40px;
  padding-left: 20px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.login .options {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.login .options label {
  display: flex;
  align-items: center;
  font-size: 14px;
  color: #666;
}

.login .options label input {
  height: auto;
  margin-right: 5px;
}

.login .options a {
  font-size: 14px;
  color: #007bff;
  text-decoration: none;
}

.login .options a:hover {
  text-decoration: underline;
}

.login button {
  width: 100%;
  height: 40px;
  background: #143888;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-bottom: 20px;
}

.login button:hover {
  background: #0056b3;
}

.login p {
  text-align: center;
  margin-bottom: 20px;
}

.login p a {
  color: #007bff;
  text-decoration: none;
}

.login p a:hover {
  text-decoration: underline;
}

.google-auth {
  width: 100%;
  height: 40px;
  background: #db4437;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.google-auth:hover {
  background: #c23321;
}
</style>
