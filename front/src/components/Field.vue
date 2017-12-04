<template>
    <v-container id="field" text-xs-center>
        <v-layout row v-for="i in 15" :key="i">
            <v-flex xs1 v-for="j in 24" :key="j">
                <v-card dark flat color="green darken-4">
                    <v-card-text></v-card-text>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>
</template>