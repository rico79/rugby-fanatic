<template>
    <div>
        <!-- If laptop, desktop or tablet -->
        <v-toolbar class="hidden-xs-only" :id="id" :color="menuColor" elevation-10 dark dense>
            <v-btn icon>
                <img :src="logo" :alt="title">
            </v-btn>
            <v-toolbar-title>{{ title }}</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn v-for="link in links" :key="link.url" icon :to="link.url" exact router>
                <v-icon>{{ link.icon }}</v-icon>
            </v-btn>
            <User></User>
        </v-toolbar>
        <!-- If mobile phone -->
        <v-toolbar class="hidden-sm-and-up" :id="id" :color="menuColor" elevation-10 dark dense extended>
            <v-btn icon>
                <img :src="logo" :alt="title">
            </v-btn>
            <v-toolbar-title>{{ title }}</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn v-for="link in links" :key="link.url" icon :to="link.url" exact router slot="extension">
                <v-icon>{{ link.icon }}</v-icon>
            </v-btn>
            <User></User>
        </v-toolbar>
    </div>
</template>

<script>
    import User from './User.vue'

    export default {
        // Other components included
        components: {
            User,
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
