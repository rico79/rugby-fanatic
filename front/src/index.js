import Vue from 'vue'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'

import App from './components/App.vue'

Vue.use(Vuetify)

new Vue({
    el: '#app',
    template: '<App/>',
    components: { App }
})