<template>
    <ion-item>
        <ion-label>
            <ion-text>
                <p><b>{{ denunciation?.id1 }}</b></p>
                <p><b>{{ denunciation?.id2 }}</b></p>
                <p>{{ denunciation?.content }}</p>
            </ion-text>
        </ion-label>
    </ion-item>
</template>

<script lang="ts">
import { IonIcon, IonItem, IonLabel, IonText } from '@ionic/vue';
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
    }
})
</script>

<style scoped></style>