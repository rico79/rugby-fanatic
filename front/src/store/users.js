// Users module
export default {
    state: {
        connectedUser: {
            user_id: false,
            name: false,
            picture: false,
        },

        users: [],
        users_loading: false,
    },

    mutations: {
        setConnectedUser (state, user) {
            state.connectedUser = user
        },

        resetConnectedUser (state) {
            state.connectedUser = {
                user_id: false,
                name: false,
                picture: false,
            }
        },

        setUsers (state, users) {
            state.users = users
        },

        usersAreLoading (state, loading) {
            state.users_loading = loading
        },
    },

    actions: {
        fetchConnectedUser (context) {
            fetch('/connecteduser', {credentials: 'same-origin'})
            .then((resp) => resp.json())
            .then(function(data) {
                if (data.user_id) {
                    context.commit('setConnectedUser', data)
                } else {
                    context.commit('resetConnectedUser')
                }
            })
            .catch(function(error) {
                context.commit('resetConnectedUser')
            })
        },

        fetchUsers (context) {
            context.commit('usersAreLoading', true)

            fetch('/users', {credentials: 'same-origin'})
            .then((resp) => resp.json())
            .then(function(data) {
                context.commit('usersAreLoading', false)
                context.commit('setUsers', data)
            })
            .catch(function(error) {
                context.commit('usersAreLoading', false)
                context.commit('setUsers', [])
            })
        },
    },
}