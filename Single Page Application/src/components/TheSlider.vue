<template>
  <div class="slider-container">
    <transition name="slide">
      <div class="slider-slide" :style="{ transform:'translateX(-${currentIndex * 100}%)'}">
        <img :src="require('@/assets/' + images[currentIndex])" :alt="'Image ' + (currentIndex + 1)" class="slider-image" />
      </div>
    </transition>
    <div class="slider-controls">
      <div class="slider-arrow left" @click="previousImage">
        <i class="fas fa-chevron-left"></i>
      </div>
      <div class="slider-arrow right" @click="nextImage">
        <i class="fas fa-chevron-right"></i>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    images: {
      type: Array,
      required: true
    }
  },
  data () {
    return {
      currentIndex: 0
    }
  },
  methods: {
    previousImage () {
      if (this.currentIndex > 0) {
        this.currentIndex--
      } else {
        this.currentIndex = 7
      }
    },
    nextImage () {
      if (this.currentIndex < this.images.length - 1) {
        this.currentIndex++
      } else {
        this.currentIndex = 0
      }
    },
    startAutoSlide () {
      this.autoSlideInterval = setInterval(() => {
        this.nextImage()
      }, 2000)
    },
    stopAutoSlide () {
      clearInterval(this.autoSlideInterval)
    }
  },
  mounted () {
    // Запуск автоматической прокрутки слайдов при загрузке компонента
    this.startAutoSlide()
  },
  beforeDestroy () {
    // Остановка автоматической прокрутки слайдов перед удалением компонента
    this.stopAutoSlide()
  }
}
</script>
