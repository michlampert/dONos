<template>
  <ion-page>
    <ion-tabs>
      <ion-router-outlet></ion-router-outlet>
      <ion-tab-bar slot="bottom">
        <ion-tab-button tab="profile" href="/tabs/profile">
          <ion-icon aria-hidden="true" :icon="personCircle" />
          <ion-label>Profile</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="leaderboard" href="/tabs/leaderboard">
          <ion-icon aria-hidden="true" :icon="list" />
          <ion-label>Leaderboard</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="achievements" href="/tabs/achievements">
          <ion-icon aria-hidden="true" :icon="trophy" />
          <ion-label>Achievements</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="review" href="/tabs/review">
          <ion-icon aria-hidden="true" :icon="glasses" />
          <ion-label>Review</ion-label>
        </ion-tab-button>
      </ion-tab-bar>
    </ion-tabs>
  </ion-page>
</template>

<script setup lang="ts">
import { IonTabBar, IonTabButton, IonTabs, IonLabel, IonIcon, IonPage, IonRouterOutlet } from '@ionic/vue';
import { trophy, personCircle, list, glasses } from 'ionicons/icons';
</script>
