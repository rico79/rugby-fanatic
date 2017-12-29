<template>
    <v-avatar 
        :id="player.id" 
        :class="player.color" 
        :size="playerSize" 
        :draggable="true" 
        @dragstart="dragStart($event)"
    >
        <span class="white--text caption"><b>{{ player.number }}</b></span>
    </v-avatar>
</template>

<script>
    export default {
        // Data passed from parent component
        props: ['player'],

        // Component methods
        methods: {
            dragStart (event) {
                event.dataTransfer.setData("text", event.target.id)
            },
        },

        // Data generated from other data
        computed: {
            playerSize () {
                return `${Math.ceil(this.$store.state.game.stadium.cellSize * 0.8)}px`
            },
        },
    }
</script>