<template>
   <td :style="styleCell" @drop="drop($event)" @dragover="allowDrop($event)"></td>
</template>

<script>
    export default {
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
                    width: this.$store.state.game.stadium.cellSize + 'px',
                    height: this.$store.state.game.stadium.cellSize + 'px',
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