<template>
    <ion-page>
        <ion-header>
            <ion-img src="../../public/logo.png" alt=""></ion-img>
            <ion-icon>

            </ion-icon>
        </ion-header>
        <ion-content :fullscreen="true">
            <ion-header collapse="condense">
                <ion-toolbar>
                    <ion-title size="large">Leaderboard</ion-title>
                </ion-toolbar>
            </ion-header>

            <LeaderboardProfile v-for="profile, index in profiles" :name="index + 1 + '. ' +profile.name" :points="profile.points"></LeaderboardProfile>
        </ion-content>
    </ion-page>
</template>

<script lang="ts">
import LeaderboardProfile from '@/components/LeaderboardProfile.vue';
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent, IonIcon } from '@ionic/vue';
import { defineComponent } from 'vue'

export default defineComponent({
    setup() {


        return {}
    },
    components: {
        IonPage,
        IonHeader,
        IonToolbar,
        IonTitle,
        IonContent,
        IonIcon,

        LeaderboardProfile
    },
    computed: {
        profiles: () => [
            { name: "dupa", points: { plus: 20, minus: 10 } },
            { name: "dupa", points: { plus: 20, minus: 10 } },
            { name: "dupa", points: { plus: 20, minus: 10 } },
            { name: "dupa", points: { plus: 20, minus: 10 } },
        ]
    }
})
</script>

<style scoped></style>