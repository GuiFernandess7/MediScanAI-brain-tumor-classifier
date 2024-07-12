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
        <div v-else-if="!loading && Object.keys(uploadResult).length > 0">
          <div class="progress-container">
            <p>Glioma: {{ formatPercentage(uploadResult.data.glioma) }}%</p>
            <progress
              :value="uploadResult.data.glioma * 100"
              max="100"></progress>
          </div>
          <div class="progress-container">
            <p>
              Meningioma: {{ formatPercentage(uploadResult.data.meningioma) }}%
            </p>
            <progress
              :value="uploadResult.data.meningioma * 100"
              max="100"></progress>
          </div>
          <div class="progress-container">
            <p>
              Pituitary: {{ formatPercentage(uploadResult.data.pituitary) }}%
            </p>
            <progress
              :value="uploadResult.data.pituitary * 100"
              max="100"></progress>
          </div>
          <div class="progress-container">
            <p>Notumor: {{ formatPercentage(uploadResult.data.notumor) }}%</p>
            <progress
              :value="uploadResult.data.notumor * 100"
              max="100"></progress>
          </div>
        </div>
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
    async handleUploadSuccess(result) {
      if (result) {
        this.uploadResult = result;
        console.log(this.uploadResult.data.glioma);
      }
    },
    handleLoading(isLoading) {
      this.loading = isLoading;
    },
    formatPercentage(value) {
      return (value * 100).toFixed(2);
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
  height: 90%;
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

progress {
  width: 100%;
  height: 20px;
  -webkit-appearance: none;
  appearance: none;
}

progress::-webkit-progress-bar {
  background-color: #f3f3f3;
  border-radius: 5px;
}

progress::-webkit-progress-value {
  background-color: #4caf50;
  border-radius: 5px;
}

progress::-moz-progress-bar {
  background-color: #4caf50;
  border-radius: 5px;
}
</style>
