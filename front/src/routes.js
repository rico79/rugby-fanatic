import Home from './components/Home.vue'
import Game from './components/game/Game.vue'
import Teams from './components/team/Teams.vue'
import Users from './components/user/Users.vue'

// Routes of vue-router
export default [
    { path: '/', component: Home },
    { path: '/game', component: Game },
    { path: '/teams', component: Teams },
    { path: '/users', component: Users },
]