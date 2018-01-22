<template>
    <div>
        <!-- If laptop, desktop or tablet -->
        <v-toolbar class="hidden-xs-only" :id="id" :color="menuColor" dark dense>
            <v-btn icon>
                <img :src="logo" :alt="title">
            </v-btn>
            <v-toolbar-title>{{ title }}</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn v-for="link in links" :key="link.url" icon :to="link.url" exact router>
                <v-icon>{{ link.icon }}</v-icon>
            </v-btn>
            <ConnectedUser></ConnectedUser>
        </v-toolbar>
        <!-- If mobile phone -->
        <v-tabs dark grow>
            <v-toolbar class="hidden-sm-and-up" :id="id" :color="menuColor" dark dense extended>
                <v-btn icon>
                    <img :src="logo" :alt="title">
                </v-btn>
                <v-toolbar-title>{{ title }}</v-toolbar-title>
                <v-spacer></v-spacer>
                <v-tabs-bar slot="extension">
                    <v-tabs-slider color="white"></v-tabs-slider>
                    <v-tabs-item v-for="link in links" :key="link.url" :to="{path:link.url}">
                        <v-icon>{{ link.icon }}</v-icon>
                    </v-tabs-item>
                </v-tabs-bar>
                <ConnectedUser></ConnectedUser>
            </v-toolbar>
        </v-tabs>
    </div>
</template>

<script>
    import ConnectedUser from './users/ConnectedUser.vue'

    export default {
        // Other components included
        components: {
            ConnectedUser,
        },

        // Component Data
        data () {
            return {
                id: 'navigation',
                title: 'Rugby Fanatic',
                logo: '/static/img/logo_32.png',
                menuColor: 'grey darken-3',
                links: [
                    {url: '/', icon: 'home'},
                    {url: '/game', icon: 'subscriptions'},
                    {url: '/teams', icon: 'library_books'},
                    {url: '/users', icon: 'supervisor_account'},
                ],
            }
        },
    }
</script>
