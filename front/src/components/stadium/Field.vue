<template>
    <table id="field" v-resize="onResize">
        <tr v-for="i in rowNb" :key="i">
            <td v-for="j in colNb" :key="j" v-bind:style="styleCell"></td>
        </tr>
    </table>
</template>

<script>
    export default {
        // properties from parent component
        props: ['long', 'large', 'fieldSize'],

        // Data generated from other data
        computed: {
            rowNb () {
               if (this.fieldSize.x > this.fieldSize.y) {
                   return this.large
               } else {
                   return this.long
               }
            },

            colNb () {
               if (this.fieldSize.x > this.fieldSize.y) {
                   return this.long
               } else {
                   return this.large
               }
            },

            cellSize () {
               if (this.fieldSize.x / this.colNb < this.fieldSize.y / this.rowNb) {
                   return Math.floor(this.fieldSize.x / this.colNb)
               } else {
                   return Math.floor(this.fieldSize.y / this.rowNb)
               }
            },

            styleCell () {
               return { width: this.cellSize + 'px', height: this.cellSize + 'px' }
            }
        },
    }
</script>

<style>
    table, th, td {
        border: 1px solid black;
        border-collapse: collapse;
        text-align: center;
    }
</style>