<template>
  <div>
    <NavigationMenu />
    <div class="container mt-5">
      <router-view />
    </div>
    <Modal v-if="showModal" :title="modalTitle" :message="modalMessage" @closeModal="closeModal" />
  </div>
</template>

<script>
import NavigationMenu from './components/NavigationMenu.vue'
import Modal from './components/TheModal.vue'

export default {
  components: {
    NavigationMenu,
    Modal
  },
  data () {
    return {
      showModal: false,
      modalTitle: '',
      modalMessage: ''
    }
  },
  methods: {
    closeModal () {
      this.showModal = false
      this.modalTitle = ''
      this.modalMessage = ''
    }
  }
}
</script>

<style>

@import './css/styles.css';

</style>
