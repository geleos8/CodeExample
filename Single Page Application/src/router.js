import Vue from 'vue'
import VueRouter from 'vue-router'
import HomePage from './components/HomePage.vue'
import OurServices from './components/OurServices.vue'
import AboutUs from './components/AboutUs.vue'
import ContactUs from './components/ContactUs.vue'

Vue.use(VueRouter)

const routes = [
  { path: '/', component: HomePage },
  { path: '/services', component: OurServices },
  { path: '/about', component: AboutUs },
  { path: '/contact', component: ContactUs }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
