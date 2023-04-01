import axios from "axios";
import { Person } from "./model";

const baseUrl = "" // nie wiem jaki


export function addCompany(company: string): Boolean {
    const [error, ] = axios({
        method: 'post',
        url: "localhost:5000/company/add/",
        data: {
            name: company
        }
      });
}

export function addEmployee(firstName: string, lastName: string, company_id: number): Boolean {
    const [error, ] = axios({
        method: 'post',
        url: "localhost:5000/employee/add/",
        data: {
            first_name: firstName,
            last_name: lastName,
            company_id: company_id
        }
      });
}

export function getLeaderBoard(company_id: number): Person[] {
    const [error, ] = axios({
        method: 'get',
        url: `localhost:5000/leaderboard/?company=${company_id}`
      });
}

export function addDonos(content: string, donor: number, receiver: number): Boolean {
    const [error, ] = axios({
        method: 'post',
        url: "localhost:5000/donos/add/",
        data: {
            content: content,
            donor_id: donor,
            receiver_id: receiver
        }
      });
}


export function getMyName(myId: number): string {
    const [error, ] = axios({
        method: 'get',
        url: `${baseUrl}/me/?id=${myId}`
      });
}
