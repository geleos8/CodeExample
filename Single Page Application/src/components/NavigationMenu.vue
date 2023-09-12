<template>
  <nav class="navbar navbar-expand-md navbar-dark bg-dark">
    <router-link class="navbar-brand" to="/">Аренда серверов</router-link>
    <button
      class="navbar-toggler"
      type="button"
      data-toggle="collapse"
      data-target="#navbarNav"
      aria-controls="navbarNav"
      aria-expanded="false"
      aria-label="Toggle navigation"
      @click="toggleMobileMenu"
    >
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav" :class="{ show: isMobileMenuOpen }">
      <ul class="navbar-nav">
        <li class="nav-item">
          <router-link class="nav-link" to="/">Главная</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" to="/about">О наших серверах</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" to="/services">Услуги</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" to="/contact">Контакты</router-link>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
export default {
  data () {
    return {
      isMobileMenuOpen: false
    }
  },
  methods: {
    toggleMobileMenu () {
      this.isMobileMenuOpen = !this.isMobileMenuOpen
    }
  }
}
</script>
