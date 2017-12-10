<template>
    <v-container id="field">
        <v-layout row v-for="i in getLarge()" :key="i">
            <v-flex xs1 v-for="j in getLong()" :key="j">
                <v-card flat color="green darken-4">
                    <v-card-text></v-card-text>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
    export default {
        props: ['windowSize'],

        data: () => ({
            size: {
                long: 26,
                large: 15
            }
        }),

        methods: {
            getLarge () {
               if (this.windowSize.x > this.windowSize.y) {
                   return this.size.large
               } else {
                   return this.size.long
               }
            },

            getLong () {
               if (this.windowSize.x > this.windowSize.y) {
                   return this.size.long
               } else {
                   return this.size.large
               }
            }
        }
    }
</script>