<template>
    <v-container id="field" fluid>
        <v-layout row v-for="i in 15" :key="i">
            <v-flex xs1 v-for="j in 24" :key="j">
                <v-card dark tile flat color="green darken-3">
                    <v-card-text>x</v-card-text>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
    import Field from './Field.vue'

    export default {
        components: {
            Field
        }
    }
</script>