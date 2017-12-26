<template>
    <v-container id="stadium" v-resize="onResize">
        <Field :row-nb="fieldRowNb" :col-nb="fieldColNb" :cell-size="cellSize"></Field>
    </v-container>
</template>

<script>
    import Field from './Field.vue'

    export default {
        // Other components included
        components: {
            Field,
        },

        // Component data
        data: () => ({
            stadiumSize: { x: 0, y: 0 },
            fieldCells: { long: 26, large: 15 },
        }),

        // When element is created
        mounted () {
            this.onResize()
        },

        // Component methods
        methods: {
            onResize () {
                this.stadiumSize = { 
                    x:  document.getElementById("stadium").clientWidth, 
                    y: document.getElementById("stadium").clientHeight,
                }
            }
        },

        // Data generated from other data
        computed: {
            fieldRowNb () {
               if (this.stadiumSize.x > this.stadiumSize.y) {
                    return this.fieldCells.large
               } else {
                    return this.fieldCells.long
               }
            },

            fieldColNb () {
               if (this.stadiumSize.x > this.stadiumSize.y) {
                    return this.fieldCells.long
               } else {
                    return this.fieldCells.large
               }
            },

            cellSize () {
               if (this.stadiumSize.x / this.fieldColNb < this.stadiumSize.y / this.fieldRowNb) {
                    return Math.floor(this.stadiumSize.x / this.fieldColNb)
               } else {
                    return Math.floor(this.stadiumSize.y / this.fieldRowNb)
               }
            },
        },
    }
</script>