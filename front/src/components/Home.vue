<template>
    <v-app>
        <Navigation></Navigation>
        <v-container>
            <h1>Home</h1>
        </v-container>
    </v-app>
</template>

<script>
    import Navigation from './Navigation.vue'

    export default {
        components: {
            Navigation,
        }
    }
</script>