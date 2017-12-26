<template>
    <table id="field" v-bind:style="styleField">
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
            styleField () {
                var imgUrl = 'url("/static/img/bb-field-horizontal.jpg")'
                if (this.rowNb > this.colNb) {
                    imgUrl = 'url("/static/img/bb-field-vertical.jpg")'
                }

                return {
                    backgroundImage: imgUrl,
                    backgroundSize: '100% 100%',
                }
            },

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
    table, th, td {
        border: 1px solid black;
        border-collapse: collapse;
        text-align: center;
    }
</style>