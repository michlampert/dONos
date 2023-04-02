<template>
  <ion-page>
    <Header></Header>
    <ion-content :fullscreen="true">
      <ion-item-sliding v-for="denunciation in denunciations">
        <ion-item-options side="start" expandable>
          <ion-item-option color="success" @click="acceptDenunciation(denunciation.id)" expandable
            @ionSwipe="acceptDenunciation(denunciation.id)">
            <ion-icon slot="icon-only" :icon="checkmarkOutline"></ion-icon>
            accept
          </ion-item-option>

          <ion-item-option color="primary" @click="superDenunciation(denunciation.id)">
            <ion-icon slot="icon-only" :icon="heart"></ion-icon>
            super
          </ion-item-option>
        </ion-item-options>

        <ion-item-options side="end" expandable>
          <ion-item-option color="danger" @click="rejectDenunciation(denunciation.id)" expandable
            @ionSwipe="rejectDenunciation(denunciation.id)">
            <ion-icon slot="icon-only" :icon="closeOutline"></ion-icon>
            reject
          </ion-item-option>
        </ion-item-options>

        <DenunciationItem :denunciation="denunciation"></DenunciationItem>
      </ion-item-sliding>

    </ion-content>
  </ion-page>
</template>

<script lang="ts">
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent, IonItemSliding, IonItemOptions, IonItemOption, IonItem, IonIcon, IonLabel } from '@ionic/vue';
import { defineComponent } from 'vue'
import Header from '@/components/Header.vue';
import { showToast } from '@/toast';
import { getDonos } from '@/service';
import DenunciationItem from '../components/DenunciationItem.vue'
import { Denunciation } from '@/model';
import { checkmarkOutline, closeOutline, heart } from 'ionicons/icons';

export default defineComponent({
  data() {
    return {
      denunciations: Array<Denunciation>()
    }
  },
  setup() {


    return { checkmarkOutline, closeOutline, heart }
  },
  components: {
    IonPage, IonHeader, IonToolbar, IonTitle, IonContent, IonItemSliding, IonItemOptions, IonItemOption, IonItem, IonIcon, IonLabel,

    Header,
    DenunciationItem,
  },
  created() {
    getDonos(1).then(data => this.denunciations = data)
  },
  methods: {
    acceptDenunciation(id: string) {
      this.denunciations = this.denunciations.filter(data => data.id != id)
      showToast("accept")
    },
    superDenunciation(id: string) {
      this.denunciations = this.denunciations.filter(data => data.id != id)
      showToast("super")
    },
    rejectDenunciation(id: string) {
      this.denunciations = this.denunciations.filter(data => data.id != id)
      showToast("reject")
    },
  }
})
</script>

<style scoped></style>