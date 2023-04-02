<template>
  <ion-fab slot="fixed" vertical="bottom" horizontal="end">
    <ion-fab-button id="open-modal" expand="block" @click="openModal()">
      <ion-icon :icon="add"></ion-icon>
    </ion-fab-button>
  </ion-fab>
</template>

<script lang="ts">
import {
  IonButtons,
  IonButton,
  IonModal,
  IonHeader,
  IonContent,
  IonToolbar,
  IonTitle,
  IonItem,
  IonInput,
  IonLabel,
  IonFab,
  IonFabButton,
  IonIcon,
  IonRow,
  IonCol,
  modalController,
} from '@ionic/vue';
import { defineComponent, ref } from 'vue';
import { add } from 'ionicons/icons';
import { Camera, CameraResultType, CameraSource, Photo } from '@capacitor/camera';
import Modal from './NewDenunciationModal.vue'

export default defineComponent({
  setup() {
    return {
      add
    }
  },
  components: {
    IonButtons,
    IonButton,
    IonModal,
    IonHeader,
    IonContent,
    IonToolbar,
    IonTitle,
    IonItem,
    IonInput,
    IonLabel,
    IonFab,
    IonFabButton,
    IonIcon,
    IonRow,
    IonCol,
  },
  data() {
    return {};
  },
  methods: {
    async openModal() {
      const modal = await modalController.create({
        component: Modal,
      });
      modal.present();

      const { data, role } = await modal.onWillDismiss();

      if (role === 'confirm') {

      }
      else {

      }
    },
  },
});
</script>