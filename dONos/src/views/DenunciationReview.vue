<template>
  <ion-page>
    <Header></Header>
    <ion-content :fullscreen="true">
      <ion-item-sliding>
        <ion-item-options side="start" expandable>
          <ion-item-option color="success" @click="acceptDenunciation()" expandable @ionSwape="acceptDenunciation()">
            <!-- <ion-icon slot="icon-only" :icon="archive"></ion-icon> -->
            accept
          </ion-item-option>

          <ion-item-option color="primary" @click="superDenunciation()">
            <!-- <ion-icon slot="icon-only" :icon="archive"></ion-icon> -->
            super
          </ion-item-option>
        </ion-item-options>

        <ion-item-options side="end" expandable>
          <ion-item-option color="danger" @click="rejectDenunciation()" expandable @ionSwape="rejectDenunciation()">
            <!-- <ion-icon slot="icon-only" :icon="archive"></ion-icon> -->
            reject
          </ion-item-option>
        </ion-item-options>

          <DenunciationItem :denunciation="{
            id1: 'asd', id2: 'dsa' , content:'dupa'}"></DenunciationItem>
      </ion-item-sliding>

    </ion-content>
  </ion-page>
</template>

<script lang="ts">
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent, IonItemSliding, IonItemOptions, IonItemOption, IonItem, IonIcon, IonLabel } from '@ionic/vue';
import { defineComponent } from 'vue'
import Header from '@/components/Header.vue';
import { showToast } from '@/toast';
import DenunciationItem from '../components/DenunciationItem.vue'

export default defineComponent({
  setup() {


    return {}
  },
  components: {
    IonPage, IonHeader, IonToolbar, IonTitle, IonContent, IonItemSliding, IonItemOptions, IonItemOption, IonItem, IonIcon, IonLabel,

    Header,
    DenunciationItem,
  },
  methods: {
    acceptDenunciation() {
      showToast("accept")
    },
    superDenunciation() {
      showToast("super")
    },
    rejectDenunciation() {
      showToast("reject")
    },
  }
})
</script>

<style scoped></style>