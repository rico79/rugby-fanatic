import Vue from 'vue'
import VueRouter from 'vue-router'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'

import Home from './components/Home.vue'
import Game from './components/Game.vue'

Vue.use(VueRouter)
Vue.use(Vuetify)

// Routes of vue-router
const routes = [
    { path: '/', component: Home },
    { path: '/game', component: Game },
];

// view router
const router = new VueRouter({
    routes,
});

// App with router
new Vue({
    el: '#app',
    router,
})