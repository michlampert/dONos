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
            <ion-label position="stacked">Target</ion-label>
            <ion-input :value="input" type="number" placeholder="Select name" @ionInput="onInput($event)"></ion-input>
        </ion-item>

        <ion-item>
            <ion-label position="stacked">Enter your name</ion-label>
            <ion-input :value="content" type="text" placeholder="Your name" @ionInput="onContent($event)"></ion-input>
        </ion-item>

        <ion-item>
            <ion-img :src="src" v-if="src != ''"></ion-img>
            <ion-button @click="takePhoto()" v-if="src == ''">Take Photo</ion-button>
        </ion-item>
        <ion-img v-if="base64Data != ''" :src="'data:image/jpeg;base64,' + base64Data"></ion-img>
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
    IonImg,
} from '@ionic/vue';
import { Camera, CameraResultType, CameraSource, Photo } from '@capacitor/camera';
import { Filesystem } from '@capacitor/filesystem';
import { defineComponent, ref } from 'vue';
import { showToast } from '../toast'
import { addDonos } from '@/service';
import { profileStore } from '@/state';
import { mapStores } from 'pinia';

export default defineComponent({
    name: 'Modal',
    components: { IonContent, IonHeader, IonTitle, IonToolbar, IonButtons, IonButton, IonItem, IonLabel, IonInput, IonRow, IonCol, IonImg },
    data() {
        return {
            src: "",
            base64Data: ""
        }
    },
    setup() {

        const input = ref('');
        const content = ref('');

        return {
            input, content
        };
    },
    methods: {
        cancel() {
            return modalController.dismiss(null, 'cancel');
        },
        confirm() {
            addDonos(this.content, '1', this.input, this.base64Data)
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
        },
        takePhoto() {
            Camera.getPhoto({
                resultType: CameraResultType.Base64,
                source: CameraSource.Camera,
                quality: 10,
            }).then(async base64 => {
                this.base64Data = base64.base64String!;
                console.log(this.base64Data)
            });
        }
    },
    computed: {
        ...mapStores(profileStore)
    }
});
</script>