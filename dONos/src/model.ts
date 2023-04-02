import { ribbonOutline, diamondOutline, personOutline, thumbsUpOutline, timeOutline, calendarOutline, calendarNumberOutline, cameraOutline, peopleOutline, mapOutline, flameOutline, fishOutline, flowerOutline, fingerPrintOutline, trophyOutline, cartOutline, nutritionOutline, bedOutline, telescopeOutline, logoFacebook, gameControllerOutline, logoAmazon, flame } from "ionicons/icons"

export interface Points {
    plus: number,
    minus: number,
}

export interface Person {
    id?: string,
    name: string,
    points: Points,
}

export interface Denunciation {
    id: string,
    donor_name: string,
    receiver_name: string,
    content: string,
}

export const achievments = [
    {
        icon: ribbonOutline,
        title: "Donos tygodnia",
        desc: "Donos wyróżniający się na tle innych złożonych w danym tygodniu. Najbardziej dotkliwy, najzabawniejszy, a może została zgłoszona najtrudniejsza do wykrycia zbrodnia? ",
    },
    {
        icon: diamondOutline,
        title: "Senior donosiciel",
        desc: "Zaawansowany donosiciel, który wykonał już 100 donosów.",
    },
    {
        icon: personOutline,
        title: "Donosiciel",
        desc: "Osoba dla której donosy nie są już niczym nowym. Odblokowany po 10 donosach.",
    },
    {
        icon: thumbsUpOutline,
        title: "Junior donosiciel",
        desc: "Brawo! Wykonałeś już swój pierwszy donos!",
    },
    {
        icon: timeOutline,
        title: "Pierwszy donos w ciągu dnia.",
        desc: "Super! Zacząłeś dzień od donosu.",
    },
    {
        icon: calendarOutline,
        title: "Tydzień donoszenia",
        desc: "Wykonałeś donosy każdego dnia w danym tygodniu.",
    },
    {
        icon: calendarNumberOutline,
        title: "Wytrwały donosiciel",
        desc: "Twoja wytrwałość jest godna podziwu! Wykonałeś donosy każdego dnia w danym miesiącu.",
    },
    {
        icon: cameraOutline,
        title: "Fotodonos",
        desc: "Zamieściłeś w donosie zdjęcie.",
    },
    {
        icon: peopleOutline,
        title: "Współdonos",
        desc: "Ten sam donos zamieściły co najmniej dwie osoby.",
    },
    {
        icon: mapOutline,
        title: "Wszystkie lokalizacje",
        desc: "Twoje donosy dotyczyły wszystkich dostępnych miejsc w obrębie korpomapy: biuro, kuchnia, pokój socjalny, toaleta.",
    },
    {
        icon: mapOutline,
        title: "Cichacz",
        desc: "Dbasz o niezakłócanie ciszy w biurze.",
    },
    {
        icon: flameOutline,
        title: "Strażak",
        desc: "Pilnujesz, żeby nikt nie przypalał jedzenia w biurowej kuchence mikrofalowej.",
    },
    {
        icon: fishOutline,
        title: "Śledzik",
        desc: "Pilnujesz, żeby nie odgrzewać we wspólnej mikroweli śmierdzącego jedzenia - w tym ryb.",
    },
    {
        icon: fishOutline,
        title: "Segregator",
        desc: "Pilnujesz, żeby segregować prawidłowo śmieci",
    },
    {
        icon: flowerOutline,
        title: "Czyścioszek",
        desc: "Pilnujesz, żeby współpracownicy dbali o higienę osobistą, oszczędzając innym przykrych doświadczeń.",
    },
    {
        icon: flowerOutline,
        title: "Prohibitor",
        desc: "Zgłosiłeś picie alkoholu w pracy lub przyjście do niej pijanym.",
    },
    {
        icon: fingerPrintOutline,
        title: "Bezpiecznik",
        desc: "Zgłosiłeś niezablokowanie komputera po odejściu od stanowiska pracy lub inne nadużycie prowadzące do narażenia danych firmy.",
    },
    {
        icon: trophyOutline,
        title: "Achievement achievement",
        desc: "Dostałeś achievement za zebranie 15 achievementów.",
    },
    {
        icon: cartOutline,
        title: "Schowaj kumplowi rzeczy",
        desc: "Ktoś doniósł, że schowałeś komuś rzeczy.",
    },
    {
        icon: nutritionOutline,
        title: "Obrońca owoców",
        desc: "Pilnujesz, żeby nikt nie wychodził ponad swój owocowy przydział w owocowy czwartek - zgłosiłeś to naganne zachowanie.",
    },
    {
        icon: bedOutline,
        title: "Śpioszek",
        desc: "Doniosłeś o spaniu w pracy.",
    },
    {
        icon: bedOutline,
        title: "Top model",
        desc: "Doniosłeś o nieodpowiednim ubiorze w pracy.",
    },
    {
        icon: telescopeOutline,
        title: "Sokole oko",
        desc: "Zgłosiłeś coś trudnego do zauważenia.",
    },
    {
        icon: logoFacebook,
        title: "Marek Zuckerberg",
        desc: "Zgłosiłeś siedzenie w pracy na facebooku.",

    },
    {
        icon: logoFacebook,
        title: "YouTube destroyer",
        desc: "Zgłosiłeś oglądanie filmików w czasie pracy.",

    },
    {
        icon: gameControllerOutline,
        title: "Game over",
        desc: "Doniosłeś na granie w godzinach pracy.",

    },
    {
        icon: logoAmazon,
        title: "Besos",
        desc: "Zgłosiłeś robienie zakupów w czasie pracy.",

    },
]