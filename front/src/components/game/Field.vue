<template>
    <v-card id="field">
        <table :style="styleField" :width="'100%'">
            <tr v-for="i in $store.state.game.stadium.field.verticalCellNb" :key="i">
                <Cell v-for="j in $store.state.game.stadium.field.horizontalCellNb" :key="j"></Cell>
            </tr>
        </table>
    </v-card>
</template>

<script>
    import Cell from './Cell.vue'

    export default {
        // Other components included
        components: {
            Cell,
        },

        // Data generated from other data
        computed: {
            styleField () {
                return {
                    backgroundImage: this.$store.state.game.stadium.field.imageURL,
                    backgroundSize: '100% 100%',
                }
            },
        },
    }
</script>

<style>
    table {
        border-collapse: collapse;
    }
</style>