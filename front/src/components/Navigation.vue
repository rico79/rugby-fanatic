<template>
    <v-toolbar id="navigation" color="grey darken-3" elevation-10 dark dense>
        <v-btn icon>
            <img src="/static/img/logo_32.png" alt="Rugby Fanatic">
        </v-btn>
        <v-toolbar-title>Rugby Fanatic</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn icon to="/" exact router>
            <v-icon>home</v-icon>
        </v-btn>
        <v-btn icon to="/game" exact router>
            <v-icon>subscriptions</v-icon>
        </v-btn>
        <User></User>
    </v-toolbar>
</template>

<script>
    import User from './User.vue'

    export default {
        components: {
            User,
        }
    }
</script>
