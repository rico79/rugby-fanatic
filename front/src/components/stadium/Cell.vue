<template>
   <td :style="styleCell" @drop="drop($event)" @dragover="allowDrop($event)"></td>
</template>

<script>
    export default {
        // properties from parent component
        props: ['cellSize'],

        // Component methods
        methods: {
            allowDrop (event) {
                event.preventDefault()
            },

            drop (event) {
                event.preventDefault()
                var data = event.dataTransfer.getData("text")
                event.target.appendChild(document.getElementById(data))
            },
        },

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