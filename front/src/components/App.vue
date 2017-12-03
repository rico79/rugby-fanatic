<template>
    <v-app id="app">
        <Navigation></Navigation>
        <Field></Field>
    </v-app>
</template>

<script>
    import Navigation from './Navigation.vue'
    import Field from './Field.vue'

    export default {
        components: {
            Navigation,
            Field
        }
    }
</script>

<style>
</style>
