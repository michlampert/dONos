<template>
    <ion-item>
        <ion-avatar slot="start">
            <img src="https://ionicframework.com/docs/img/demos/avatar.svg" />
        </ion-avatar>

        <ion-label>
            <p><b><ion-text color="dark">{{ name }}</ion-text></b></p>
            <p><b>
                <ion-text color="">{{ points.plus - points.minus }}</ion-text>
                (
                <ion-text color="success">{{ points.plus }}</ion-text>
                /
                <ion-text color="danger">{{ points.minus }}</ion-text>
                )
            </b></p>
        </ion-label>
    </ion-item>
</template>

<script lang="ts">
import { checkmark } from 'ionicons/icons';
import { PropType, defineComponent } from 'vue'
import { Points } from '../model'
import { IonItem, IonAvatar, IonLabel, IonText } from '@ionic/vue';

export default defineComponent({
    props: {
        image: { type: String, default: "" },
        name: String,
        points: { type: Object as PropType<Points>, default: { plus: 0, minus: 0 } },
    },
    setup() {
        return { checkmark }
    },
    components: {
        IonItem, IonAvatar, IonLabel, IonText,
    }
})
</script>

<style scoped></style>