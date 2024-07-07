<template>
  <div class="home-container">
    <div class="white-box">
      <h1>Test</h1>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomePage'
}
</script>

<style>
body, html {
  margin: 0;
  padding: 0;
  height: 90%;
  background-image: url("../assets/home-background.jpg");
  background-size: cover;
  background-position: center;
}

.home-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 70vh;
}

.white-box {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 35%;
  height: 85%;
  background-color: rgba(255, 255, 255, 0.878);
  border-radius: 2px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.278);
}

.upload-column {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.file-upload-input {
  display: none;
}

.file-upload-label {
  display: inline-block;
  padding: 10px 20px;
  background-color: #143888;
  color: #ffffff;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.file-upload-label:hover {
  background-color: #0d2a5e;
}

.button-custom {
  width: 220px;
  height: 70px;
  margin-top: 20px;
  border-radius: 20px;
  background-color: #ffffff;
  border: 1px solid #ffffff;
  color: #143888;
  transition: background-color 0.3s ease;
}

.button-custom:hover {
  background-color: #143888;
  color: #ffffff;
}
</style>