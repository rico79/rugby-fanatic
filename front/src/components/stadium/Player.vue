<template>
    <v-avatar id="player" class="grey darken-4" :size="playerSize" :draggable="true" @dragstart="drag($event)">
        <span class="white--text caption"><b>15</b></span>
    </v-avatar>
</template>

<script>
    export default {
        // properties from parent component
        props: ['size'],

        // Component methods
        methods: {
            drag (event) {
                event.dataTransfer.setData("text", event.target.id)
            },
        },

        // Data generated from other data
        computed: {
            playerSize () {
                return `${this.size}px`
            },
        },
    }
</script>