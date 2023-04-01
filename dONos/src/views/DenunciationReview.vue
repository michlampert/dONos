<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-title>Denunciation Review</ion-title>
      </ion-toolbar>
    </ion-header>
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

export default defineComponent({
    setup () {
        

        return {}
    },
    components: {
        IonPage, IonHeader, IonToolbar, IonTitle, IonContent
    }
})
</script>

<style scoped>

</style>