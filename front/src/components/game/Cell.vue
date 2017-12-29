<template>
   <td :id="cellId" :style="styleCell" @drop="drop($event)" @dragover="dragOver($event)">
       <Player v-if="playerInCell" :player="playerInCell"></Player>
   </td>
</template>

<script>
    import Player from './Player.vue'

    export default {
        // Other components included
        components: {
            Player,
        },

        // Data passed from parent component
        props: ['cellId'],

        // Component methods
        methods: {
            dragOver (event) {
                event.preventDefault()
            },

            drop (event) {
                event.preventDefault()
                var playerId = event.dataTransfer.getData("text")
                var cellId = event.target.id
                event.target.appendChild(document.getElementById(playerId))
                this.$store.commit('playerMovesTo', { playerId: playerId, cellId: this.cellId })
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

            playerInCell () {
                return this.$store.getters.getPlayerInCell(this.cellId)
            },
        },
    }
</script>

<style>
    td {
        text-align: center;
    }
</style>