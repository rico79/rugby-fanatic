<template>
   <td v-bind:style="styleCell"></td>
</template>

<script>
    export default {
        // properties from parent component
        props: ['cellSize'],

        // Data generated from other data
        computed: {
            styleCell () {
                return {
                    width: this.cellSize + 'px',
                    height: this.cellSize + 'px',
                }
            },
        },
    }
</script>

<style>
    td {
        text-align: center;
    }
</style>