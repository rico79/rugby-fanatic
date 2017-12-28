<template>
    <v-avatar id="player" class="black" :size="playerSize" :draggable="true" @dragstart="drag($event)">
        <span class="white--text body-1"><b>15</b></span>
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