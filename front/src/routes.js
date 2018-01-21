import Home from './components/Home.vue'
import Game from './components/games/Game.vue'
import Teams from './components/teams/Teams.vue'
import Users from './components/users/Users.vue'

// Routes of vue-router
export default [
    { path: '/', component: Home },
    { path: '/game', component: Game },
    { path: '/teams', component: Teams },
    { path: '/users', component: Users },
]