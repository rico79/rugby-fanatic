import Vue from 'vue'
import Vuex from 'vuex'
import VueRouter from 'vue-router'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'

import routes from './routes.js'
import storeInstance from './store.js'

Vue.use(Vuex)
Vue.use(VueRouter)
Vue.use(Vuetify)

// vue router
const router = new VueRouter({
    routes,
})

// vuex store
const store = new Vuex.Store(storeInstance)

// App with router
new Vue({
    el: '#app',
    router,
    store,
})