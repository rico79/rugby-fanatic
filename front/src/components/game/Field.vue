<template>
    <v-card id="field">
        <!-- If the field is vertical -->
        <table v-if="$store.state.game.stadium.isVertical" :style="styleField" :width="'100%'">
            <tr v-for="i in $store.state.game.stadium.field.long" :key="i">
                <Cell 
                    :id="$store.getters.getFieldCellId(j, 1 + $store.state.game.stadium.field.long - i)" 
                    v-for="j in $store.state.game.stadium.field.large" 
                    :key="j">
                </Cell>
            </tr>
        </table>
        <!-- If the field is horizontal -->
        <table v-else :style="styleField" :width="'100%'">
            <tr v-for="i in $store.state.game.stadium.field.large" :key="i">
                <Cell 
                    :id="$store.getters.getFieldCellId(i,j)" 
                    v-for="j in $store.state.game.stadium.field.long" 
                    :key="j">
                </Cell>
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