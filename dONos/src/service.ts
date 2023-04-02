import axios from "axios";
import { Person, Denunciation } from "./model";

const baseUrl = "http://172.20.47.165:5000" // nie wiem jaki

// const baseUrl = "http://172.18.0.1:5000" // nie wiem jaki


export async function addCompany(company: string) {
    await axios({
        method: 'post',
        url: `${baseUrl}/company/add/`,
        data: {
            name: company
        }
    });
}

export async function addEmployee(name: string, company_id: number) {
    await axios({
        method: 'post',
        url: `${baseUrl}/employee/add/`,
        data: {
            name,
            company_id
        }
    });
}

export function getLeaderBoard(company_id: number): Promise<Person[]> {
    return axios<Person[]>({
        method: 'get',
        url: `http://172.20.47.165:5000/leaderboard/?company_id=${company_id}`
    })
        .then(response => {console.log(response); return response.data})
}

export function addDonos(content: string, donor: string, receiver: string, image: string): void {
    axios<void>({
        method: 'post',
        url: `${baseUrl}/donos/add`,
        data: {
            content: content,
            donor_id: donor,
            receiver_id: receiver,
            image: image
        }
    });
}


export function getMyName(myId: number): Promise<string> {
    return axios<{name: string}>({
        method: 'get',
        url: `${baseUrl}/me/?id=${myId}`
      })
      .then(response => response.data.name)
}


export function acceptDonos(donosID: string): void {
    axios<void>({
        method: 'post',
        url: `${baseUrl}/donos/${donosID}/accept`
    })
}


export function rejectDonos(donosID: string): void {
    axios<void>({
        method: 'post',
        url: `${baseUrl}/donos/${donosID}/reject`
    })
}

export function superDonos(donosID: string): void {
    axios<void>({
        method: 'post',
        url: `${baseUrl}/donos/${donosID}/super`
    })
}

export function getDonos(companyID: number): Promise<Denunciation[]> {
    return axios<Denunciation[]>({
        method: 'get',
        url: `${baseUrl}/donos/?company_id=${companyID}`
    })
        .then(response => response.data)
}
