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
            <ion-label position="stacked">Receivers</ion-label>
            <ion-input :value="input" type="number" placeholder="Your name" @ionInput="onInput($event)"></ion-input>
        </ion-item>

        <ion-item>
            <ion-label position="stacked">Enter your name</ion-label>
            <ion-input :value="content" type="text" placeholder="Your name" @ionInput="onContent($event)"></ion-input>
        </ion-item>
        <br>
        User {{ input }} will be reported! <br><br>
        Reason: {{ content }}
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
} from '@ionic/vue';
import { Camera, CameraResultType, CameraSource, Photo } from '@capacitor/camera';
import { defineComponent, ref } from 'vue';
import { showToast } from '../toast'
import { addDonos } from '@/service';

import { Plugins } from '@capacitor/core';

export default defineComponent({
    name: 'Modal',
    components: { IonContent, IonHeader, IonTitle, IonToolbar, IonButtons, IonButton, IonItem, IonLabel, IonInput, IonRow, IonCol, },
    setup() {

        const input = ref('');
        const content = ref('');

        const takePhoto = async () => {
            const photo = await Camera.getPhoto({
                resultType: CameraResultType.Uri,
                source: CameraSource.Camera,
                quality: 100,
            });
        };
        return {
            takePhoto, input, content
        };
    },
    methods: {
        cancel() {
            return modalController.dismiss(null, 'cancel');
        },
        confirm() {
            addDonos(this.content, '1', this.input)
            showToast("Good job! :)")
            return modalController.dismiss(null, 'confirm');
        },
        onInput(ev: any) {
            const value = ev.target!.value;
            this.input = value;
        },
        onContent(ev: any) {
            const value = ev.target!.value;
            this.content = value;
        }
    },
});
</script>