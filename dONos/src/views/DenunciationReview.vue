<template>
  <ion-page>
    <Header></Header>
    <ion-content :fullscreen="true">
      <ion-header collapse="condense">
        <ion-toolbar>
          <ion-title size="large">Denunciation Review</ion-title>
        </ion-toolbar>
      </ion-header>

      dupa
    </ion-content>
  </ion-page>
</template>

<script lang="ts">
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent } from '@ionic/vue';
import { defineComponent } from 'vue'
import Header from '@/components/Header.vue';

export default defineComponent({
  setup() {


    return {}
  },
  components: {
    IonPage, IonHeader, IonToolbar, IonTitle, IonContent,

    Header
  }
})
</script>

<style scoped></style>