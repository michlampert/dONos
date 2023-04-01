import { toastController } from "@ionic/vue";

export async function showToast(text: string) {
    const toast = await toastController.create({
        message: text,
        duration: 1000,
        position: 'bottom'
    });

    await toast.present();
}