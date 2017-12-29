<template>
    <v-card id="field" :style="styleField">
        <!-- If the field is vertical -->
        <table v-if="$store.state.game.stadium.isVertical":width="'100%'">
            <tr v-for="i in $store.state.game.stadium.field.long" :key="i">
                <Cell 
                    :cell-id="$store.getters.getFieldCellId(j, 1 + $store.state.game.stadium.field.long - i)"
                    v-for="j in $store.state.game.stadium.field.large"
                    :key="j">
                </Cell>
            </tr>
        </table>
        <!-- If the field is horizontal -->
        <table v-else :width="'100%'">
            <tr v-for="i in $store.state.game.stadium.field.large" :key="i">
                <Cell 
                    :cell-id="$store.getters.getFieldCellId(i,j)"
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
                    backgroundImage: this.imageURL,
                    backgroundSize: '100% 100%',
                }
            },

            imageURL () {
                if (this.$store.state.game.stadium.isVertical) {
                    return 'url("/static/img/' + this.$store.state.game.stadium.field.image + '-vertical.jpg")'
                } else {
                    return 'url("/static/img/' + this.$store.state.game.stadium.field.image + '-horizontal.jpg")'
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