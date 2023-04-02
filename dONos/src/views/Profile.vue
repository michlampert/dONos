<template>
  <ion-page>
    <Header></Header>
    <ion-content :fullscreen="true">
      <ion-header collapse="condense">
        <ion-toolbar>
          <ion-title size="large">Profile</ion-title>
        </ion-toolbar>
      </ion-header>
      <ion-item>
        <ion-input label-placement="floating" fill="outline" placeholder="Podaj nick"></ion-input>
      </ion-item>
      <ion-item>
        <ion-button size="default" shape="round">
          <ion-icon slot="start" :icon="addCircle"></ion-icon>
          <ion-label>dołącz</ion-label>
        </ion-button>

        <ion-button size="default" shape="round">
          <ion-icon slot="start" :icon="arrowForwardCircle"></ion-icon>
          <ion-label>stwórz nową</ion-label>
        </ion-button>
      </ion-item>
      Hello {{ myName }}! 

      

      <NewDenunciation></NewDenunciation>
    
    </ion-content>

  </ion-page>
</template>

<script lang="ts">
import { profileStore } from '@/state';
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent, IonInput, IonItem, IonButton, IonLabel, IonIcon } from '@ionic/vue';
import { addCircle, arrowForwardCircle } from 'ionicons/icons';
import { mapStores } from 'pinia';
import { defineComponent, ref } from 'vue'
import Header from '@/components/Header.vue';
import NewDenunciation from '@/components/NewDenunciation.vue';

import { getMyName } from '../service'

export default defineComponent({
  setup() {
    const myName=ref('')

    const getName = async ()=> {
      const value = await getMyName(1);

      myName.value=value;
    };

    getName();

    return { addCircle, arrowForwardCircle, myName }
  },
  components: {
    IonPage, IonHeader, IonToolbar, IonTitle, IonContent, IonInput, IonItem, IonButton, IonLabel, IonIcon,

    Header,
    NewDenunciation,
  },
  computed: {
    ...mapStores(profileStore)
  }
})
</script>

<style scoped></style>