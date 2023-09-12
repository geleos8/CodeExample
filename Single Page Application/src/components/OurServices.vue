<template>
  <div class="our-services">
    <div v-if="showSuccessMessage" class="success-message">
      <h3>Информация об условиях аренды отправлена на вашу электронную почту!</h3>
    </div>
    <h2>Выберите конфигурацию сервера:</h2>
    <div class="services">
      <div
        class="service-item"
        v-for="service in services"
        :key="service.id"
        @mouseover="handleMouseOver(service.id)"
        @mouseout="handleMouseOut(service.id)"
      >
        <img :src="service.image" :alt="service.title" />
        <div class="overlay" v-show="hoveredService === service.id">
          <h4>{{ service.title }}</h4>
          <p>{{ service.description }}</p>
          <button @click="openOrderModal(service)">Заказать</button>
        </div>
      </div>
    </div>

    <!-- Модальное окно для заказа -->
    <div class="modal " v-if="showModal">
      <div class="modal-content">
        <span class="close" @click="closeOrderModal">&times;</span>
        <h3>Форма заказа</h3>
        <form @submit.prevent="submitOrderForm">
          <label for="name">Имя:</label>
          <input type="text" id="name" v-model="orderForm.name" required>
          <label for="email">Email:</label>
          <input type="email" id="email" v-model="orderForm.email" required>
          <label for="message">Сообщение:</label>
          <textarea id="message" v-model="orderForm.message"></textarea>
          <button type="submit">Отправить</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      services: [
        {
          id: 1,
          title: 'Эконом',
          description: 'Мог бы захостить на телефоне',
          image: require('@/assets/images/econom.jpg')
        },
        {
          id: 2,
          title: 'Золотая середина',
          description: 'Вся мощь домашнего ПК',
          image: require('@/assets/images/medium.jpg')
        },
        {
          id: 3,
          title: 'Суперкомпьютер',
          description: 'Арендуй сервер Яндекса',
          image: require('@/assets/images/high-end.jpg')
        }
      ],
      hoveredService: null,
      showModal: false,
      showSuccessMessage: false, // Состояние сообщения об успешной отправке заказа

      orderForm: {
        name: '',
        email: '',
        message: ''
      }
    }
  },
  methods: {
    handleMouseOver (serviceId) {
      this.hoveredService = serviceId
    },
    handleMouseOut (serviceId) {
      if (this.hoveredService === serviceId) {
        this.hoveredService = null
      }
    },
    openOrderModal (service) {
      this.showModal = true
    },
    closeOrderModal () {
      this.showModal = false
    },
    submitOrderForm () {
      this.orderForm.name = ''
      this.orderForm.email = ''
      this.orderForm.message = ''
      this.closeOrderModal()
      this.showSuccessMessage = true
      setTimeout(() => {
        this.showSuccessMessage = false
      }, 8000)
    }
  }
}
</script>
