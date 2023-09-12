<template>
  <div>
    <h2></h2>
    <form @submit.prevent="submitForm">
      <div>
        <label for="name">Имя:</label>
        <input type="text" id="name" v-model="formData.name" required>
      </div>
      <div>
        <label for="email">Электронная почта:</label>
        <input type="email" id="email" v-model="formData.email" required>
      </div>
      <div>
        <label for="message">Сообщение:</label>
        <textarea id="message" v-model="formData.message" required></textarea>
      </div>
      <button class = "btn btn-primary bg-dark" type="submit">Отправить</button>
    </form>
    <!-- Модальное окно успеха отправки -->
    <div v-if="showSuccessModal" class="modal">
      <div class="modal-content">
        <h3>Отправлено!</h3>
        <p>Ваше сообщение было успешно отправлено.</p>
        <button @click="closeModal">Закрыть</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      formData: {
        name: '',
        email: '',
        message: ''
      },
      showSuccessModal: false
    }
  },
  methods: {
    submitForm () {
      // Ваша логика отправки формы обратной связи
      // Вы можете отправить данные на сервер или выполнить другие действия
      // Для примера, мы просто открываем модальное окно успеха отправки
      this.showSuccessModal = true
    },
    closeModal () {
      this.showSuccessModal = false
    }
  }
}
</script>
<style scoped>
form div {
  margin-bottom: 10px;
}

label {
  display: block;
  font-weight: bold;
}

input,
textarea {
  width: 30%;
}

/* Стили модального окна */
.modal {
  position: center;
  top: 25%;
  left: 30%;
  width: 40%;
  height: 50%;
  background-color: rgba(0, 0, 0, 0);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background-color: #bbbbbb;
  padding: 20px;
  border-radius: 4px;
  text-align: center;
}

.modal button {
  margin-top: 10px;
}
</style>
