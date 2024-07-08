<template>
  <div class="login-container">
    <AuthPage />
    <div class="right-panel">
      <h2>Sign Up</h2>
      <div class="login">
        <input v-model="fullName" type="text" placeholder="Full Name" />
        <input v-model="crm" type="text" placeholder="CRM" />
        <input v-model="email" type="text" placeholder="Email" />
        <input v-model="password" type="password" placeholder="Password" />
        <div class="options">
          <label>
            <input v-model="rememberPassword" type="checkbox" />
            Remember Password
          </label>
        </div>
        <button @click="signUp">Sign Up</button>
        <p v-if="message" class="message">{{ message }}</p>
        <p>
          Already have an account?
          <router-link to="/">Sign In</router-link>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import AuthPage from "./AuthPage.vue";

export default {
  name: "SignUp",
  components: {
    AuthPage,
  },
  data() {
    return {
      fullName: "",
      crm: "",
      email: "",
      password: "",
      rememberPassword: false,
      message: "",
    };
  },
  methods: {
    async signUp() {
      try {
        const response = await axios.post("/auth/signup/", {
          full_name: this.fullName,
          crm: this.crm,
          email: this.email,
          password: this.password,
        });

        this.message = response.data.message;
        this.clearFields();
      } catch (error) {
        console.error("Error during signup:", error.response);
        this.message = "Something went wrong. Please try again later.";
      }
    },
    clearFields() {
      this.fullName = "";
      this.crm = "";
      this.email = "";
      this.password = "";
      this.rememberPassword = false;
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
  background-color: white;
}

.right-panel h2 {
  margin-bottom: 35px;
  size: 10px;
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
