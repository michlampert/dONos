<template>
  <ion-page>
    <Header></Header>
    <ion-content :fullscreen="true">
      <ion-item-sliding>
        <ion-item-options side="start" expandable>
          <ion-item-option color="success" @click="$emit('delete')" expandable>
            <!-- <ion-icon slot="icon-only" :icon="archive"></ion-icon> -->
            accept
          </ion-item-option>
        </ion-item-options>

        <ion-item-options side="end" expandable>
          <ion-item-option color="danger" @click="$emit('delete')" expandable>
            <!-- <ion-icon slot="icon-only" :icon="archive"></ion-icon> -->
            reject
          </ion-item-option>
        </ion-item-options>

        <ion-item>
          <ion-label>
            dupa
          </ion-label>
        </ion-item>
      </ion-item-sliding>

    </ion-content>
  </ion-page>
</template>

<script lang="ts">
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent, IonItemSliding, IonItemOptions, IonItemOption, IonItem, IonIcon, IonLabel } from '@ionic/vue';
import { defineComponent } from 'vue'
import Header from '@/components/Header.vue';

export default defineComponent({
  setup() {


    return {}
  },
  components: {
    IonPage, IonHeader, IonToolbar, IonTitle, IonContent, IonItemSliding, IonItemOptions, IonItemOption, IonItem, IonIcon, IonLabel,

    Header
  }
})
</script>

<style scoped></style>