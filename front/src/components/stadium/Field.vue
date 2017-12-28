<template>
    <v-card id="field">
        <table :style="styleField" :width="'100%'">
            <tr v-for="i in verticalCellNb" :key="i">
                <Cell v-for="j in horizontalCellNb" :key="j" :cell-size="cellSize"></Cell>
            </tr>
        </table>
    </v-card>
</template>

<script>
    import Cell from './Cell.vue'

    export default {
        // Other components included
        components: {
            Cell,
        },

        // properties from parent component
        props: ['field', 'isVertical', 'cellSize'],

        // Data generated from other data
        computed: {
            styleField () {
                return {
                    backgroundImage: this.imgUrl,
                    backgroundSize: '100% 100%',
                }
            },

            imgUrl () {
                if (this.isVertical) {
                    return 'url("/static/img/' + this.field.image + '-vertical.jpg")'
                } else {
                    return 'url("/static/img/' + this.field.image + '-horizontal.jpg")'
                }
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
        },
    }
</script>

<style>
    table {
        border-collapse: collapse;
    }
</style>