<template>
    <ion-page>
        <Header></Header>

        <ion-content :fullscreen="true">
            <ion-progress-bar :value="0.93"></ion-progress-bar>
            <vue-countdown :time=timeLeft() v-slot="{ days, hours, minutes, seconds }">
                <p style="text-align: center;">
                    Time Remaining: {{ days }}d {{ hours }}h {{ minutes }}m {{ seconds }}s
                </p>
            </vue-countdown>
            <hr>
            <LeaderboardProfile v-for="profile, index in profiles" :name="index + 1 + '. ' + profile.name"
                :points="profile.points"></LeaderboardProfile>

            <NewDenunciation></NewDenunciation>

        </ion-content>

    </ion-page>
</template>

<script lang="ts">
import LeaderboardProfile from '@/components/LeaderboardProfile.vue';
import { IonPage, IonToolbar, IonTitle, IonContent, IonIcon, IonImg, IonGrid, IonRow, IonCol, IonFab, IonFabButton, IonProgressBar } from '@ionic/vue';
import { defineComponent } from 'vue'
import Header from '@/components/Header.vue'
import NewDenunciation from '@/components/NewDenunciation.vue';
import { getLeaderBoard } from '@/service';
import { Person } from '../model'

export default defineComponent({
    setup() {
        return {}
    },
    data() {
        return {
            profiles: Array<Person>()
        }
    },
    methods: {
        timeLeft() {
            const current = Date.now();
            const difference = 1680479999000 - Date.now()
            return difference
        }
    },
    components: {
        IonPage,
        IonToolbar,
        IonTitle,
        IonContent,
        IonIcon,
        IonImg,
        IonGrid, IonRow, IonCol,
        IonFab, IonFabButton,
        IonProgressBar,

        LeaderboardProfile,
        Header,
        NewDenunciation,
    },
    created() {
        getLeaderBoard(1).then(persons => { console.log(persons); this.profiles = persons })
    }
})
</script>

<style scoped></style>