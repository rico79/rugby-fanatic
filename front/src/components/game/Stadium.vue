<template>
    <v-container id="stadium" text-xs-center v-resize="onResize">
        <v-layout row wrap>
            <v-flex xs12>
                <Player></Player>
            </v-flex>
            <v-flex xs12>
                <Field></Field>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
    import Field from './Field.vue'
    import Player from './Player.vue'

    export default {
        // Other components included
        components: {
            Field,
            Player,
        },

        // When element is created
        mounted () {
            this.onResize()
        },

        // Component methods
        methods: {
            onResize () {
                this.$store.commit('redesignStadium', 
                    {
                        width: document.getElementById("stadium").clientWidth, 
                        height: document.getElementById("stadium").clientHeight
                    })
            },
        },
    }
</script>