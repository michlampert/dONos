<template>
    <ion-header>
        <ion-toolbar>
            <ion-buttons slot="start">
                <ion-button @click="cancel()">Cancel</ion-button>
            </ion-buttons>
            <ion-row>
                <ion-col></ion-col>
                <ion-col>
                    <ion-title>New</ion-title>
                </ion-col>
                <ion-col></ion-col>
            </ion-row>
            <ion-buttons slot="end">
                <ion-button :strong="true" @click="confirm()">Confirm</ion-button>
            </ion-buttons>
        </ion-toolbar>
    </ion-header>
    <ion-content class="ion-padding">
        <ion-item>
            <ion-label position="stacked">Enter your name</ion-label>
            <ion-input ref="input" type="text" placeholder="Your name"></ion-input>
        </ion-item>

        <ion-item>
            <ion-label position="stacked">Enter your name</ion-label>
            <ion-input ref="input" type="text" placeholder="Your name"></ion-input>
        </ion-item>
        <ion-item>
            <ion-button @click="takePhoto()">Take Photo</ion-button>
        </ion-item>
    </ion-content>
</template>
  
<script lang="ts">
import {
    IonContent,
    IonHeader,
    IonTitle,
    IonToolbar,
    IonButtons,
    IonButton,
    IonItem,
    IonLabel,
    IonInput,
    IonRow,
    IonCol,
    modalController,
    toastController,
} from '@ionic/vue';
import { Camera, CameraResultType, CameraSource, Photo } from '@capacitor/camera';
import { defineComponent } from 'vue';
import { showToast } from '../toast'

export default defineComponent({
    name: 'Modal',
    components: { IonContent, IonHeader, IonTitle, IonToolbar, IonButtons, IonButton, IonItem, IonLabel, IonInput, IonRow, IonCol, },
    setup() {
        const takePhoto = async () => {
            const photo = await Camera.getPhoto({
                resultType: CameraResultType.Uri,
                source: CameraSource.Camera,
                quality: 100,
            });
        };

        return {
            takePhoto,
        };
    },
    methods: {
        cancel() {
            return modalController.dismiss(null, 'cancel');
        },
        confirm() {
            showToast("Good job! :)")
            return modalController.dismiss(null, 'confirm');
        },
    },
});
</script>