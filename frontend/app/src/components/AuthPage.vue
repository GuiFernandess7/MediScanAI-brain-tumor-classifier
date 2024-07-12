<template>
  <div class="left-panel">
    <video class="background-video" autoplay loop muted>
      <source src="../assets/preview2.mp4" type="video/mp4" />
      Your browser does not support the video tag.
    </video>
    <div class="video-overlay"></div>
    <div class="content">
      <img class="logo" src="../assets/logo-white.svg" alt="" />
      <p>AI Insights for Accurate Tomography Diagnosis</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "AuthPage",
};
</script>

<style>
html,
body {
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
  background: linear-gradient(
    to bottom,
    rgba(0, 0, 0, 0.5),
    rgba(0, 0, 0, 0.5)
  );
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
</style>
