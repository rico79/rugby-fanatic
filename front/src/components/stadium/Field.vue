<template>
    <table id="field">
        <tr v-for="i in rowNb" :key="i">
            <td v-for="j in colNb" :key="j" v-bind:style="styleCell"></td>
        </tr>
    </table>
</template>

<script>
    export default {
        // properties from parent component
        props: ['rowNb', 'colNb', 'cellSize'],

        // Data generated from other data
        computed: {
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