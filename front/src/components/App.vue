<template>
    <v-app>
        <Navigation class="hidden-sm-and-down"></Navigation>
        <Stadium></Stadium>
    </v-app>
</template>

<script>
    import Navigation from './Navigation.vue'
    import Stadium from './Stadium.vue'

    export default {
        components: {
            Navigation,
            Stadium
        }
    }
</script>

<style>
</style>
