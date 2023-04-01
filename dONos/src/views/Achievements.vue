<template>
    <ion-page>
        <ion-header>
            <ion-toolbar>
                <ion-title>Achievements</ion-title>
            </ion-toolbar>
        </ion-header>
        <ion-content :fullscreen="true">
            <ion-header collapse="condense">
                <ion-toolbar>
                    <ion-title size="large">Profile</ion-title>
                </ion-toolbar>
            </ion-header>

            <Achievement :icon="triangle" title="title" desc="desc"></Achievement>
            <Achievement :icon="triangle" title="title" desc="desc" :is-active="true"></Achievement>
            <Achievement :icon="triangle" title="title" desc="desc"></Achievement>
            <Achievement :icon="triangle" title="title" desc="desc" :is-active="true"></Achievement>
            <Achievement :icon="triangle" title="title" desc="desc"></Achievement>

        </ion-content>
    </ion-page>
</template>

<script lang="ts">
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent } from '@ionic/vue';
import Achievement from '@/components/Achievement.vue';
import { triangle } from 'ionicons/icons';
import { defineComponent } from 'vue'

export default defineComponent({
    setup() {


        return { triangle }
    },
    components: {
        Achievement,
        IonPage, IonHeader, IonToolbar, IonTitle, IonContent
    }
})
</script>

<style scoped></style>