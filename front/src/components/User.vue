<template>
    <div>
        <v-chip v-if="isUserConnected" @input="logout()" close light>
            <v-avatar>
                <img :src="imageURL">
            </v-avatar>
            {{ userName }}
        </v-chip>
        <v-btn v-else icon href="/login">
            <v-icon>account_circle</v-icon>
        </v-btn>
    </div>
</template>

<script>
    export default {
        // When element is mounted
        mounted () {
            this.$store.dispatch('fetchUserConnected')
        },

        // Component methods
        methods: {
            logout () {
                window.location = '/logout'
            },
        },

        // Data generated from other data
        computed: {
            isUserConnected () {
                return this.$store.state.users.connectedUser.user_id
            },

            userName () {
                return this.$store.state.users.connectedUser.name
            },

            imageURL () {
                return this.$store.state.users.connectedUser.picture
            },
        },
    }
</script>
