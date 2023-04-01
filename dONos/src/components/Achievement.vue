<template>
    <ion-item>
        <ion-icon :icon="icon" slot="start" size="large" :color="isActive ? 'dark' : 'medium'"></ion-icon>
        <ion-label>
        <ion-text :color="isActive ? 'active' : 'medium'">
                <p><b>{{ title }}</b></p>
                <p>{{ desc }}</p>
            </ion-text>
        </ion-label>
        <ion-icon v-if="isActive" :icon="checkmark" slot="end" size="large" color="success"></ion-icon>
    </ion-item>
</template>

<script lang="ts">
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent, IonInput, IonItem, IonButton, IonLabel, IonIcon, IonText, IonGrid, IonRow } from '@ionic/vue';
import { checkmark } from 'ionicons/icons';
import { defineComponent } from 'vue'

export default defineComponent({
    props: {
        icon: String,
        title: String,
        desc: { type: String, default: "" },
        isActive: { type: Boolean, default: false },
    },
    setup() {
        return { checkmark }
    },
    components: {
        IonPage, IonHeader, IonToolbar, IonTitle, IonContent, IonInput, IonItem, IonButton, IonLabel, IonIcon, IonText, IonGrid, IonRow
    }
})
</script>

<style scoped></style>