<template>
    <v-container id="stadium" v-resize="onResize">
        <Player></Player>
        <Field :field="field" :is-vertical="isVertical" :cell-size="cellSize"></Field>
    </v-container>
</template>

<script>
    import Field from './Field.vue'
    import Player from './Player.vue'

    export default {
        // Other components included
        components: {
            Field,
            Player,
        },

        // Component data
        data: () => ({
            stadiumSize: { 
                x: 0, 
                y: 0 
            },

            field: {
                long: 26, 
                large: 17,
                image: 'rugby-field',
            },
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
            },
        },

        // Data generated from other data
        computed: {
            isVertical () {
                return ! (this.stadiumSize.x > this.stadiumSize.y)
            },

            verticalCellNb () {
                if (this.isVertical) {
                    return this.field.long
                } else {
                    return this.field.large
                }
            },

            horizontalCellNb () {
                if (this.isVertical) {
                    return this.field.large
                } else {
                    return this.field.long
                }
            },

            cellSize () {
                if (this.stadiumSize.x / this.horizontalCellNb < this.stadiumSize.y / this.verticalCellNb) {
                    return Math.floor(this.stadiumSize.x / this.horizontalCellNb)
                } else {
                    return Math.floor(this.stadiumSize.y / this.verticalCellNb)
                }
            },
        },
    }
</script>