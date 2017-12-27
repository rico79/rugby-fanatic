<template>
    <span id="player" :draggable="true" @dragstart="drag($event)"><b>15</b></span>
</template>

<script>
    export default {
        // Component methods
        methods: {
            drag (event) {
                event.dataTransfer.setData("text", event.target.id)
            },
        },
    }
</script>