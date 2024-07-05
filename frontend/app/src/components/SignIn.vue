<template>
  <div class="login-container">
    <div class="left-panel">
      <video class="background-video" autoplay loop muted>
        <source src="../assets/preview.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <div class="video-overlay"></div>
      <div class="content">
        <img class="logo" src="../assets/logo-white.svg" alt="">
        <p>Computer vision healthcare project applying AI for medical insights</p>
      </div>
    </div>
    <div class="right-panel">
      <h2>Sign In</h2>
      <div class="login">
        <input type="email" placeholder="Email address" />
        <input type="password" placeholder="Password" />
        <div class="options">
          <label>
            <input type="checkbox" />
            Remember Password
          </label>
          <a href="#">Reset Password</a>
        </div>
        <button>Login</button>
        <p>
          Don't have an account? <a href="#">Sign up</a>
        </p>
        <button class="google-auth">Authorize with Google</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SignIn'
}
</script>

<style>

html, body {
  height: 90%;
  padding-left: 0%;
}

.login-container {
  display: flex;
  height: 90vh;
  background-color: #f9f9f9;
}

.left-panel {
  flex: 2;
  background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
  color: white;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;

  padding-top: -20px;
  margin-top: -70px;
  margin-left: -20px;
  padding-bottom: 50px;
  overflow: hidden;
}

.left-panel .logo {
  width: 150px;
  margin-bottom: 20px;
}

.left-panel p {
  font-size: 16px;
  max-width: 300px;
  text-align: center;
}

.background-video {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: 1;
}

.video-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(to bottom, rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5));
  z-index: 2;
}

.content {
  position: relative;
  z-index: 3;
  color: white;
  text-align: center;
}

.content .logo {
  width: 180px;
  margin-bottom: 20px;
}

.content h1 {
  font-size: 24px;
  margin-bottom: 10px;
}

.content p {
  font-size: 16px;
  max-width: 300px;
  text-align: center;
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
  background: #007bff;
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
