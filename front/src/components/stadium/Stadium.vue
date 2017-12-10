<template>
    <v-container v-resize="onResize" id="stadium">
        <Field :window-size="windowSize"></Field>
    </v-container>
</template>

<script>
    import Field from './Field.vue'

    export default {
        components: {
            Field
        },

        data: () => ({
            windowSize: { x: 0, y: 0 }
        }),

        mounted () {
            this.onResize()
        },

        methods: {
            onResize () {
                this.windowSize = { x: window.innerWidth, y: window.innerHeight }
            }
        }
    }
</script>