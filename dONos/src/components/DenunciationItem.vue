<template>
    <ion-item>
        <ion-label>
            <ion-text>
                <p>Donor: <b>{{ denunciation?.donor_name }}</b></p>
                <p>Receiver: <b>{{ denunciation?.receiver_name }}</b></p>
                <p>Reason: {{ denunciation?.content }}</p>

                <p>
                    <ion-img v-if="denunciation?.base64Data"
                        :src="'data:image/jpeg;base64,' + denunciation?.base64Data"></ion-img>
                </p>
            </ion-text>
        </ion-label>
    </ion-item>
</template>

<script lang="ts">
import { IonIcon, IonImg, IonItem, IonLabel, IonText } from '@ionic/vue';
import { PropType, defineComponent } from 'vue'
import { Denunciation } from '../model'

export default defineComponent({
    props: {
        denunciation: Object as PropType<Denunciation>
    },
    setup() {


        return {}
    },
    components: {
        IonItem,
        IonIcon,
        IonLabel,
        IonText,
        IonImg,
    }
})
</script>

<style scoped>
ion-img {
    height: 200px;
}
</style>