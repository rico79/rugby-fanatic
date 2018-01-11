import game from './store/game.js'
import users from './store/users.js'

// vuex store
export default {
    modules: {
        users: users,
        game: game,
    }
}