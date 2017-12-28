<template>
    <v-container id="stadium" text-xs-center v-resize="onResize">
        <v-layout row wrap>
            <v-flex xs12>
                <Player :size="cellSize"></Player>
            </v-flex>
            <v-flex xs12>
                <Field :field="field" :is-vertical="isFieldVertical" :cell-size="cellSize"></Field>
            </v-flex>
        </v-layout>
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
            isFieldVertical () {
                return ! (this.stadiumSize.x > this.stadiumSize.y)
            },

            fieldVerticalCellNb () {
                if (this.isFieldVertical) {
                    return this.field.long
                } else {
                    return this.field.large
                }
            },

            fieldHorizontalCellNb () {
                if (this.isFieldVertical) {
                    return this.field.large
                } else {
                    return this.field.long
                }
            },

            cellSize () {
                if (this.stadiumSize.x / this.fieldHorizontalCellNb < this.stadiumSize.y / this.fieldVerticalCellNb) {
                    return Math.floor(this.stadiumSize.x / this.fieldHorizontalCellNb)
                } else {
                    return Math.floor(this.stadiumSize.y / this.fieldVerticalCellNb)
                }
            },
        },
    }
</script>