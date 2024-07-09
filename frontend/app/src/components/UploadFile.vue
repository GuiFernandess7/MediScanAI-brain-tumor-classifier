<template>
  <div class="card">
    <div class="top">
      <p>Drag & drop images</p>
    </div>
    <div class="drag-area">
      <span v-if="!isDragging">
        Drag & drop image here or
        <span class="select" role="button" @click="selectFiles"> Choose </span>
      </span>
      <div class="select">Drop image here</div>
      <input name="image" type="file" ref="fileInput" @change="onFileSelect" />
    </div>
    <div class="container">
      <div class="image" v-if="image">
        <span class="delete" @click="removeImage">&times;</span>
        <img :src="image.url" />
      </div>
    </div>
    <button type="button" @click="submitFile" :disabled="loading">
      Analyse
    </button>
    <p v-if="loading">Uploading...</p>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "UploadFile",
  data() {
    return {
      image: null,
      isDragging: false,
      loading: false,
    };
  },
  methods: {
    selectFiles() {
      this.$refs.fileInput.click();
    },
    onFileSelect(event) {
      const file = event.target.files[0];
      if (!file) return;
      if (file.type.split("/")[0] !== "image") return;
      this.image = { name: file.name, url: URL.createObjectURL(file) };
      this.img_file = file;
    },
    removeImage() {
      this.image = null;
      this.$refs.fileInput.value = null;
    },

    async submitFile() {
      if (!this.image) {
        alert("No file selected!");
        return;
      }
      const formData = new FormData();
      formData.append("image", this.img_file);
      formData.append("category", "Brain");

      this.loading = true;
      this.$emit("loading", true);

      try {
        const response = await axios.post(
          "/api/v1/add-tomography/?patient_id=1",
          formData,
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        );

        console.log("File uploaded successfully", response.data);
        this.$emit("upload-success", response.data);
      } catch (error) {
        console.error("Error uploading file", error);
        this.$emit("upload-failure", error);
      } finally {
        this.loading = false;
        this.$emit("loading", false);
      }
    },
  },
};
</script>

<style scoped>
.card {
  width: 100%;
  padding: 10px;
  box-shadow: 0 0 5px #fff;
  border-radius: 5px;
  overflow: hidden;
}

.card .top {
  text-align: center;
}

.card p {
  font-weight: bold;
  color: #143888;
}

.card button {
  outline: 0;
  border: 0;
  color: #fff;
  border-radius: 4px;
  font-weight: 400;
  padding: 8px 13px;
  width: 100%;
  background: #143888;
  transition: background-color 0.3s ease;
}

.card button:hover {
  background-color: #0f0a0a;
}

.card .drag-area {
  height: 150px;
  border-radius: 5px;
  border: 2px dashed #143888;
  background: #fff;
  color: #143888;
  display: flex;
  justify-content: center;
  align-items: center;
  user-select: none;
  -webkit-user-select: none;
  margin-top: 10px;
}

.card .drag-area .visible {
  font-size: 18px;
}

.card .select {
  color: #2f0101;
  margin-left: 5px;
  cursor: pointer;
  transition: 0.4s;
}

.card .select:hover {
  opacity: 0.6;
}

.card .container {
  width: 100%;
  height: auto;
  display: flex;
  justify-content: flex-start;
  align-items: flex-start;
  flex-wrap: wrap;
  max-height: 200px;
  position: relative;
  margin-bottom: 8px;
}

.card .container .image {
  width: 75px;
  margin-right: 5px;
  height: 75px;
  position: relative;
  margin-bottom: 8px;
}

.card .container .image img {
  width: 100%;
  height: 100%;
  border-radius: 5px;
}

.card .container .image span {
  position: absolute;
  top: -2px;
  right: 9px;
  font-size: 20px;
  cursor: pointer;
}

.card .drag-area .on-drop,
.card .drag-area.dragover .visible {
  display: none;
}

.delete {
  z-index: 999;
  color: #143888;
}
</style>
