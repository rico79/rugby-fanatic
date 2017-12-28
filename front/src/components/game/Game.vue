<template>
    <v-app>
        <Navigation></Navigation>
        <Stadium></Stadium>
    </v-app>
</template>

<script>
    import Navigation from '../Navigation.vue'
    import Stadium from './Stadium.vue'

    export default {
        components: {
            Navigation,
            Stadium,
        }
    }
</script>