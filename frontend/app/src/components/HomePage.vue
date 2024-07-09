<template>
  <div class="home-container">
    <div class="white-box">
      <div class="left-side">
        <UploadFile
          @upload-success="handleUploadSuccess"
          @loading="handleLoading" />
      </div>
      <div class="right-side">
        <img
          v-if="uploadResult.image"
          :src="uploadResult.image"
          alt="Tomography" />
        <p v-else-if="loading">Loading...</p>
        <p v-else-if="!loading && Object.keys(uploadResult).length > 0">
          Glioma: {{ uploadResult.glioma }} <br />
          Meningioma: {{ uploadResult.meningioma }} <br />
          Pituitary: {{ uploadResult.pituitary }} <br />
          Notumor: {{ uploadResult.notumor }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import UploadFile from "./UploadFile.vue";

export default {
  name: "HomePage",
  components: {
    UploadFile,
  },
  data() {
    return {
      uploadResult: {},
      loading: false,
    };
  },
  methods: {
    handleUploadSuccess(result) {
      this.uploadResult = result;
    },
    handleLoading(isLoading) {
      this.loading = isLoading;
    },
  },
};
</script>

<style>
body {
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
  width: 90%;
  height: 85%;
  max-width: 800px;
  background-color: rgb(255, 255, 255);
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(254, 254, 254, 0.93);
  padding: 20px;
}

.left-side,
.right-side {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.left-side {
  flex: 0.5;
  padding-right: 10px;
}

.right-side {
  flex: 0.5;
  padding-left: 10px;
}

.results-container {
  text-align: center;
}
</style>
