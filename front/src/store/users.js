// Users module
export default {
    state: {
        connectedUser: {
            user_id: false,
            name: false,
            picture: false,
        },
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
    },

    actions: {
        fetchConnectedUser (context) {
            // fetch user data
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
    },
}