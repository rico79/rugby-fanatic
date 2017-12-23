<template>
    <v-container id="stadium" v-resize="onResize">
        <Field :long="fieldCells.long" :large="fieldCells.large" :field-size="fieldSize"></Field>
    </v-container>
</template>

<script>
    import Field from './Field.vue'

    export default {
        // Other components included
        components: {
            Field
        },

        // Component data
        data: () => ({
            windowSize: { x: 0, y: 0 },
            fieldCells: { long: 26, large: 15 },
        }),

        // When element is created
        mounted () {
            this.onResize()
        },

        // Component methods
        methods: {
            onResize () {
                this.windowSize = { x:  document.getElementById("stadium").clientWidth, y: document.getElementById("stadium").clientHeight }
            }
        },

        // Data generated from other data
        computed: {
            fieldSize () {
               return { x: this.windowSize.x, y: this.windowSize.y }
            },
        },
    }
</script>