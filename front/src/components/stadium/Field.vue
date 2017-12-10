<template>
    <v-container id="field">
        <v-layout row v-for="i in rowNb" :key="i">
            <v-flex xs1 v-for="j in colNb" :key="j">
                <Cell :cell-size="cellSize"></Cell>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
    import Cell from './Cell.vue'

    export default {
        components: {
            Cell
        },

        props: ['windowSize'],

        data: () => ({
            size: {
                long: 26,
                large: 15
            }
        }),

        computed: {
            rowNb () {
               if (this.windowSize.x > this.windowSize.y) {
                   return this.size.large
               } else {
                   return this.size.long
               }
            },

            colNb () {
               if (this.windowSize.x > this.windowSize.y) {
                   return this.size.long
               } else {
                   return this.size.large
               }
            },

            cellSize () {
               if (this.windowSize.x / this.rowNb < this.windowSize.y / this.colNb) {
                   return Math.floor(this.windowSize.x / this.rowNb)
               } else {
                   return Math.floor(this.windowSize.y / this.colNb)
               }
            }
        }
    }
</script>