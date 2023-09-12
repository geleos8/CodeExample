<template>
  <div>
    <h1 class="tab-title">Обратная связь</h1>
    <p class="tab-text">
      Мы ценим ваше мнение и готовы ответить на ваши вопросы. Пожалуйста, заполните форму ниже, чтобы связаться с нами.
    </p>
    <Form></Form>
  </div>
</template>

<script>
import Form from '@/components/TheForm.vue'

export default {
  name: 'TheTab3',
  components: {
    Form
  }
}
</script>
