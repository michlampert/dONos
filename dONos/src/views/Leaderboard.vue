<template>
    <ion-page>
        <Header></Header>

        <ion-content :fullscreen="true">

            <LeaderboardProfile v-for="profile, index in profiles" :name="index + 1 + '. ' + profile.name"
                :points="profile.points"></LeaderboardProfile>

                <NewDenunciation></NewDenunciation>
                
        </ion-content>

    </ion-page>

</template>

<script lang="ts">
import LeaderboardProfile from '@/components/LeaderboardProfile.vue';
import { IonPage, IonToolbar, IonTitle, IonContent, IonIcon, IonImg, IonGrid, IonRow, IonCol, IonFab, IonFabButton } from '@ionic/vue';
import { defineComponent } from 'vue'
import Header from '@/components/Header.vue'
import NewDenunciation from '@/components/NewDenunciation.vue';

export default defineComponent({
    setup() {


        return { }
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

        LeaderboardProfile,
        Header,
        NewDenunciation,
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