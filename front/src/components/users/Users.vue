<template>
    <v-app>
        <Navigation></Navigation>
        <v-container>
            <h1>Users</h1>
            <v-progress-circular v-if="usersLoading" indeterminate></v-progress-circular>
            <v-list v-else two-line>
                <v-list-tile avatar v-for="user in users" :key="user.user_id">
                    <v-list-tile-avatar>
                        <img :src="user.picture"/>
                    </v-list-tile-avatar>
                    <v-list-tile-content>
                        <v-list-tile-title>{{ user.name }} ({{ user.locale }})</v-list-tile-title>
                        <v-list-tile-sub-title>{{ user.last_connection }}</v-list-tile-sub-title>
                    </v-list-tile-content>
                    <v-list-tile-action>
                        <v-icon>chat_bubble</v-icon>
                    </v-list-tile-action>
                </v-list-tile>
            </v-list>
        </v-container>
    </v-app>
</template>

<script>
    import Navigation from '../Navigation.vue'

    export default {
        // Other components included
        components: {
            Navigation,
        },

        // When element is mounted
        mounted () {
            this.$store.dispatch('fetchUsers')
        },

        // Data generated from other data
        computed: {
            users () {
                return this.$store.state.users.users
            },

            usersLoading () {
                return this.$store.state.users.users_loading
            },
        },
    }
</script>